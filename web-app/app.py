from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    app.logger.info("Home page accessed")
    return "<h1>Welcome to My Simple Web App</h1><p>This is the home page.</p>"

@app.route('/api/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'World')
    app.logger.info(f"Greet endpoint accessed with name: {name}")
    return jsonify(message=f"Hello, {name}!")

@app.route('/api/info')
def info():
    app.logger.info("Info endpoint accessed")
    return jsonify(
        status="success",
        data="This is a simple web app to demonstrate Kubernetes and Splunk integration."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
