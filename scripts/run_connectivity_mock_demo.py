import requests
from app.connectivity.manager import ConnectivityManager

# Smoke demo (local-only). This script must NOT call external network.
if __name__=='__main__':
    cm = ConnectivityManager()
    print('Initial providers:')
    for k,v in cm.probe_all().items():
        print(k, v.name, v.state, 'latency', v.latency_ms)
    print('\nSimulating ethernet disconnect then cellular:')
    cm.simulate_scenario('ethernet_disconnect_then_cellular')
    for k,v in cm.probe_all().items():
        print(k, v.name, v.state, 'latency', v.latency_ms)
    print('\nSimulating Starlink present:')
    cm.simulate_scenario('starlink_detected')
    for k,v in cm.probe_all().items():
        print(k, v.name, v.state, 'latency', v.latency_ms)
