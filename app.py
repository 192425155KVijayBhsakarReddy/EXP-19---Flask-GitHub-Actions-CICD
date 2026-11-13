from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "app": "Flask CI/CD Microservice",
        "status": "healthy",
        "version": "2.0.0 (Automated CI/CD Live)",
        "pipeline": "GitHub Actions Automated CI/CD"
    })

@app.route('/api/status')
def status():
    return jsonify({
        "environment": "Production",
        "testing": "Pytest Automated Suite Passed",
        "uptime": "99.9%"
    })

@app.route('/health')
def health():
    return jsonify({"health": "ok"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

