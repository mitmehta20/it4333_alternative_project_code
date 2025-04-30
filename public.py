import os
from flask import Flask
import requests

app = Flask(__name__)

@app.route('/unblocked')
def hello():
    return "This is the EC2 instance in the unblocked public subnet!"

@app.route('/private-test')
def privateTest():
    privateIp = os.environ.get('PRIVATE_EC2_IP')
    try:
        response = requests.get(f"http://{privateIp}:80/blocked", timeout=5)
        return f"Success contacting private EC2: {response.text}\n"
    except Exception as e:
        return f"Failed to contact private EC2: {e}\n"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)  # Run on port 80 and accessible from the VPC  PRIVATE_EC2_IP
