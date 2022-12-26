from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="secret"
        )
        cls.post = Post.objects.create(
            title="A good title", body="Nice body content", author=cls.user
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, "A good title")
        self.assertEqual(self.post.body, "Nice body content")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")

    def test_url_locations(self):
        home_page_response = self.client.get("/")
        detail_page_response = self.client.get("/post/1/")
        self.assertEqual(home_page_response.status_code, 200)
        self.assertEqual(detail_page_response.status_code, 200)

    def test_home_page(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "Django blog")

    def test_post_page(self):
        response = self.client.get(reverse("post_detail", kwargs={"pk": self.post.pk}))
        no_response = self.client.get("/post/1000000")
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(no_response.status_code, 200)
        self.assertContains(response, "A good title")
        self.assertTemplateUsed(response, "post_detail.html")
