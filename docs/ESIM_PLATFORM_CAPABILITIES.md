# ESIM_PLATFORM_CAPABILITIES.md

# eSIM Platform Capabilities (Reference)

Summary
- eSIM provisioning and switching is controlled by OS-level APIs and carrier entitlements (Apple / Android differences).
- XTOBE can present capability information, guidance, and user-facing instructions, but must not attempt programmatic installation without explicit OS/carrier approvals.

What XTOBE can do (mock / UI only)
- Query device-reported capability (mocked)
- Show whether multiple eSIM profiles are present (mock)
- Provide carrier activation guidance and links (user-initiated)
- Track user-declared plan metadata (manual entry)
- Monitor usage if OS or carrier exposes metrics (rare; mock otherwise)

Security
- Do not store carrier credentials
- Do not attempt to proxy provisioning flows
