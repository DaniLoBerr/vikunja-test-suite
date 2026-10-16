def test_user_returns_logged_in_username(client, token):
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/user", headers=headers)
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"
