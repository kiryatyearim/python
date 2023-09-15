from flask import Flask, request, abort
import sys
import time

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    print( "Insode /webhook endpoint", end=' ', flush=True )
    sys.stdout.flush()
    if request.method == 'POST':
        sys.stdout.write('SUCCESS. 200 response will be sent')
        sys.stdout.flush()
        data = request.json
        sys.stdout.write(str(data))
        sys.stdout.flush()
        return request.json, 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
