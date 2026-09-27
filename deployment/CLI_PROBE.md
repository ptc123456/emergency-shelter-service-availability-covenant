# Studio Dev CLI probe

- CLI: `genlayer 0.39.2`
- SDK: `genlayer-py 0.16.3`; `genlayer-test 0.29.2`; `genvm-linter 0.11.1rc2`
- Current CLI network list: `localnet`, `studionet` (61999), `testnet-asimov`, `testnet-bradbury`; no `studio-dev` preset.
- Direct RPC: `POST https://studio-dev.genlayer.com/api` with `eth_chainId` returned `0xf22d` (61997).
- Broadcast attempt: `genlayer deploy --contract .\\contract.py --rpc https://studio-dev.genlayer.com/api --args idalia OrangeCounty`
- Result: `InvalidChainId` from RPC before transaction broadcast. No hash, receipt, or state change was produced; no blind retry was performed.
- Consequence: Studio Dev deployment and all E2E/finality/readback gates remain unverified. Git publication remains locked by the release order.
