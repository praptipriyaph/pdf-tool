The PDF Manager is a web-based application designed to streamline the management of PDF files by providing functionalities to merge and split PDFs. Developed using Flask, a micro web framework for Python, this tool offers a user-friendly interface and efficient backend processing.

Pre-requisites:
- install PyMuPDF
- install Flask

Key Features:

- Merge PDFs:
Users can upload up to 10 PDF files to be merged into a single document.
The tool uses PyMuPDF (Fitz) to handle the merging process.
The merged PDF is automatically saved and made available for download.

- Split PDFs:
Users can upload a single PDF and specify a range of pages to extract.
The tool splits the specified range into a new PDF file using PyMuPDF.
The resulting split PDF is saved and available for download.
Technical Details:

Backend:
- The application is built with Flask, providing a robust and scalable backend.
- Python handles file operations, merging, and splitting PDFs using the PyMuPDF library.
- Uploaded files are temporarily stored in a designated 'uploads' directory for processing.

Frontend:
- HTML templates are used for rendering the web interface.
- Users interact with the tool through simple forms for merging and splitting PDFs.
  
File Handling:
- Uploaded files are saved temporarily and cleaned up after the merging or splitting process.
- The application ensures efficient handling and processing of PDF files to maintain performance and reliability.



Following is the User-Interface for the PDF Tool:
![pdf-tool](https://github.com/praptipriyaph/pdf-tool/assets/131396397/811a26bb-cf3f-4a83-80a9-4934c35ec5a0)
