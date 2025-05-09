from flask import Flask

app = Flask(__name__)

@app.route('/blocked')
def hello():
    return "This is the EC2 instance in the blocked private subnet!\n"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)  # Run on port 80 and accessible from the VPC