from flask import Flask, send_from_directory

app = Flask(__name__, static_folder=".", static_url_path="")

# Serve index.html
@app.route("/")
def home():
    return send_from_directory(".", "E251003_index5.html")

if __name__ == "__main__":
    # '0.0.0.0' makes server visible to others in sam LAN.
    app.run(host="0.0.0.0", port=5003, debug=False)