# STUDIO DEV TOOLCHAIN BLOCKED (SUPERSEDED)

Checked 2026-09-27 against the official network source of truth: `https://docs.genlayer.com/developers/networks` (last updated 2026-09-03).

## Official target

- Network/preset required by the documentation: explicit `studioDevnet` / `studio-dev`.
- Canonical RPC: `https://studio-dev.genlayer.com/api`.
- Chain ID: `61997` (`0xf22d`).
- Explorer: `https://explorer-studio-dev.genlayer.com`.
- The documentation requires a matching release-candidate CLI/SDK and explicitly forbids relabeling `studionet`.

## Installed and published toolchain checks

- Installed CLI: `genlayer 0.39.2`.
- Published CLI RCs checked: `0.40.0-rc1`, `0.40.0-rc2`, `0.40.0-rc.3`, `0.40.0-clarke.1` through `0.40.0-clarke.4`.
- Every checked CLI reports only `localnet`, `studionet`, `testnet-asimov`, and `testnet-bradbury`; none exposes `studio-dev` or `studioDevnet`.
- Installed Python SDK: `genlayer-py 0.16.3`; public latest queried: `0.18.0`. No published package metadata located a 61997 preset.

## Runtime evidence

1. Direct `eth_chainId` to the canonical Studio Dev RPC returned `0xf22d` (61997).
2. CLI deployment used the required endpoint and explicit account:

   `genlayer deploy --contract .\\contract.py --rpc https://studio-dev.genlayer.com/api --args idalia OrangeCounty`

3. Result: `InvalidChainId` from `eth_sendRawTransaction`, before a transaction hash was returned. No broadcast was retried.
4. The CLI source resolves its chain from the built-in network registry; `--rpc` replaces the endpoint but does not add/change the chain definition. Therefore it signs as `studionet` (61999) against Studio Dev (61997).

## Decision

`STUDIO DEV TOOLCHAIN BLOCKED` was the pre-SDK finding. It is superseded by the discovery and successful use of `genlayer-js@2.0.0-rc.1` with `studioDevnet`.

No network substitution, CLI patch, contract workaround, retry, broadcast, commit, or push is permitted. On-chain work stops here. Offline lint/tests and documentation remain valid; E2E is not PASS.

## Recheck 2026-09-27

The npm registry still reports stable `0.39.2` and RC tags through `0.40.0-clarke.4`; `genlayer network list` still has no `studio-dev`, while the canonical RPC still reports `0xf22d`. Compatibility is unchanged.
