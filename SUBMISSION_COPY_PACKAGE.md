# Submission Copy Package

Title
Emergency Shelter Service Availability Covenant

Repository
https://github.com/ptc123456/emergency-shelter-service-availability-covenant

Commit
476e85db68bfa898e486d73d6c1195cf099daa83

Notes / Description
This contract records an authoritative, event-scoped historical shelter listing for Hurricane Idalia. An owner seals a dated source section with its content hash; the contract then evaluates the supplied historical section against the registered authority, facility, access class, timestamp, and hash. It distinguishes historically listed open, historically listed closed, and unknown results, preserves superseded history, rejects unauthorized or invalid lifecycle transitions, and explicitly does not assert current capacity or current availability. Studio Dev evidence covers deployment, open and closed paths, a scheduled-opening counterexample, mismatch handling, authorization failure, invalid transition, replay rejection, and supersession.

Studio Dev evidence
- Network: Studio Dev, chain 61997
- Deployments and transaction receipts: deployment/DEPLOYMENT_EVIDENCE.md and deployment/E2E_MATRIX.md
- Explorer: https://explorer-studio-dev.genlayer.com
- Latest tested source hash: 3bf0a73332b0d0f3dbe011559a672ee87cf55f7d0d58089916c63866d1e5fc49

Source
https://github.com/ptc123456/emergency-shelter-service-availability-covenant/blob/main/contract.py

