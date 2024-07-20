from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def serve_clover():
    return render_template('clover.html')

if __name__ == '__main__':
    app.run(debug=True)