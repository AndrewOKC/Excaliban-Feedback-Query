#!/usr/bin/env python3
import csv
import urllib.request
import json
import ssl
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration
# Yes... You'll find an old version of the actual API Key in commit history ;)... 
# Call me out on this... I dare you...
API_URL = os.getenv("API_URL")
API_KEY = os.getenv("FEEDBACK_API_KEY")
CSV_FILE = "feedback_data.csv"
MAX_RESULTS = 20

def fetch_feedback():
    """Fetch feedback from the API and save to CSV file."""
    
    try:
        # Make API request with authentication
        headers = {"X-API-Key": API_KEY}
        
        # Create a URL with parameters
        full_url = f"{API_URL}?limit={MAX_RESULTS}"
        
        print(f"Fetching up to {MAX_RESULTS} feedback items...")
        
        # Create a custom request with headers
        req = urllib.request.Request(full_url, headers=headers)
        
        # Ignore SSL certificate verification if needed
        context = ssl._create_unverified_context()
        
        # Make the request
        with urllib.request.urlopen(req, context=context) as response:
            # Read and decode the response
            response_data = response.read().decode('utf-8')
            data = json.loads(response_data)
        
        # Handle different response formats
        # Adjust this based on your actual API response structure
        if isinstance(data, dict) and "items" in data:
            # If API returns a paginated response like {"items": [...], "total": 42}
            feedback_items = data["items"]
        elif isinstance(data, list):
            # If API returns a direct list of items
            feedback_items = data
        else:
            print(f"Error: Unexpected API response format: {type(data)}")
            return False
        
        # Write to CSV file
        with open(CSV_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            
            # Write header row based on the feedback schema
            writer.writerow(["ID", "Message", "App Version", "Browser", "Created At", "Status"])
            
            # Write data rows
            for item in feedback_items:
                writer.writerow([
                    item.get("id", ""),
                    item.get("message", ""),
                    item.get("appVersion", ""),
                    item.get("browser", ""),
                    item.get("createdAt", ""),
                    item.get("status", "")
                ])
        
        print(f"Successfully saved {len(feedback_items)} feedback items to {CSV_FILE}")
        return True
        
    except urllib.error.URLError as e:
        print(f"Error: Failed to fetch feedback from API: {e}")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    fetch_feedback()