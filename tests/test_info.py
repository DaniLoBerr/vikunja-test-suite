import httpx


def test_info_returns_the_running_version():
    response = httpx.get("http://localhost:8080/api/v1/info")
    assert response.status_code == 200
    assert response.json()["version"] == "v2.6.0"
