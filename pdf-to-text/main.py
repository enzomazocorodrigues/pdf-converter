from flask import Flask, flash, redirect, render_template, request
from pypdf import PdfReader
import os

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
         raise Exception("Arquivo deve ser .pdf") 
      text = pdf_to_text(file)
      return text
   except Exception as error:
      return redirect('/')


def pdf_to_text(file):
   pdf = PdfReader(file)
   text = ''
   for page in pdf.pages:
      text += page.extract_text()
   return text
		
if __name__ == '__main__':
   app.run(debug = True)