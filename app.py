from flask import Flask, render_template, send_file

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route('/issues')
def issues():  # put application's code here
    return render_template('Issues.html')

@app.route('/Ziele')
def ziele():  # put application's code here
    return render_template('ziele.html')


@app.route('/download-pdf')
def download_pdf():
    # Specify the path to the PDF file
    file_path = './static/pdf/Willkommenspaket_4.pdf'

    # Send the file to the client as an HTTP response
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run()
