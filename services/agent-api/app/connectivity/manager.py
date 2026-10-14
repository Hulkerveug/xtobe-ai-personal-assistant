# Connectivity Manager (Phase G mock)
from .mock_providers import MockEthernet, MockWiFi, MockCellular, MockStarlinkTerminal
from .interface import ProviderStatus, TransportState

class ConnectivityManager:
    def __init__(self, providers=None, policy=None):
        # providers: list of provider instances (mock)
        self.providers = providers or [MockEthernet(True), MockWiFi(), MockCellular(True), MockStarlinkTerminal(False, False)]
        self.policy = policy or {}

    def probe_all(self):
        statuses = [p.probe() for p in self.providers]
        return {s.provider_id: s for s in statuses}

    def recommend(self):
        statuses = self.probe_all().values()
        # simple ranking: connected & low latency preferred
        ranked = sorted(statuses, key=lambda s: (0 if s.state==TransportState.CONNECTED else 1, s.latency_ms or 9999))
        best = ranked[0] if ranked else None
        return best

    def simulate_scenario(self, scenario_name: str):
        # change internal mock provider states for demo scenarios
        if scenario_name == 'ethernet_disconnect_then_cellular':
            # bring ethernet down
            for p in self.providers:
                if p.id()=='eth0': p._up=False
                if p.id()=='cell0': p.available=True
        if scenario_name == 'starlink_detected':
            for p in self.providers:
                if p.id()=='starlink0': p.present=True; p.gateway_reachable=True
        return self.probe_all()
