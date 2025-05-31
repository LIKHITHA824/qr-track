from flask import Flask, redirect, request
import datetime

app = Flask(__name__)
LOG_FILE = "scan_logs.txt"

@app.route('/qr')
def track_scan():
    # Log time and IP
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.datetime.now()} - {request.remote_addr}\n")
    
    # ✅ Redirect to the actual Google Drive PDF link
    return redirect("https://drive.google.com/file/d/1B-Pu3yyU0ODYw7N2qsV7368FkPIS2j2c/view?usp=drive_link")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
