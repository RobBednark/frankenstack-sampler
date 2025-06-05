from flask import Flask

app = Flask(__name__)

@app.route('/frank-api-main/')
def frank_api_main():
    return 'frank-api-main: success response'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)