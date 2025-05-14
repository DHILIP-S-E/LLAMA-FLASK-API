import ollama

# Ensure 'image_path' is a string variable holding the correct path to your image.
# For example:
image_path = "1.jpg"  # <--- !!! REPLACE THIS WITH THE ACTUAL PATH TO YOUR IMAGE !!!

# Make sure the model 'llama3.2-vision' is available in your Ollama setup.
# You might need to run `ollama pull llama3.2-vision` or the correct tag for it.
try:
    response = ollama.chat(
        model='llama3.2-vision',
        messages=[{
            'role': 'user',
            'content': """Analyze the text in the provided image.
Extract all readable content and present it in a structured Markdown format that is clear, concise, and well-organized. Ensure proper formatting (e.g., headings, lists, or code blocks) as necessary to represent the content effectively.""",
            'images': [image_path]  # Pass the path string in a list
        }]
    )
    # Accessing the response content:
    # The ollama library typically returns a dictionary-like object.
    # The standard way to access the message content is:
    print(response['message']['content'])

    # Your f:\mediai\app.py uses response.message.content.
    # If that works for you, it means your ollama response object might support attribute access.
    # However, response['message']['content'] is generally more robust for TypedDicts.

except FileNotFoundError:
    print(f"Error: The image file was not found at '{image_path}'. Please check the path.")
except Exception as e:
    print(f"An error occurred: {e}")

