from flask import Flask

app= Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!" 
 
@app.route("/estudiante")
def hello2():
    return "Public salio de closet tmr" 
