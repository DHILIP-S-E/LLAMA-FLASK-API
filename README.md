# FastAPI Image Analysis API

This project provides a simple API using FastAPI to analyze text within images using the `llama3.2-vision` model from Ollama.

## Prerequisites

*   Python 3.7+
*   pip (Python package installer)
*   Ollama installed and running.
*   The `llama3.2-vision` model pulled in Ollama. This model is required for image analysis. If you haven't pulled it yet, run the following command:
    ```bash
    ollama pull llama3.2-vision
    ```

## Installation

1.  Clone this repository (if applicable) or ensure you have the `api.py` file.
2.  Navigate to the project directory in your terminal.
3.  Install the required Python packages:
    ```bash
    pip install fastapi uvicorn python-multipart ollama base64
    ```

## Running the API

To start the FastAPI application, run the following command from the project directory:

```bash
uvicorn api:app --reload --port 7000
```

*   `api:app`: Refers to the `app` object inside the `api.py` file.
*   `--reload`: Restarts the server automatically when code changes are detected.
*   `--port 7000`: Specifies that the server should run on port 7000.

The API will be accessible at `http://127.0.0.1:7000`.

## API Documentation

Once the server is running, you can access the automatically generated interactive API documentation (Swagger UI) at:

[http://127.0.0.1:7000/docs](http://127.0.0.1:7000/docs)

Here you can test the `/ai/ovr` endpoint by uploading an image file.

## Endpoint

*   **POST `/ai/ovr`**: Analyzes text in an uploaded image.
    *   **Request Body**: `file` (type: `UploadFile`) - The image file to analyze.
    *   **Response**: JSON containing the text analysis result from the Ollama model.