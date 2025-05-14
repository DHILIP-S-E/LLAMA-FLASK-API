import ollama
from fastapi import FastAPI, File, UploadFile, HTTPException
import base64

app = FastAPI()

@app.post("/ai/ocr")
async def analyze_image(file: UploadFile = File(...)):
    """
    Analyzes text in an uploaded image using Ollama's llama3.2-vision model.
    """
    try:
        # Read the image file content
        image_content = await file.read()

        # Ollama expects image data as base64 encoded string
        image_base64 = base64.b64encode(image_content).decode('utf-8')

        # Make sure the model 'llama3.2-vision' is available in your Ollama setup.
        # You might need to run `ollama pull llama3.2-vision` or the correct tag for it.
        response = ollama.chat(
            model='llama3.2-vision',
            messages=[{
                'role': 'user',
                'content': """Analyze the text in the provided image.
Extract all readable content and present it in a structured Markdown format that is clear, concise, and well-organized. Ensure proper formatting (e.g., headings, lists, or code blocks) as necessary to represent the content effectively.""",
                'images': [image_base64]  # Pass the base64 encoded image data
            }]
        )

        # Accessing the response content
        return {"analysis": response['message']['content']}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")