"""This module contains functions for command line interface."""
from argparse import ArgumentParser

from imgsaver.imgsaver import download_images_from_page


def download_images() -> None:
    """Downloads images from web page."""
    parser = ArgumentParser(description='Downloads images from URL and saves them into a folder.')
    parser.add_argument('url', help='Page URL to download images from.')
    parser.add_argument('folder', default='', help='Path to an existing folder to save images to.')
    args = parser.parse_args()
    download_images_from_page(args.url, args.folder)
