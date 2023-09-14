from flask import Flask, request, abort

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print('SUCCESS. 200 response will be sent')
        print(request.json)
        return request.json, 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
