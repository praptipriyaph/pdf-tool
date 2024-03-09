from flask import Flask, render_template, request, send_file
import os
import fitz

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/merge', methods=['POST'])
def merge():
    merged_pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], 'merged.pdf')

    # Create a list to store the paths of uploaded files
    uploaded_files = []

    # Iterate over the uploaded files and save them
    for i in range(1, 11):  # Assuming a maximum of 10 files, adjust as needed
        file_key = f'file{i}'
        if file_key in request.files:
            uploaded_file = request.files[file_key]
            uploaded_file_path = os.path.join(app.config['UPLOAD_FOLDER'], f'file{i}.pdf')
            uploaded_file.save(uploaded_file_path)
            uploaded_files.append(uploaded_file_path)

    # Merging using PyMuPDF
    with open(merged_pdf_path, 'wb') as output_file:
        pdf_merger = fitz.open()

        # Insert each uploaded file into the merger
        for file_path in uploaded_files:
            pdf_merger.insert_pdf(fitz.open(file_path))

        pdf_merger.save(output_file, garbage=4, deflate=True)

    # Clean up temporary files
    for file_path in uploaded_files:
        os.remove(file_path)

    return send_file(merged_pdf_path, as_attachment=True)

@app.route('/split', methods=['POST'])
def split():
    file = request.files['file']
    pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], 'input.pdf')

    file.save(pdf_path)

    start_page = int(request.form['start_page'])
    end_page = int(request.form['end_page'])

    pdf_document = fitz.open(pdf_path)
    pdf_writer = fitz.open()

    for page_num in range(start_page - 1, end_page):
        pdf_writer.insert_pdf(pdf_document, from_page=page_num, to_page=page_num)

    output_path = os.path.join(app.config['UPLOAD_FOLDER'], f'split_{start_page}_{end_page}.pdf')
    pdf_writer.save(output_path)

    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
