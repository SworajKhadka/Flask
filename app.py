from flask import Flask
## WSGI Application
app = Flask(__name__)

@app.route('/')
def welcome():
    return "wassup gang, how you doin"

if __name__ == '__main__':  # Corrected condition
    app.run(debug=True)
