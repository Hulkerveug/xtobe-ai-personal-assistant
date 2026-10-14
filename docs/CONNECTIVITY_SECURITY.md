# CONNECTIVITY_SECURITY.md

# Connectivity Security (Phase G)

Principles
- Do not expose network diagnostics or credentials externally
- Label all simulated/hypothetical network status clearly as DEMO
- Avoid any operation that requires elevated OS or carrier privileges

Tests to include
- SSRF prevention for any HTTP probes (mocked)
- Spoofed connectivity state handling
- Duplicate event suppression
- Privacy checks on subscription data storage
