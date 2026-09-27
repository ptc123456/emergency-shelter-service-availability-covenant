"""Deterministic validation for historically scoped shelter listings."""
from dataclasses import dataclass
from enum import Enum
import hashlib
import re

class Lifecycle(str, Enum):
    DRAFT='DRAFT'; SEALED='SEALED'; ASSESSED='ASSESSED'; SUPERSEDED='SUPERSEDED'
class PublishedState(str, Enum):
    OPEN='OPEN'; CLOSED='CLOSED'; WILL_OPEN='WILL_OPEN'; UNKNOWN='UNKNOWN'
class AccessClass(str, Enum):
    GENERAL_POPULATION='GENERAL_POPULATION'; SPECIAL_NEEDS='SPECIAL_NEEDS'; PET_FRIENDLY='PET_FRIENDLY'; UNKNOWN='UNKNOWN'

@dataclass(frozen=True)
class SectionAssessment:
    authority_match: bool
    section_time_match: bool
    facility_match: bool
    access_class: AccessClass
    published_state: PublishedState
    evidence_state: str
    result: str

def canonical_hash(text: str) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def assess_section(section_text: str, facility: str, access: AccessClass, authority: str,
                   expected_authority: str, section_time: str, expected_time: str,
                   content_hash: str, expected_hash: str) -> SectionAssessment:
    lower = section_text.lower()
    authority_match = authority == expected_authority and bool(authority)
    time_match = section_time == expected_time and bool(section_time)
    facility_match = facility.lower() in lower and bool(facility)
    access_match = access == AccessClass.PET_FRIENDLY and ('pet friendly' in lower or 'pet-friendly' in lower) or access == AccessClass.GENERAL_POPULATION and 'general population' in lower or access == AccessClass.SPECIAL_NEEDS and 'special needs' in lower
    if re.search(r'\bwill open\b|\bwill be open\b', lower): state = PublishedState.WILL_OPEN
    elif re.search(r'\bnow closed\b|\bclosed\b', lower): state = PublishedState.CLOSED
    elif re.search(r'\bare now open\b|\bnow open\b|\bopen\b', lower): state = PublishedState.OPEN
    else: state = PublishedState.UNKNOWN
    ok = authority_match and time_match and facility_match and access_match and content_hash == expected_hash
    result = 'HISTORICALLY_LISTED_OPEN' if ok and state == PublishedState.OPEN else 'HISTORICALLY_LISTED_CLOSED' if ok and state == PublishedState.CLOSED else 'UNKNOWN'
    return SectionAssessment(authority_match, time_match, facility_match and access_match, access, state, 'VERIFIED' if ok else 'UNRESOLVED', result)
