# XTOBE ONE Product Roadmap (Design-only)

Phase 0 — Foundation (now)
- Preserve Phase A frontend verified work in xtobe-ai-personal-assistant repo
- Add design docs, mock API contracts, and ci checks

Phase 1 — Personal Cloud (MVP)
- Minimal encrypted storage prototype (mock keys)
- Device sync and per-device registration UI
- /health and /v1/demo endpoints for frontend integration

Phase 2 — Guardian Personal AI
- Typed interfaces for profile, calendar, knowledge vault
- Mock assistant workflows and approval flows

Phase 3 — Relationship Management
- RM onboarding UI and ticketing model
- Scoped access requests and Approval Center

Phase 4 — Financial Connect (mock)
- Provider-neutral API contracts
- Demo flows: account aggregation, payment request (no money movement)

Phase 5 — Device Ecosystem
- Pairing, revocation, telemetry

Phase 6 — Testing & Compliance
- Tenant isolation tests, RM permission tests, audit integrity

Next immediate milestones (next 1–2 sprints)
1. Commit Phase-A frontend snapshot and docs (done by this change)
2. Add CI for TypeScript/Vitest/build checks
3. Add minimal FastAPI demo backend with /health
4. Add .env.example and contributor guidance

Notes
- All deliverables are design and mock contracts only. No real secrets, credentials, or live transactions will be included.
