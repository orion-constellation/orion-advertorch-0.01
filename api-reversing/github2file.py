""" Extracting Github Documentation for the target for OSINT and other reconnaisance """

import sys
import re
import os
from git import Repo
from urllib.parse import urlparse

def clone_repo(repo_url, dest_dir):
    try:
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        Repo.clone_from(repo_url, dest_dir)
        print(f"Repository cloned to {dest_dir}")
    except Exception as e:
        print(f"Error: {e}")

# Read documentation text file
def read_documentation(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    

# Parse Documentation
def parse_documentation(doc_text):
    api_info = {}
    
    # Extract base URL
    base_url_match = re.search(r"Base URL:\s*(https?://[^\s]+)", doc_text)
    if base_url_match:
        api_info["base_url"] = base_url_match.group(1)
    
    # Extract endpoints
    endpoint_matches = re.findall(r"Endpoint:\s*([^\s]+)\s*\nMethod:\s*([A-Z]+)\s*\nParameters:\s*([^\n]+)", doc_text)
    endpoints = {}
    for endpoint, method, params in endpoint_matches:
        endpoints[endpoint] = {
            "method": method,
            "parameters": params.split(", ")
        }
    api_info["endpoints"] = endpoints
    
    # Extract other relevant information (e.g., authentication)
    auth_match = re.search(r"Authentication:\s*(.+)", doc_text)
    if auth_match:
        api_info["authentication"] = auth_match.group(1)
    
    return api_info






def main():
    if len(sys.argv) != 2:
        print("Usage: python github2file.py <repository-url>")
        sys.exit(1)

    repo_url = sys.argv[1]
    parsed_url = urlparse(repo_url)
    repo_name = os.path.splitext(os.path.basename(parsed_url.path))[0]
    dest_dir = os.path.join(os.getcwd(), repo_name)

    clone_repo(repo_url, dest_dir)

if __name__ == "__main__":
    main()

