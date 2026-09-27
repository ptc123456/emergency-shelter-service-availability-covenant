# Emergency Shelter Service Availability Covenant

Contract-only Intelligent Contract for an archival, event-scoped receipt of what an official emergency-management update said about a named shelter. It never asserts current availability, capacity, routing, or admission.

## Lifecycle and API

`DRAFT -> SEALED -> ASSESSED -> SUPERSEDED`. The owner creates an event, registers a facility/access class, seals the authority-authored section timestamp and SHA-256 hash, and may supersede an assessed section. Anyone may submit the bounded section for assessment and read the result. `WILL_OPEN` is never treated as `OPEN`; mismatched authority, timestamp, facility, access category, or hash yields `UNKNOWN`.

Public methods: `register_facility`, `seal_section`, `assess_section`, `supersede_section`, `get_assessment`, `read_historical_listing`.

## Network and evidence status

Target is Studio Dev (chain 61997, `https://studio-dev.genlayer.com/api`) using the official release-candidate SDK `genlayer-js@2.0.0-rc.1` and its explicit `studioDevnet` preset. The current official network documentation confirms Studio development preview, chain 61997, and Explorer `https://explorer-studio-dev.genlayer.com`. Deployment evidence is recorded under `deployment/`; E2E remains incomplete until every required scenario is executed.

## Consensus engineering lessons

The authoritative basis is the publisher-authored section timestamp, not caller retrieval time. Validators must compare consequential fields (authority, section time, facility, access class, state verb, and content hash); explanations are display-only. Unavailable, changed, ambiguous, or contradictory evidence is `UNKNOWN` and cannot create a favorable state.

## Limitations

This is historical evidence only. It excludes reservations, notifications, maps, PII, payments, current status, capacity and admission decisions.
