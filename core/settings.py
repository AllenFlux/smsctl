import json
import os

# Define the configuration file path
home_dir = os.path.expanduser("~")  # Get the home directory
config_file = os.path.join(home_dir, ".smscli.json")  # Configuration file path

# Default URL in case the configuration file doesn't exist
default_url = "https://api.smscli.net"

# Load configuration or set default URL
try:
    if os.path.exists(config_file):  # Check if the configuration file exists
        with open(config_file, "r") as file:
            config_data = json.load(file)  # Load JSON data from the file
            url_prefix = config_data.get("url", default_url)  # Extract URL or use default
    else:
        url_prefix = default_url  # Use default URL if file doesn't exist
except (json.JSONDecodeError, IOError) as e:  # Handle JSON decoding or file I/O errors
    print(f"Warning: Failed to load configuration file: {e}")
    url_prefix = default_url  # Fallback to the default URL

# Output the URL prefix (for debugging or logging purposes)
print(f"Using API URL: {url_prefix}")