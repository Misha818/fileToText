ArabicOCR – Project Description
Overview

ArabicOCR is a simple, user-friendly web application that allows users to upload PDFs or images containing Arabic text and instantly extract the text using OCR (Optical Character Recognition).
The system will support two OCR engines:

Qari-OCR (Python library, runs locally on the server)

Mistral OCR (external or local integration)

Users can then translate the extracted Arabic text, transliterate it into Latin script, and download the results.

Frontend

Technology stack: Pure HTML, CSS, and JavaScript (no frontend frameworks).

Features:

Upload PDF, JPG/JPEG, and PNG files via a simple drag-and-drop or file picker.

Option to select the OCR engine (Qari-OCR or Mistral OCR) before processing.

Display the extracted Arabic text in a text area for preview and editing.

Buttons for:

Translate (Arabic → English or other selected language via GPT-4o, Gemini 1.5 Pro, etc.).

Transliterate Arabic text into Latin script.

Download the result as a .docx file containing:

Original Arabic text

Translation

Transliteration

Backend

Technology stack: Python (Flask).

Endpoints:

/upload – Receives the uploaded file, runs the selected OCR engine, returns extracted text.

/translate – Receives Arabic text, calls the translation API (GPT-4o, Gemini, etc.), returns translated text.

/transliterate – Converts Arabic text to Latin script.

/download – Generates and returns a .docx file with all outputs.

Processing Flow:

Receive file from frontend.

Run OCR using the selected engine.

Return extracted Arabic text to frontend.

If requested, run translation or transliteration.

On request, generate .docx containing:

Original Arabic text

Translation

Transliteration.