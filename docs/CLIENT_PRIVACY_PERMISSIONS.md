# Client Privacy & Permissions (Design-only)

Principles
- Client control: explicit consent for access, sharing and third-party actions
- Transparency: every access attempt recorded and visible to client
- Revocability: clients can revoke access and require attestation of actions taken

Approval Center (mock)
- Request: { requester, action, resource, reason }
- Client UI: Approve / Deny / Approve with limited scope / Request more info
- System: Issue time-limited token on approval and log the event

Data export & deletion
- Export: authenticated client request initiates export job; client notified when ready
- Deletion: soft-delete then scheduled purge after retention window; clients may request immediate purge with confirmation steps

Third-party sharing
- Consent tokens with exact scope, expiry, and allowed recipients
- Humans (RMs) treated as third parties and require same approval workflows

Developer guidelines
- Never log full sensitive payloads in plaintext
- Use pseudonymization for analytics and debugging
