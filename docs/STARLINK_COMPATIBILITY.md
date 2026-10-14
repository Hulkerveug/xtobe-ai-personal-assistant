# STARLINK_COMPATIBILITY.md

# Starlink Compatibility (Phase G — Mock)

Overview
- Treat Starlink as an access transport: terminal provides IP connectivity via a local router.
- Do NOT assume Starlink APIs beyond documented user-facing features.
- For Phase G: implement a read-only adapter (mock) that models terminal availability, gateway reachability, latency and usage metadata.

Capabilities (mocked)
- terminal.present: boolean
- gateway.reachable: boolean
- link.latency_ms: numeric
- usage.bytes_estimate: numeric (mock)
- plan.reference: user-entered plan metadata (no account integration)

Limitations
- No automatic eSIM provisioning
- No carrier- or direct-to-cell control
- No hardware activation

Regulatory note
- Presence of a license (like TDRA UAE) is not sufficient to enable any direct-to-cell functionality in XTOBE without local carrier coordination and device compatibility checks.
