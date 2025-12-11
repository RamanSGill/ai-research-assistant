import requests
import os

def download_file(url: str, save_path: str):
    """
    Downloads any file from a URL and saves it locally.
    Returns the local file path.
    """
    response = requests.get(url)

    # Write the file to disk
    with open(save_path, "wb") as f:
        f.write(response.content)

    return save_path