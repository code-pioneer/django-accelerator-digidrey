from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from home.models import Contactus
from django.utils import timezone

"""
Run testcases: ./manage.py test
"""

# Test Homepage
class Home_View_TestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_view(self):
        response = self.client.post("/", {})
        self.assertContains(response, "taralnest.com &copy; 2019")
        self.assertContains(response, "taralnest.min.css")
        self.assertContains(response, "bootstrap.bundle.min.js")
        self.assertNotContains(response, "step1.md")

# Test Getting Started
class GettingStarted_View_TestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_view1(self):
        response = self.client.post("/docs/", {})
        self.assertContains(response, "taralnest.com &copy; 2019")
        self.assertContains(response, "Get Started")
        self.assertContains(response, "step1.md")
        self.assertNotContains(response, "Theme Documentation")

    def test_view2(self):
        response = self.client.post("/docs/step6.md", {})
        self.assertContains(response, "taralnest.com &copy; 2019")
        self.assertContains(response, "Get Started")
        self.assertContains(response, "Deploy Django on GCP Cloud Run")
        self.assertNotContains(response, "Create POSTGRESQL database on local workstation")

# Test Theme
class Theme_View_TestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_view1(self):
        response = self.client.post("/theme/", {})
        self.assertContains(response, "taralnest.com &copy; 2019")
        self.assertContains(response, "Theme Documentation")
        self.assertContains(response, "Illustrations")
        self.assertNotContains(response, "step2.md")

    def test_get_view2(self):
        response = self.client.get("/theme/card", {})
        self.assertContains(response, "taralnest.com &copy; 2019")
        self.assertContains(response, "Theme Documentation")
        self.assertContains(response, "Gradient State Card")
        self.assertNotContains(response, "step2.md")


# Test ContactUs model
class Contactus_Model_TestCase(TestCase):
    def setUp(self):
        Contactus.objects.create(user="testcase_user", feedback="model feedback input", tm=timezone.now())

    def test_model(self):
        obj = Contactus.objects.get(user="testcase_user")
        self.assertEqual(obj.feedback, "model feedback input")

# Test ContactUs view
class Contactus_View_TestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client = Client()
        self.client.force_login(self.user)

    def test_view(self):
        self.client.force_login(self.user)
        response = self.client.post("/contactus/save", {"feedback": "form feedback input"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "form feedback input")
        self.assertNotContains(response, "abcdefghijklmnopqrstuvwxyz")


# Test static pages (About Us and Disclaimer)
class Static_Views_TestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_view_aboutus(self):
        response = self.client.post("/aboutus/", {})
        self.assertContains(response, "taralnest.com &copy; 2019")
        self.assertContains(response, "👋 Hello 👋")
        self.assertNotContains(response, "step2.md")

    def test_get_view_disclaimer(self):
        response = self.client.get("/disclaimer/", {})
        self.assertContains(response, "taralnest.com &copy; 2019")
        self.assertContains(response, "By using our website, you hereby consent ")
        self.assertNotContains(response, "step2.md")