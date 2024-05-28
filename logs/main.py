from flask import Flask, jsonify, request, send_file
import os

LOG_FILE = '/app/logs.txt'
LOG_TOKEN = os.environ.get('LOG_TOKEN')

app = Flask(__name__)
	
@app.route('/', methods = ['GET'])
def get_logs():
   return send_file(LOG_FILE, as_attachment=True)
   
@app.route('/', methods = ['POST'])
def save_logs():
   try:
      if request.headers.get('Authorization') != LOG_TOKEN:
         return jsonify({'error': 'Unauthorized'}), 403

      append_log(request.json) 
      return jsonify({'status': 'logged'}), 200
   except Exception as error:
      return jsonify({'error': 'Unexpected error'}), 500

def append_log(log_entry):
   with open(LOG_FILE, 'a') as file:
      file.write(str(log_entry) + '\n')
		
if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=5000)