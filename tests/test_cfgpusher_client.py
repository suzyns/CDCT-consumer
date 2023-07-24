import atexit
import logging

import pytest
from pact import Consumer, Like, Provider

from src.cfgpusher_client import CfgpusherClient

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

PACT_MOCK_HOST = "localhost"
PACT_MOCK_PORT = 1234
PACT_DIR = "pacts"

@pytest.fixture(scope="session")
def pact(request):
    provider = request.config.getoption("--provider")
    pact = Consumer("CDCT-consumer").has_pact_with(
        Provider(provider),
        host_name=PACT_MOCK_HOST,
        port=PACT_MOCK_PORT,
        pact_dir=PACT_DIR,
    )
    pact.start_service()
    atexit.register(pact.stop_service)
    yield pact


def test_get_file(pact):
    expected = "test2225"

    (
        pact.given("Cfgpusher returns file content")
        .upon_receiving("a get file request to Cfgpusher")
        .with_request("get", "/file/opt/ns/tenant/1113/watchlist2.json")
        .will_respond_with(200, body=Like(expected))
    )

    with pact:
        client = CfgpusherClient(f"http://{PACT_MOCK_HOST}:{PACT_MOCK_PORT}")
        file_conent = client.get_file("opt/ns/tenant/1113/watchlist2.json")
        assert file_conent == expected
        pact.verify()

def test_get_file_not_exist(pact):
    expected = {"message": "[Reason]: File /opt/ns/configshare/dp/opt/ns/tenant/1114/watchlist2.json doesn't exist."}
    (
        pact.given("Cfgpusher returns file not found")
        .upon_receiving("a get file request to Cfgpusher")
        .with_request("get", "/file/opt/ns/tenant/1114/watchlist2.json")
        .will_respond_with(404, body=expected)
    )

    with pact:
        client = CfgpusherClient(f"http://{PACT_MOCK_HOST}:{PACT_MOCK_PORT}")
        resp = client.get_file("opt/ns/tenant/1114/watchlist2.json")
        assert resp == expected

def test_get_file_not_exist2(pact):
    expected = {"message": "[Reason]: File /opt/ns/configshare/dp/opt/ns/tenant/1113/watchlist2.json doesn't exist."}
    (
        pact.given("Cfgpusher returns file not found")
        .upon_receiving("a get file request to Cfgpusher2")
        .with_request("get", "/file/opt/ns/tenant/1113/watchlist2.json")
        .will_respond_with(404, body=expected)
    )

    with pact:
        client = CfgpusherClient(f"http://{PACT_MOCK_HOST}:{PACT_MOCK_PORT}")
        resp = client.get_file("opt/ns/tenant/1113/watchlist2.json")
        assert resp == expected

def test_get_file_not_exist3(pact):
    expected = {"message": "[Reason]: File /opt/ns/configshare/dp/opt/ns/tenant/1113/watchlist2.json doesn't exist."}
    (
        pact.given("Cfgpusher returns file not found")
        .upon_receiving("a get file request to Cfgpusher3")
        .with_request("get", "/file/opt/ns/tenant/1112/watchlist2.json")
        .will_respond_with(404, body=expected)
    )

    with pact:
        client = CfgpusherClient(f"http://{PACT_MOCK_HOST}:{PACT_MOCK_PORT}")
        resp = client.get_file("opt/ns/tenant/1112/watchlist2.json")
        assert resp == expected

def test_get_file_not_exist3(pact):
    expected = {"message": "[Reason]: File /opt/ns/configshare/dp/opt/ns/tenant/1113/watchlist2.json doesn't exist."}
    (
        pact.given("Cfgpusher returns file not found")
        .upon_receiving("a get file request to Cfgpusher4")
        .with_request("get", "/file/opt/ns/tenant/1113/watchlist2.json")
        .will_respond_with(404, body=expected)
    )

    with pact:
        client = CfgpusherClient(f"http://{PACT_MOCK_HOST}:{PACT_MOCK_PORT}")
        resp = client.get_file("opt/ns/tenant/1113/watchlist2.json")
        assert resp == expected

def test_delete(pact):
    expected = {'status': 'OK'}
    (
        pact.given("Cfgpusher delete file")
        .upon_receiving("a delete file request to Cfgpusher")
        .with_request("delete", "/file/opt/ns/tenant/1113/watchlist2.json")
        .will_respond_with(200, body=expected)
    )

    with pact:
        client = CfgpusherClient(f"http://{PACT_MOCK_HOST}:{PACT_MOCK_PORT}")
        resp = client.delete_file("opt/ns/tenant/1113/watchlist2.json")
        assert resp == expected

def test_delete_not_exist(pact):
    expected = {'status': 'OK'}
    (
        pact.given("Cfgpusher delete file not found")
        .upon_receiving("a delete file request to Cfgpusher")
        .with_request("delete", "/file/opt/ns/tenant/1113/watchlist2.json")
        .will_respond_with(200, body=expected)
    )

    with pact:
        client = CfgpusherClient(f"http://{PACT_MOCK_HOST}:{PACT_MOCK_PORT}")
        resp = client.delete_file("opt/ns/tenant/1113/watchlist2.json")
        assert resp == expected
