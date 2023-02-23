from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Hiya Liam.  You have just accessed the Company's newest   website in the Cloud. Cool eh?"

if __name__=="__main__":
  app.run(host='0.0.0.0', debug=True)
