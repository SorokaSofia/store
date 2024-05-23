# orders/tests/test_models.py
import pytest
from django.contrib.auth import get_user_model
from orders.models import Order

User = get_user_model()

@pytest.mark.django_db
def test_create_order():
    user = User.objects.create_user(email='testuser@example.com', password='testpassword', full_name='Test User')
    order = Order.objects.create(user=user, status=True)
    assert order.user == user
    assert order.status is True
    assert order.items.count() == 0
