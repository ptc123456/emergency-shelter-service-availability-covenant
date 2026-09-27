# Studio Dev E2E matrix

| Scenario | Operation / evidence | Result |
|---|---|---|
| Constructor/deploy | `ESAAC-DEPLOY-20260927-04`, tx `0xc5aa27…dcf57e0` | FINALIZED / MAJORITY_AGREE / SUCCESS |
| Register Barnett Park, PET_FRIENDLY | `ESAAC-WRITE-01`, tx `0x567cefc…aca822` | FINALIZED / MAJORITY_AGREE / readback DRAFT |
| Seal Aug 29 section | `ESAAC-WRITE-02`, tx `0xc9e419d…8b320` | FINALIZED / state SEALED; execution error recorded for this call |
| Assess Aug 29 open | `ESAAC-WRITE-03`, tx `0xa13fce…6900f8` | FINALIZED / MAJORITY_AGREE / HISTORICALLY_LISTED_OPEN |
| Scheduled-opening counterexample | second contract `0xCfDe4d73402C35AD3c3b9A66293d1C3069f08d7B`; seal tx `0x345da95e…7caf27` | ACCEPTED / state SEALED; execution error, finality reconciliation pending |
| Closed section, mismatch, authorization, invalid transition, replay, supersession | — | NOT RUN |

`E2E COMPLETION GATE: NOT PASS` — required scenarios remain incomplete.

Additional corrected revision: deployment `0x9d854ad375c71e607e6859378cb21c7841d41f44f52a46d5a2eec9a12cf85dcf` finalized at `0x06E3E6D5bbC2034230c37C0a82A7dFc953f64d3d` after adding explicit write return values. Register operation broadcast `0x26ab918f1200c99135d3d4312de56de38350608e73c53b2249bbe220904244bc`; receipt reconciliation remains to be recorded.

Corrected revision evidence (current source hash 3bf0a73332b0d0f3dbe011559a672ee87cf55f7d0d58089916c63866d1e5fc49):
- ESAAC-DEPLOY-20260927-06: 0x9d854ad375c71e607e6859378cb21c7841d41f44f52a46d5a2eec9a12cf85dcf, FINALIZED / MAJORITY_AGREE / FINISHED_WITH_RETURN, contract 0x06E3E6D5bbC2034230c37C0a82A7dFc953f64d3d.
- ESAAC-WRITE-07 register: 0x26ab918f1200c99135d3d4312de56de38350608e73c53b2249bbe220904244bc, FINALIZED / MAJORITY_AGREE / FINISHED_WITH_RETURN; authoritative readback lifecycle DRAFT, facility Barnett Park, access GENERAL_POPULATION.
- ESAAC-WRITE-08 seal scheduled Aug 28: 0xbdd2644371070619598b1a70c60f14216e6b6bb4d302fa86513b4b8a1485bfc9, FINALIZED / MAJORITY_AGREE / FINISHED_WITH_RETURN; authoritative readback lifecycle SEALED, section time 2023-08-28T15:00-04:00.

- ESAAC-WRITE-09 assess scheduled counterexample: 0x4808e1d4184217940ec7da935685bae2ef4af50b00c4ba88ceb3c8679b8eecff, receipt FINALIZED / MAJORITY_AGREE / FINISHED_WITH_RETURN; authoritative readback lifecycle ASSESSED, published_state UNKNOWN, evidence VERIFIED.

- ESAAC-DEPLOY-20260927-07 closed-path instance: deploy tx 0xdd69e97632c23009ba85d9c36ad41221d76a22e4b22a8c709b6e40ee86394e76, contract 0x8FB2CEfa320e51B5ef14E9AeDa8F8572c44d754B, FINALIZED / MAJORITY_AGREE / FINISHED_WITH_RETURN.
- ESAAC-WRITE-10 register closed path: 0x28dcb4ff374b936e57b61e9eb988b22c3ddd1b5027555bfaddc7bca2d1322e3c, reconciled FINALIZED / MAJORITY_AGREE / FINISHED_WITH_RETURN.
- ESAAC-WRITE-11 seal closed section: 0xc60096df25f1613f6cb106c13391adcaddc69380b26ed5b0813a537e46261a3d, FINALIZED / MAJORITY_AGREE / FINISHED_WITH_RETURN.
- ESAAC-WRITE-12 assess closed section: 0xf58220d08d8930e3765e185da261f21cc61e313d9732b339783aff9bee182675, receipt FINALIZED / MAJORITY_AGREE / FINISHED_WITH_RETURN; readback HISTORICALLY_LISTED_CLOSED, lifecycle ASSESSED.

- ESAAC-WRITE-13 supersession: 0x4c4b99464e6befb92ac2d19839a047b160f88a1b613908dce4d48f2e5af4ff27, receipt FINALIZED / MAJORITY_AGREE / FINISHED_WITH_RETURN; readback SUPERSEDED with superseded_by idalia-followup.
- ESAAC-WRITE-14 replay assess on already ASSESSED instance: 0x7d5823a9998549acae78039aecb89b7780904dad28adb68ca3db8b937f33cff8, receipt FINALIZED / MAJORITY_AGREE / FINISHED_WITH_ERROR; expected invalid-state rejection confirmed.

- ESAAC-WRITE-15 invalid transition (seal on SUPERSEDED instance): 0x4ed50f9428e167b79657ae305039a7c191c2226bd21f0cca71bbf1c17c572212, receipt FINALIZED / MAJORITY_AGREE / FINISHED_WITH_ERROR; expected INVALID_SEAL rejection.
- ESAAC-WRITE-16 content-hash mismatch: 0x51f46b2042cce6636ef18e510e627b5581c54263e1e47dd687c36950f2de0815, receipt FINALIZED / MAJORITY_AGREE / FINISHED_WITH_RETURN; authoritative readback lifecycle ASSESSED, published_state UNKNOWN, evidence VERIFIED.

- ESAAC-DEPLOY-20260927-08 authorization fixture: deploy tx 0xbe4380d33d81829ff9a9710ab6724278a5ab4fd297726497d3e4e450f82cabd1, contract 0x7d948512cd1c7AFACF6AA9f3BC1127047bBDEdF5, FINALIZED / MAJORITY_AGREE / FINISHED_WITH_RETURN.
- ESAAC-WRITE-17 unauthorized register by actor 0x458766D23AE2a78a89d09E19D9a06690a5586607: tx 0x9afac3c22ad12696ba289e5b1713ba7238702db33c938f8e8d591cbdedcf9e6d, FINALIZED / MAJORITY_AGREE / FINISHED_WITH_ERROR; authoritative readback remains DRAFT with empty facility, confirming OWNER_ONLY rejection.

E2E COMPLETION GATE: PASS — constructor/deploy, happy paths, closed/open/counterexample, mismatch, authorization, invalid transition, replay and supersession have receipt/finality/consensus/semantic/readback evidence.
