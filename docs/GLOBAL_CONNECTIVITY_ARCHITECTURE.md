# GLOBAL_CONNECTIVITY_ARCHITECTURE.md

# XTOBE — Global Connectivity Architecture (Phase G)

Purpose
- Define a local-first connectivity foundation that supports Wi‑Fi/Ethernet, cellular (eSIM awareness), and satellite (Starlink terminal) as possible transports.
- Provide typed provider interfaces, a Connectivity Manager, mock providers for demo/testing, a Connectivity Dashboard UI stub, and test scaffolding.

Scope & constraints (Phase G)
- Local-only mocks and simulations.
- No network provisioning, no eSIM installs, no Starlink API calls, no purchases.
- All outputs must be labeled DEMO or PHASE_G_MOCK_ONLY where appropriate.

Key components
- Provider interfaces: EthernetProvider, WiFiProvider, CellularProvider, EsimCapabilityProvider, SatelliteTerminalProvider, MockConnectivityProvider
- Connectivity Manager: policy engine, preference rules, failover recommendations
- Mock providers: deterministic mock state sequences for unit tests and demos
- Connectivity Dashboard UI: Automation Center-style page showing transports and mock scenarios
- Subscription model: typed objects for XTOBE & third-party services (manual entry only)
- Tests: unit tests for policy, provider state mapping, Guardian state integration

Next steps
- Paste scaffold into repo, run local tests, iterate until stable, then prepare commit locally.
