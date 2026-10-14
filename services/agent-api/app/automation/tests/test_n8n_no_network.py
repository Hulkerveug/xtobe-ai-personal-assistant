import pytest
from .. import n8n_adapter

def test_n8n_adapter_no_network(monkeypatch):
    # monkeypatch network-related modules to ensure adapter doesn't call them
    called = {'net': False}
    def fake_requests_get(*args, **kwargs):
        called['net'] = True
    monkeypatch.setattr('requests.get', fake_requests_get, raising=False)
    res = n8n_adapter.mock_trigger_workflow('wf-1', {'a':1})
    assert res.get('workflowId') == 'wf-1' or res.get('workflowId') == 'wf-1'
    assert called['net'] == False
