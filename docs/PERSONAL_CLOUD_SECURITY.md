# Personal Cloud Security (Design-only)

Goals
- Ensure confidentiality, integrity, and availability for each client's personal cloud while preserving user control over data and sharing.

Core controls
- Encryption
  - Data encrypted at rest using per-tenant data keys.
  - Keys protected by a KMS or hardware-backed key store (design mock only).
- Access control
  - Device-bound credentials and per-device access policies.
  - Short-lived session tokens and refresh flows.
- Sync integrity
  - Conflict resolution policy and audit logs for all changes.
- Backup & recovery
  - Encrypted backups with retention policies; explicit delete/export flows initiated by the client.
- Regional residency
  - Tenant metadata tag selecting storage region; mock implementations only.

Operational considerations
- Logging and monitoring: redact sensitive fields; retain auditable approval entries.
- Incident response: defined playbooks and human RM escalation channels.
- Privacy: minimize data collection; enable data export and deletion APIs.

Mock threats and mitigations
- Stolen device: remote revocation, per-device key wipe
- Compromised RM credentials: least-privilege scopes, session time limits, audit alerting

Developer notes
- Use environment variables for secrets in local dev; add .env.example (not included here).
- All designs in this repo are non-production mock contracts.
