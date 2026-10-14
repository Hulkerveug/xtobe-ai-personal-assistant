# Relationship Management Model (Design-only)

Purpose
- Define how professional Relationship Managers (RMs) interact with clients and the Guardian platform without gaining unrestricted access to client vaults.

Roles
- Client: account owner with full control over approvals
- Relationship Manager (RM): human operator with scoped, auditable access
- Guardian AI: assistant agent performing automated tasks and preparing materials for RM

Key flows
1. Onboarding
   - Client consents to RM introduction and defines permitted scopes (view-only, edit-with-approval, etc.)
2. Service request
   - Client or Guardian raises a service ticket. RM can view ticket metadata and request scoped access if needed.
3. Scoped access approval
   - RM requests access via Approval Center -> client approves -> short-lived scoped token issued -> access logged
4. Escalation
   - RM escalates to specialist or senior RM; escalation path recorded in ticket and audit logs

Permissions model
- RBAC + attribute checks (ABAC) including:
  - role (RM, RM-lead)
  - ticket_id, client_consent_id
  - resource_type and resource_scope

Audit and compliance
- All RM actions generate audit events with reason, ticket link, and client consent reference.
- Periodic review of RM activity and reassignment procedures.

Privacy safeguards
- RMs cannot extract bulk exports without explicit client approval.
- Sensitive operations require multi-party approval for high-risk categories (financial, legal).
