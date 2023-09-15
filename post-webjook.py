from flask import Flask, request, abort
import sys
import time

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    print( "Insode /webhook endpoint", end=' ', flush=True )
    sys.stdout.flush()
    time.sleep(.2)  # or other time-consuming work        
    if request.method == 'POST':
        sys.stdout.write('SUCCESS. 200 response will be sent')
        sys.stdout.flush()
        time.sleep(.2)  # or other time-consuming work        
        data = request.json
        sys.stdout.write(str(data))
        sys.stdout.flush()
        time.sleep(.2)  # or other time-consuming work        
        return request.json, 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
