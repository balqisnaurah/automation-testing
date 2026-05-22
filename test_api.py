"""
Automation testing untuk JSONPlaceholder API menggunakan pytest.
Menguji endpoint CRUD dan komentar.
"""

import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"


class TestGetUsers:
    """Test suite untuk endpoint GET users."""

    def test_get_list_users_returns_200(self):
        response = requests.get(f"{BASE_URL}/users")
        assert response.status_code == 200

    def test_get_list_users_returns_10_users(self):
        response = requests.get(f"{BASE_URL}/users")
        data = response.json()
        assert len(data) == 10

    def test_get_single_user_returns_correct_id(self):
        response = requests.get(f"{BASE_URL}/users/1")
        data = response.json()
        assert response.status_code == 200
        assert data["id"] == 1

    def test_get_user_not_found_returns_404(self):
        response = requests.get(f"{BASE_URL}/users/999")
        assert response.status_code == 404

    def test_user_has_required_fields(self):
        response = requests.get(f"{BASE_URL}/users/1")
        user = response.json()
        required_fields = ["id", "name", "email", "username", "address"]
        for field in required_fields:
            assert field in user, f"Field '{field}' tidak ditemukan"


class TestCreateUser:
    """Test suite untuk endpoint POST users."""

    def test_create_user_returns_201(self):
        payload = {"name": "Balqis", "email": "balqis@test.com"}
        response = requests.post(f"{BASE_URL}/users", json=payload)
        assert response.status_code == 201

    def test_create_user_returns_correct_data(self):
        payload = {"name": "Balqis", "email": "balqis@test.com"}
        response = requests.post(f"{BASE_URL}/users", json=payload)
        data = response.json()
        assert data["name"] == "Balqis"
        assert data["email"] == "balqis@test.com"
        assert "id" in data


class TestUpdateUser:
    """Test suite untuk endpoint PUT users."""

    def test_update_user_returns_200(self):
        payload = {"name": "Updated Name", "email": "updated@test.com"}
        response = requests.put(f"{BASE_URL}/users/1", json=payload)
        assert response.status_code == 200

    def test_update_user_returns_updated_data(self):
        payload = {"name": "Updated Name", "email": "updated@test.com"}
        response = requests.put(f"{BASE_URL}/users/1", json=payload)
        data = response.json()
        assert data["name"] == "Updated Name"


class TestDeleteUser:
    """Test suite untuk endpoint DELETE users."""

    def test_delete_user_returns_200(self):
        response = requests.delete(f"{BASE_URL}/users/1")
        assert response.status_code == 200


class TestPosts:
    """Test suite untuk endpoint posts dan comments."""

    def test_get_all_posts_returns_200(self):
        response = requests.get(f"{BASE_URL}/posts")
        assert response.status_code == 200

    def test_get_all_posts_returns_100(self):
        response = requests.get(f"{BASE_URL}/posts")
        data = response.json()
        assert len(data) == 100

    def test_each_post_has_title_and_body(self):
        response = requests.get(f"{BASE_URL}/posts")
        for post in response.json():
            assert "title" in post
            assert "body" in post

    def test_get_comments_by_post(self):
        response = requests.get(f"{BASE_URL}/posts/1/comments")
        assert response.status_code == 200
        for comment in response.json():
            assert comment["postId"] == 1