# Mock connectivity providers for Phase G
from .interface import ProviderStatus, TransportState
from datetime import datetime

class MockEthernet:
    def __init__(self, up: bool = True):
        self._up = up
    def id(self): return 'eth0'
    def name(self): return 'Ethernet'
    def probe(self):
        return ProviderStatus(provider_id=self.id(), name=self.name(), state=(TransportState.CONNECTED if self._up else TransportState.DISCONNECTED), latency_ms=5.0 if self._up else None, last_checked=datetime.utcnow().isoformat(), details={})

class MockWiFi:
    def __init__(self, ssid='Office-WiFi', strength_dbm=-60):
        self.ssid=ssid; self.strength=strength_dbm
    def id(self): return 'wifi0'
    def name(self): return f'Wi-Fi ({self.ssid})'
    def probe(self):
        return ProviderStatus(provider_id=self.id(), name=self.name(), state=TransportState.CONNECTED, latency_ms=20.0, signal_dbm=self.strength, last_checked=datetime.utcnow().isoformat(), details={'ssid':self.ssid})

class MockCellular:
    def __init__(self, available=True, rssi=-85):
        self.available=available; self.rssi=rssi
    def id(self): return 'cell0'
    def name(self): return 'Cellular'
    def probe(self):
        state = TransportState.CONNECTED if self.available else TransportState.DISCONNECTED
        return ProviderStatus(provider_id=self.id(), name=self.name(), state=state, latency_ms=80.0 if self.available else None, signal_dbm=self.rssi if self.available else None, last_checked=datetime.utcnow().isoformat(), details={})

class MockStarlinkTerminal:
    def __init__(self, present=False, gateway_reachable=False):
        self.present = present
        self.gateway_reachable = gateway_reachable
    def id(self): return 'starlink0'
    def name(self): return 'Starlink Terminal (mock)'
    def probe(self):
        if not self.present:
            state = TransportState.DISCONNECTED
        elif self.gateway_reachable:
            state = TransportState.CONNECTED
        else:
            state = TransportState.DEGRADED
        return ProviderStatus(provider_id=self.id(), name=self.name(), state=state, latency_ms=120.0 if self.gateway_reachable else None, last_checked=datetime.utcnow().isoformat(), details={'present':self.present,'gateway':self.gateway_reachable})
