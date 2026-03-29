



class TestNegativeCases:

    def test_get_nonexistent_post(self, client):
        response = client.get("/posts/99999")

        assert response.status_code == 404

    def test_get_nonexistent_user(self, client):
        response = client.get("/users/99999")  

        assert response.status_code == 404

    def test_response_time_is_acceptable(self, client):
        response = client.get("/posts")

        assert response.elapsed.total_seconds() < 3.0      
        
