import os
import requests
from flask import Flask, flash, redirect, render_template, request, send_file
from pypdf import PdfReader

LOG_SERVICE_URL = os.environ.get('LOG_SERVICE_URL')
LOG_TOKEN = os.environ.get('LOG_TOKEN')

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('./upload.html')
	
@app.route('/upload', methods = ['POST'])
def upload():
   try:
      if 'file' not in request.files:
         raise Exception('Nenhum arquivo informado.')
      file = request.files['file']
      if file.filename == '':
         raise Exception('Nenhum arquivo informado.')
      filename, extension = file.filename.split('.')
      if not extension == 'pdf':
         raise Exception('Arquivo deve ser .pdf.')
      
      output_path = os.path.join('/tmp', filename + '.txt')
      text = pdf_to_text(file)
      create_file(output_path, text)

      log_entry = {
         'service': 'pdf-to-text',
         'filename': file.filename,
         'status': 200
      }
      log(log_entry)
      return send_file(output_path, as_attachment=True)
   except Exception as error:
      print(str(error), flush=True)
      log_entry = {
         'service': 'pdf-to-text',
         'error': str(error),
         'status': 500
      }
      log(log_entry)
      return redirect('/')

def pdf_to_text(file):
   pdf = PdfReader(file)
   text = ''
   for page in pdf.pages:
      text += page.extract_text()
   return text

def create_file(name, content):
   with open(name, 'w') as file:
      file.write(content)

def log(log_entry):
   headers = {
      'Authorization': LOG_TOKEN
   }
   requests.post(LOG_SERVICE_URL, json=log_entry, headers=headers)
		
if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=5000)