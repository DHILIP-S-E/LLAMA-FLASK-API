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
            'content': """Analyze the text in the provided image, focusing on extracting prescription data.
Extract the patient's name, medication names, dosages, frequency, and any other relevant prescription details.
Present the extracted information in a clear, concise, and well-organized Markdown format, using headings and lists as appropriate.""",
            'images': [image_path]  # Pass the path string in a list
        }]
    )
    # Accessing the response content:
    # The ollama library typically returns a dictionary-like object.
    # The standard way to access the message content is:
    print(response['message']['content'])

except FileNotFoundError:
    print(f"Error: The image file was not found at '{image_path}'. Please check the path.")
except Exception as e:
    print(f"An error occurred: {e}")