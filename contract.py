# { "Depends": "py-genlayer:latest" }
import genlayer as gl
class Lifecycle:
    DRAFT = 'DRAFT'; SEALED = 'SEALED'; ASSESSED = 'ASSESSED'; SUPERSEDED = 'SUPERSEDED'
class AccessClass:
    GENERAL_POPULATION = 'GENERAL_POPULATION'; SPECIAL_NEEDS = 'SPECIAL_NEEDS'; PET_FRIENDLY = 'PET_FRIENDLY'; UNKNOWN = 'UNKNOWN'

def _classify(text: str, facility: str, access: str):
    lower = text.lower()
    facility_ok = bool(facility) and facility.lower() in lower
    access_ok = ((access == AccessClass.PET_FRIENDLY and ('pet friendly' in lower or 'pet-friendly' in lower)) or
                 (access == AccessClass.GENERAL_POPULATION and 'general population' in lower) or
                 (access == AccessClass.SPECIAL_NEEDS and 'special needs' in lower))
    if 'will open' in lower or 'will be open' in lower: state = 'WILL_OPEN'
    elif 'now closed' in lower or ' closed' in lower: state = 'CLOSED'
    elif 'are now open' in lower or 'now open' in lower or ' open' in lower: state = 'OPEN'
    else: state = 'UNKNOWN'
    return state, facility_ok and access_ok

class EmergencyShelterServiceAvailabilityCovenant(gl.contract.Contract):
    owner: gl.Address
    lifecycle: str
    event_id: str
    authority: str
    facility: str
    section_time: str
    access_class: str
    content_hash: str
    assessment_result: str
    superseded_by: str

    def __init__(self, event_id: str, authority: str):
        self.owner = gl.message.sender_address
        self.lifecycle = Lifecycle.DRAFT
        self.event_id = event_id; self.authority = authority
        self.facility = ''; self.section_time = ''; self.access_class = AccessClass.UNKNOWN
        self.content_hash = ''; self.assessment_result = ''; self.superseded_by = ''

    def _owner(self):
        if gl.message.sender_address != self.owner: raise gl.vm.UserError('OWNER_ONLY')

    @gl.public.write
    def register_facility(self, facility: str, access_class: str):
        self._owner()
        if self.lifecycle != Lifecycle.DRAFT or not facility or access_class not in [AccessClass.GENERAL_POPULATION, AccessClass.SPECIAL_NEEDS, AccessClass.PET_FRIENDLY]: raise gl.vm.UserError('INVALID_FACILITY')
        self.facility = facility; self.access_class = access_class
        return 'REGISTERED'

    @gl.public.write
    def seal_section(self, section_time: str, content_hash: str):
        self._owner()
        if self.lifecycle != Lifecycle.DRAFT or not self.facility or len(content_hash) != 64: raise gl.vm.UserError('INVALID_SEAL')
        self.section_time = section_time; self.content_hash = content_hash; self.lifecycle = Lifecycle.SEALED
        return 'SEALED'

    @gl.public.write
    def assess_section(self, section_text: str, authority: str, section_time: str, content_hash: str):
        if self.lifecycle != Lifecycle.SEALED: raise gl.vm.UserError('INVALID_STATE')
        state, fields_ok = _classify(section_text, self.facility, self.access_class)
        ok = authority == self.authority and section_time == self.section_time and fields_ok and content_hash == self.content_hash
        self.assessment_result = 'HISTORICALLY_LISTED_OPEN' if ok and state == 'OPEN' else 'HISTORICALLY_LISTED_CLOSED' if ok and state == 'CLOSED' else 'UNKNOWN'
        self.lifecycle = Lifecycle.ASSESSED
        return self.assessment_result

    @gl.public.write
    def assess_from_url(self, source_url: str, authority: str, section_time: str):
        if self.lifecycle != Lifecycle.SEALED: raise gl.vm.UserError('INVALID_STATE')
        if source_url != 'https://newsroom.ocfl.net/2023/08/idalia-updates/': raise gl.vm.UserError('SOURCE_NOT_ALLOWLISTED')
        def fetch_and_classify():
            page = gl.nondet.web.render(source_url, mode='html')
            state, fields_ok = _classify(page, self.facility, self.access_class)
            return state, fields_ok
        def validate(leader_result):
            if not isinstance(leader_result, gl.vm.Return): return False
            state, fields_ok = fetch_and_classify()
            return (state, fields_ok) == tuple(leader_result.calldata[:2])
        state, fields_ok = gl.vm.run_nondet_unsafe(fetch_and_classify, validate)
        self.assessment_result = 'HISTORICALLY_LISTED_OPEN' if state == 'OPEN' and fields_ok else 'HISTORICALLY_LISTED_CLOSED' if state == 'CLOSED' and fields_ok else 'UNKNOWN'
        self.lifecycle = Lifecycle.ASSESSED
        return self.assessment_result

    @gl.public.write
    def supersede_section(self, child_event_id: str):
        self._owner()
        if self.lifecycle != Lifecycle.ASSESSED or not child_event_id: raise gl.vm.UserError('INVALID_SUPERSESSION')
        self.superseded_by = child_event_id; self.lifecycle = Lifecycle.SUPERSEDED
        return 'SUPERSEDED'

    @gl.public.view
    def get_assessment(self) -> dict:
        return {'event_id': self.event_id, 'authority': self.authority, 'facility': self.facility, 'section_time': self.section_time, 'access_class': self.access_class, 'published_state': self.assessment_result, 'evidence_state': 'VERIFIED' if self.assessment_result else 'UNRESOLVED', 'capacity': 'NOT_ASSERTED', 'current_availability': 'NOT_ASSERTED', 'lifecycle': self.lifecycle, 'superseded_by': self.superseded_by}

    @gl.public.view
    def read_historical_listing(self) -> str:
        return self.assessment_result or 'UNKNOWN'
