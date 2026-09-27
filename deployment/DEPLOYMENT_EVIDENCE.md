# Studio Dev deployment evidence

- Toolchain: `genlayer-js@2.0.0-rc.1`, `studioDevnet`, chain `61997`.
- RPC: `https://studio-dev.genlayer.com/api`.
- Actor: `0xf5C66e5155a62E27047aD4ccE729593D6B9c03Fc`.
- Source revision hash for successful deploy: `1574b07696d0ba0c8c4974689db25b44b34373f235098993a173ab6fb5ecfef7`.
- Contract: `0x5291a8bB374Ef3819A30d7D09dC5690C0077fc54`.
- Deployment transaction: `0xc5aa27e994744b8161c7d6ea8c1c1682bd2550a6e9e6288c3848c2eb4dcf57e0`.
- Deployment result: `FINALIZED`, `MAJORITY_AGREE`, `FINISHED_WITH_RETURN`, leader and validator execution `SUCCESS`.
- Explorer: `https://explorer-studio-dev.genlayer.com/address/0x5291a8bB374Ef3819A30d7D09dC5690C0077fc54`.

The earlier fee-only failure (`0x85fae45bb518c665684abc57eda086bb261445189c67685eea7509b56fe42864`) was reconciled as `FeeValueMustBeNonZero`; no blind retry was made. The malformed-runner attempts are retained in operation files and are not claimed as passes.
