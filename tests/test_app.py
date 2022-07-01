import unittest
import os
os.environ['TESTING'] = 'true'

from app import x

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = x.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Rashel Rojas</title>" in html
        assert "<h1>About Me</h1>" in html 
        assert "Education" in html 
        assert "Experience" in html

    def test_timeline(self):
        response=self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0
        
        response=self.client.post("/api/timeline_post",
        data= {
            'name' : 'Charlie Brown',
            'email' : 'charlie@gmail.com',
            'content' : 'content charlie'
        }
        )
        assert response.status_code == 200
        response=self.client.get("/api/timeline_post")
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 1

        response=self.client.post("/api/timeline_post",
        data= {
            'name' : 'Snoopy',
            'email' : 'snoopy@gmail.com',
            'content' : 'content snoopy'
        }
        )
        assert response.status_code == 200
        response=self.client.get("/api/timeline_post")
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 2

        response = self.client.get("/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<h1>All Timeline Posts</h1>" in html
        assert "<h1>Make a Timeline Post</h1>" in html

    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post("/api/timeline_post",data=
        {"email": "john@example.com", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        # POST request with empty 'content'
        response = self.client.post("/api/timeline_post", data=
        {"name": "John Doe", "email": "john@example.com", "content": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        # POST request with malformed email
        response =self.client.post("/api/timeline_post", data=
        {"name" : "John Doe", "email": "not-an-email", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html
