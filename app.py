from flaskk import Flask
 
app = Flask(__name__)
 
@app.route("/helloWorld", methods=["GET"])
def helloWorld():
    return 'Hello World!'
 
app.run(host="0.0.0.0", port=80, debug=True)
