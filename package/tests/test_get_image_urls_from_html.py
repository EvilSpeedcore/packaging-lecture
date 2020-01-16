"""This module contains unit tests for get_image_urls_from_html() function."""
import pathlib

import pytest

from imgsaver import imgsaver


@pytest.fixture
def html_document() -> str:
    """HTML document."""
    html_file = pathlib.Path(__file__).parent / 'assets' / 'simple.html'
    with open(html_file) as f:
        content = f.read()
    return content


def test(html_document: str) -> None:
    """Tests image URLs retrieval using HTML document."""
    urls = list(imgsaver.get_image_urls_from_html(html_document))
    assert urls == ['https://example/images/girl.png', 'https://example/images/boy.png']
