from flask import Flask, redirect, render_template, request
import os
import subprocess

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

      input_path = os.path.join("/tmp", file.filename)
      output_path = os.path.join("/tmp", "reduced_" + file.filename)
      file.save(input_path)

      gs_command = [
         "gs",
         "-sDEVICE=pdfwrite",
         "-dCompatibilityLevel=1.4",
         f"-dPDFSETTINGS={resolution}",
         "-dNOPAUSE",
         "-dBATCH",
         f"-sOutputFile={output_path}",
         input_path
      ]

      subprocess.run(gs_command, check=True)
      return send_file(output_path, as_attachment=True)
   except Exception as error:
      print(str(error))
      return redirect('/')

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=5000)