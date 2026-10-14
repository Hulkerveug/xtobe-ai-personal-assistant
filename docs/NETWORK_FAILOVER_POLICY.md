# NETWORK_FAILOVER_POLICY.md

# Network Failover Policy (Phase G — Mock)

Default policy (recommended)
1. Preferred: Ethernet (wired)
2. Trusted Wi-Fi
3. Cellular (eSIM / physical SIM)
4. Satellite terminal (Starlink) — optional, manual approval

Policy factors
- Data budget and cost
- Latency requirement
- Security of network (trusted Wi-Fi vs public)
- Battery impact (mobile)
- User preference (manual override)

Policy engine behavior (mock)
- Evaluate available providers, rank by policy weights
- Recommend but do not automatically change connections unless OS supports and user approved
- Provide manual "Use Starlink" control that only simulates switching in demo
