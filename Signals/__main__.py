from flask import Flask, jsonify, g, request_finished
from flask.signals import signals_available

if not signals_available:
    raise RuntimeError("No signals available, please install Blinker using 'pip install blinker'.")



app = Flask(__name__)

def finished(sender, response, **extra):
    print("About to send a Response\n")
    print(response)

request_finished.connect(finished)

@app.route('/api')
def service():
    return jsonify({
        'Hello':'World',
    })

if __name__ == '__main__':
    app.run()