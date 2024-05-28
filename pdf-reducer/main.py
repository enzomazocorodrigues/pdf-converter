import os
import subprocess
import requests
from flask import Flask, redirect, render_template, request, send_file

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
      resolution = request.form.get('resolution')
      if file.filename == '':
         raise Exception('Nenhum arquivo informado.')
      filename, extension = file.filename.split('.')
      if not extension == 'pdf':
         raise Exception('Arquivo deve ser .pdf.')
      if not extension == 'pdf':
         raise Exception('Arquivo deve ser .pdf.')
      if not resolution:
         raise Exception('Nunhuma resolução informada.')

      resolution_key = get_resolution_key(resolution)
      input_path = os.path.join('/tmp', file.filename)
      output_path = os.path.join('/tmp', f'{resolution}_{filename}.pdf')
      file.save(input_path)

      gs_command = [
         'gs',
         '-sDEVICE=pdfwrite',
         '-dCompatibilityLevel=1.4',
         f'-dPDFSETTINGS={resolution_key}',
         '-dNOPAUSE',
         '-dBATCH',
         f'-sOutputFile={output_path}',
         input_path
      ]

      subprocess.run(gs_command, check=True)

      log_entry = {
         'service': 'pdf-reducer',
         'filename': file.filename,
         'resolution': resolution,
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

def get_resolution_key(resolution):
   try:
      resolutions = {
         'screen': '/screen',
         'ebook': '/ebook',
         'printer': '/printer',
         'prepress': '/prepress',
         'default': '/default'
      }
      return resolutions[resolution]
   except KeyError:
      raise Exception('Resolução informada inválida.')

def log(log_entry):
   headers = {
      'Authorization': LOG_TOKEN
   }
   requests.post(LOG_SERVICE_URL, json=log_entry, headers=headers)

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=5000)