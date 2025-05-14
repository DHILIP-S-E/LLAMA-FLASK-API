import requests
import os

# Define the API endpoint URL
api_url = "http://127.0.0.1:7000/ai/ocr"

# Define the path to the image file
# Ensure '1.jpg' exists in the same directory as this script, or provide the full path.
image_path = "1.jpg"

# Check if the image file exists
if not os.path.exists(image_path):
    print(f"Error: Image file not found at '{image_path}'")
    print("Please ensure '1.jpg' is in the correct location or update the 'image_path' variable.")
else:
    # Prepare the file for the POST request
    # 'file' is the expected form-data field name by the FastAPI endpoint
    files = {'file': open(image_path, 'rb')}

    try:
        # Send the POST request to the API
        print(f"Sending image '{image_path}' to {api_url}...")
        response = requests.post(api_url, files=files)

        # Check if the request was successful
        response.raise_for_status()

        # Print the JSON response from the API
        print("API Response:")
        print(response.json())

    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Close the file after sending
        files['file'].close()