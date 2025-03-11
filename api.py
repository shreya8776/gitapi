
from flask import Flask, jsonify
from asgiref.wsgi import WsgiToAsgi
app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_api():
    return jsonify({'message': 'Hello, World FlaskApi!'})

asgi_app = WsgiToAsgi(app)

if __name__ == '__main__':
    app.run(debug=True)



