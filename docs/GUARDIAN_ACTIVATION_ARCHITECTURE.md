# Guardian Activation Architecture

This document describes the implementation architecture for the XTOBE Final Guardian 2.0 activation UI (Phase A).

Overview
- Frontend: React + TypeScript (Vite recommended)
- Desktop shell: Tauri (not included in this commit; UI scaffold prepared)
- Backend: FastAPI health endpoint and SQLite initialization (local sidecar)

Key components
- GuardianActivationScreen: full-screen hero activation
- GuardianVoicePanel: mock voice UI / transcript
- GuardianStatusOverlay: reusable overlay for state indicators
- GuardianEmblemBadge: emblem used in header/sidebar
- ParticleNetworkOverlay: GPU-conscious particle links

State machine (frontend)
- idle -> activating -> listening_mock -> processing_mock -> verification_required -> ready -> transitioning_to_dashboard

Assets
- Add the provided artwork to: apps/desktop/src/assets/guardian/xtobe-final-guardian-2.0.png

Security
- Phase A is UI-only. No external integrations.
