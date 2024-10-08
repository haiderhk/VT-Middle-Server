from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

# Store the Flask API URL in memory (you can later extend this to use a database)
CURRENT_FLASK_API_URL = "http://localhost:8000"  # Initial value, change as needed

# HTML template for the web interface
html_template = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <title>Update Flask API URL</title>
</head>
<body>
  <div style="display:flex; flex-direction:column; align-items:center; margin-top:50px;">
    <h2>Update Flask API URL</h2>
    <form method="POST">
      <label for="api_url">Current API URL:</label><br>
      <input type="text" id="api_url" name="api_url" value="{{ api_url }}" style="width:300px;"><br><br>
      <input type="submit" value="Update API URL" style="padding:5px 10px;">
    </form>
  </div>
</body>
</html>
"""

# Route to return the current Flask API URL
@app.route('/api', methods=['GET'])
def get_api_url():
    return jsonify({"flask_api_url": CURRENT_FLASK_API_URL})

# Route to render the web form and update the API URL
@app.route('/update-api', methods=['GET', 'POST'])
def update_api_url():
    global CURRENT_FLASK_API_URL
    if request.method == 'POST':
        # Get the new URL from the form submission
        new_url = request.form.get('api_url')
        if new_url:
            CURRENT_FLASK_API_URL = new_url
    return render_template_string(html_template, api_url=CURRENT_FLASK_API_URL)

if __name__ == "__main__":
    app.run()