"""Ths module contains ..."""
import concurrent.futures
import functools
import logging
import pathlib
from typing import Generator
from urllib.parse import urlparse

from bs4 import BeautifulSoup
import requests


logger = logging.getLogger(__name__)


def get_page_content(url: str) -> str:
    """Gets content of page."""
    response = requests.get(url)
    content = response.text
    return content


def get_image_name_from_url(url: str) -> str:
    """Gets image name from image URL."""
    url_components = urlparse(url)
    image_path = pathlib.Path(url_components.path)
    image_name = image_path.name
    if not image_path.suffix:
        image_name = f'{image_name}.jpg'
    return image_name


def get_image_urls_from_html(text: str) -> Generator:
    """Gets image URLs from HTML document."""
    soup = BeautifulSoup(text, 'html.parser')
    for image in soup.find_all('img'):
        image_url = image.get('src')
        components = urlparse(image_url)
        if components.scheme and components.netloc:  # Trying to validate URL.
            yield image_url


def download_image(url: str, folder: str) -> None:
    """Downloads image from URL to a folder."""
    image_name = get_image_name_from_url(url)
    image_absolute_path = pathlib.Path(folder) / image_name
    response = requests.get(url, stream=True)
    status_message = '[{}] {}'
    if response.status_code == 200:
        with open(image_absolute_path, 'wb') as f:
            f.write(response.content)
        logger.info(status_message.format('V', url))
    else:
        logger.info(status_message.format('X', url))


def download_images_from_page(url: str, folder: str) -> None:
    """Downloads images from web page."""
    content = get_page_content(url)
    urls = get_image_urls_from_html(content)
    func = functools.partial(download_image, folder=folder)
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(func, list(urls))
