import os
from flask import Flask, send_from_directory, request

FILE_FOLDER = 'files'
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! I am alive :)"
    

@app.route('/download', methods=['GET', 'POST'])
def downloadFile ():
    full_path = os.path.join(app.root_path, FILE_FOLDER)
    passed_name = request.args.get('file')
    if passed_name is None:
        filename = 'default.png'
    else:
        filename = passed_name
    return send_from_directory(full_path, filename, as_attachment=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True) 