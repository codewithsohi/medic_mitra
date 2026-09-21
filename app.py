from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = "medicmitra-ui-testing"

@app.route('/')
def index():
    return render_template('landing.html')

@app.route('/login', methods=['POST'])
@app.route('/signup', methods=['POST'])
def auth():
    # Bypassing database authentication for UI testing
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    # In the future, this route will handle image validation, preprocessing, and model inference
    return redirect(url_for('results'))

@app.route('/results')
def results():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True)