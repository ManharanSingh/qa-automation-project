



class TestUsers:

    def test_get_all_users(self, client):
        response = client.get("/users")

        response.status_code == 200
        
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 10

    def test_get_single_user(self, client):
        response = client.get("/users/1")  

        response.status_code == 200

        data = response.json()

        assert data["id"] == 1
        assert "name" in data
        assert "email" in data

    def test_user_email_format(self, client):
        response = client.get("/users/1")    
        data = response.json()

        assert "@" in data["email"]
