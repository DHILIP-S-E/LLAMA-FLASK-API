from fastapi import FastAPI, UploadFile, File, HTTPException
import ollama
import io

app = FastAPI()

@app.post("/extract_prescription/")
async def extract_prescription_data(
    page1: UploadFile = File(...),
    page2: UploadFile = File(...)
):
    """
    Analyzes two image files (pages of a prescription) and extracts prescription data.
    """
    try:
        # Read image content
        page1_content = await page1.read()
        page2_content = await page2.read()

        # Define the prompt for prescription data extraction
        prompt = """Analyze the text in the provided image, focusing on extracting prescription data.
Extract the patient's name, medication names, dosages, frequency, and any other relevant prescription details.
Present the extracted information in a clear, concise, and well-organized Markdown format, using headings and lists as appropriate."""

        # Call Ollama for the first page
        response1 = ollama.chat(
            model='llama3.2-vision',
            messages=[{
                'role': 'user',
                'content': prompt,
                'images': [page1_content] # Pass image content as bytes
            }]
        )
        data1 = response1['message']['content']

        # Call Ollama for the second page
        response2 = ollama.chat(
            model='llama3.2-vision',
            messages=[{
                'role': 'user',
                'content': prompt,
                'images': [page2_content] # Pass image content as bytes
            }]
        )
        data2 = response2['message']['content']

        # You might want to process or combine data1 and data2 here
        # For now, returning them separately
        return {
            "page1_data": data1,
            "page2_data": data2
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")