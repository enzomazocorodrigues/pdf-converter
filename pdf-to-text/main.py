from flask import Flask, redirect, render_template, request
from pypdf import PdfReader
import os

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('./upload.html')
	
@app.route('/upload', methods = ['POST'])
def upload():
   file = request.files['file']
   filename = file.filename.split('.')[0]
   text = pdf_to_text(file)
   return text

def pdf_to_text(file):
   pdf = PdfReader(file)
   text = ''
   for page in pdf.pages:
      text += page.extract_text()
   return text
		
if __name__ == '__main__':
   app.run(debug = True)