# shop/tests/test_urls.py
import pytest
from django.urls import reverse, resolve
from shop import views

@pytest.mark.django_db
def test_home_page_url():
    assert reverse('shop:home_page') == '/'
    assert resolve('/').view_name == 'shop:home_page'

@pytest.mark.django_db
def test_product_detail_url():
    url = reverse('shop:product_detail', args=['sample-slug'])
    assert url == '/sample-slug'
    assert resolve('/sample-slug').view_name == 'shop:product_detail'

@pytest.mark.django_db
def test_add_to_favorites_url():
    url = reverse('shop:add_to_favorites', args=[1])
    assert url == '/add/favorites/1/'
    assert resolve('/add/favorites/1/').view_name == 'shop:add_to_favorites'

@pytest.mark.django_db
def test_remove_from_favorites_url():
    url = reverse('shop:remove_from_favorites', args=[1])
    assert url == '/remove/favorites/1/'
    assert resolve('/remove/favorites/1/').view_name == 'shop:remove_from_favorites'

@pytest.mark.django_db
def test_favorites_url():
    assert reverse('shop:favorites') == '/favorites/'
    assert resolve('/favorites/').view_name == 'shop:favorites'

@pytest.mark.django_db
def test_search_url():
    assert reverse('shop:search') == '/search/'
    assert resolve('/search/').view_name == 'shop:search'

@pytest.mark.django_db
def test_filter_by_category_url():
    url = reverse('shop:filter_by_category', args=['sample-slug'])
    assert url == '/filter/sample-slug/'
    assert resolve('/filter/sample-slug/').view_name == 'shop:filter_by_category'

@pytest.mark.django_db
def test_about_url():
    assert reverse('shop:about') == '/about/'
    assert resolve('/about/').view_name == 'shop:about'
