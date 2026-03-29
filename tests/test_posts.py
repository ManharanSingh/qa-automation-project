


class TestPosts:

    def test_get_all_posts(self, client):
        response = client.get("/posts")

        assert response.status_code == 200
        
        data = response.json()
        
        assert isinstance(data, list)
        assert len(data) == 100

    def test_get_single_post(self, client):
        response = client.get("/posts/1")

        assert response.status_code == 200

        data = response.json()

        assert data["id"] == 1
        assert "title" in data
        assert "body" in data
        assert "userId" in data  

    def test_create_post(self, client):

        payload = {
            "title":"API testing project",
            "body":"this post created by Manu",
            "userId":1
        } 

        response = client.post("/posts", payload)  

        response.status_code == 201
        data = response.json()

        assert data["title"] == payload["title"]
        assert data["body"] == payload["body"]
        assert "id" in data
    
    def test_update_post(self, client):
        payload = {
            "id":1,
            "title":"Updated Title",
            "body":"Updated body content",
            "userId":1
        }

        response = client.put("/posts/1", payload)
        response.status_code == 200
        data = response.json()
        assert data["title"] == "Updated Title"

    def test_delete_post(self, client):
        response = client.delete("/posts/1")

        response.status_code == 200
        
