def test_info_returns_the_running_version(client):
    response = client.get("/info")
    assert response.status_code == 200
    assert response.json()["version"] == "v2.6.0"
