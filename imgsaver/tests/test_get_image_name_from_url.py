"""This module contains unit tests for get_image_name_from_url() function."""
from imgsaver import imgsaver


def test_url_with_suffix_with_query():
    """Tests function using image URL with suffix and query."""
    url = r'https://i0.wp.com/stackexchange.com/users/flair/4.png?resize=208%2C58&ssl=1'
    image_name = imgsaver.get_image_name_from_url(url)
    assert image_name == '4.png'


def test_url_with_suffix_without_query():
    """Tests function using image URL with suffix and without query."""
    url = r'https://i0.wp.com/www.joelonsoftware.com/wp-content/uploads/2016/12/fc-logo.png?w=730&ssl=1'
    image_name = imgsaver.get_image_name_from_url(url)
    assert image_name == 'fc-logo.png'


def test_url_without_suffix_with_query():
    """Tests function using image URL without suffix and with query."""
    url = r'https://secure.gravatar.com/avatar/d95216e70bed7430716b91ddd6df55fe?s=64&d=mm&r=pg'
    image_name = imgsaver.get_image_name_from_url(url)
    assert image_name == 'd95216e70bed7430716b91ddd6df55fe.jpg'
