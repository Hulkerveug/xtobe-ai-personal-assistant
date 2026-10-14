"""
Connectivity provider interfaces and dataclasses (Phase G mock-only)
"""
from typing import Protocol, Dict, Any, Optional
from dataclasses import dataclass
from enum import Enum

class TransportState(Enum):
    CONNECTED = 'connected'
    CONNECTING = 'connecting'
    DEGRADED = 'degraded'
    DISCONNECTED = 'disconnected'
    UNKNOWN = 'unknown'

@dataclass
class ProviderStatus:
    provider_id: str
    name: str
    state: TransportState
    latency_ms: Optional[float] = None
    signal_dbm: Optional[float] = None
    metered: bool = False
    data_remaining_bytes: Optional[int] = None
    last_checked: Optional[str] = None
    details: Dict[str, Any] = None

class ConnectivityProvider(Protocol):
    def id(self) -> str: ...
    def name(self) -> str: ...
    def probe(self) -> ProviderStatus: ...

# Specific provider type aliases (implementations in mock_providers)
class EthernetProvider(ConnectivityProvider): ...
class WiFiProvider(ConnectivityProvider): ...
class CellularProvider(ConnectivityProvider): ...
class EsimCapabilityProvider(ConnectivityProvider): ...
class SatelliteTerminalProvider(ConnectivityProvider): ...
