from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Serve the HTML page
@app.route('/')
def home():
    return render_template('vehicle_map.html')  # This must be placed in a 'templates' folder

# Example route to receive movement updates
@app.route('/move', methods=['POST'])
def move():
    data = request.json
    direction = data.get("direction")
    print(f"Moving {direction}")
    return jsonify({"status": "ok", "direction": direction})

if __name__ == '__main__':
    app.run(debug=True)
