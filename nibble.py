import os
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from collections import Counter
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# Configure retry logic
session = requests.Session()
retry_strategy = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
)
adapter = HTTPAdapter(max_retries=retry_strategy)
session.mount("http://", adapter)
session.mount("https://", adapter)

# Download directory
DOWNLOAD_DIR = "downloads"

def display_banner():
    """
    Display the ASCII art banner with some style.
    """
    banner = r"""
     ███▄    █  ██▓ ▄▄▄▄    ▄▄▄▄    ██▓    ▓█████      
     ██ ▀█   █ ▓██▒▓█████▄ ▓█████▄ ▓██▒    ▓█   ▀      
    ▓██  ▀█ ██▒▒██▒▒██▒ ▄██▒██▒ ▄██▒██░    ▒███        
    ▓██▒  ▐▌██▒░██░▒██░█▀  ▒██░█▀  ▒██░    ▒▓█  ▄      
    ▒██░   ▓██░░██░░▓█  ▀█▓░▓█  ▀█▓░██████▒░▒████▒     
    ░ ▒░   ▒ ▒ ░▓  ░▒▓███▀▒░▒▓███▀▒░ ▒░▓  ░░░ ▒░ ░     
    ░ ░░   ░ ▒░ ▒ ░▒░▒   ░ ▒░▒   ░ ░ ░ ▒  ░ ░ ░  ░     
       ░   ░ ░  ▒ ░ ░    ░  ░    ░   ░ ░      ░        
             ░  ░   ░       ░          ░  ░   ░  ░     
                         ░       ░                     

                FileSnatcher - Made by S1B34
    """
    print(banner)


def scan_website(url):
    """
    Scan a website to count files by extension, including .rar for WinRAR files.
    """
    file_counts = Counter()
    supported_extensions = [".pdf", ".exe", ".txt", ".jpg", ".png", ".mp4", ".rar"]  # Add .rar here
    try:
        response = session.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        for a_tag in soup.find_all("a", href=True):
            href = a_tag["href"]
            parsed_url = urlparse(urljoin(url, href))
            path = parsed_url.path
            extension = os.path.splitext(path)[1].lower()
            if extension in supported_extensions:  # Only count supported extensions
                file_counts[extension] += 1
    except requests.RequestException as e:
        print(f"[ERROR] Failed to scan {url}: {e}")
    return file_counts



def crawl_website_for_files(url, extensions):
    """
    Crawl a website and find links to files with the given extensions.
    """
    found_files = []
    try:
        response = session.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        for a_tag in soup.find_all("a", href=True):
            href = a_tag["href"]
            if any(href.endswith(ext) for ext in extensions):
                found_files.append(urljoin(url, href))
    except requests.RequestException as e:
        print(f"[ERROR] Failed to crawl {url}: {e}")
    return found_files


def download_file(file_url, download_dir):
    """
    Download a file and save it to the specified directory.
    """
    try:
        filename = os.path.basename(urlparse(file_url).path)
        if not filename:
            print(f"[WARNING] Skipping invalid file URL: {file_url}")
            return

        os.makedirs(download_dir, exist_ok=True)
        file_path = os.path.join(download_dir, filename)

        response = session.get(file_url, stream=True, timeout=10)
        response.raise_for_status()
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"[INFO] File downloaded: {file_path}")
    except requests.RequestException as e:
        print(f"[ERROR] Failed to download {file_url}: {e}")


def main():
    display_banner()
    print("Welcome to Nibble! Let's nibble some files off the web (legally, of course).")
    base_url = input("Enter the target URL: ").strip()

    # Validate URL
    if not urlparse(base_url).scheme:
        print("[ERROR] Invalid URL. Please include the scheme (http:// or https://).")
        return

    # Scan the website for available file types
    print("[INFO] Scanning the website for available file types...")
    file_counts = scan_website(base_url)
    if file_counts:
        print("[INFO] Found the following file types:")
        for ext, count in file_counts.items():
            print(f"  {ext}: {count}")
    else:
        print("[INFO] No files found on the website.")
        return

    # Ask the user for file types to download
    extensions = input("Enter file extensions to download (comma-separated, e.g., pdf,exe,txt): ").split(",")
    extensions = [f".{ext.strip()}" for ext in extensions]

    # Crawl the website for files
    print(f"[INFO] Searching for files with extensions: {', '.join(extensions)}...")
    found_files = crawl_website_for_files(base_url, extensions)

    # Download the found files
    print(f"[INFO] Found {len(found_files)} file(s). Starting downloads...")
    for file_url in found_files:
        download_file(file_url, DOWNLOAD_DIR)

    print("[INFO] Download process complete! Time to enjoy your snatched files. 😎")


if __name__ == "__main__":
    main()
