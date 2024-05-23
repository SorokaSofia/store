# accounts/tests/test_views.py
import pytest
from django.urls import reverse
from django.test import Client

@pytest.mark.django_db
def test_user_login_view_get():
    client = Client()
    url = reverse('accounts:user_login')
    response = client.get(url)
    assert response.status_code == 200
    assert 'accounts/login.html' in [t.name for t in response.templates]
