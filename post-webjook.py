from flask import Flask, request, abort
import sys

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print('SUCCESS. 200 response will be sent', file=sys.stdout)
        print(request.json, file=sys.stdout)
        return request.json, 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
