from flask import Flask, render_template, request, redirect, url_for
import requests
import time
import json
from database import init_db, log_request, get_all_logs, delete_all_logs

app = Flask(__name__)

# Initialize the database when app starts
init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        url = request.form.get("url", "").strip()
        method = request.form.get("method", "GET")
        body = request.form.get("body", "").strip()

        if not url:
            error = "Please enter a URL."
        else:
            try:
                start_time = time.time()

                if method == "GET":
                    response = requests.get(url, timeout=10)
                elif method == "POST":
                    # Try to parse body as JSON if provided
                    headers = {"Content-Type": "application/json"}
                    json_body = json.loads(body) if body else {}
                    response = requests.post(url, json=json_body, headers=headers, timeout=10)

                end_time = time.time()
                response_time = round((end_time - start_time) * 1000, 2)  # in milliseconds

                # Try to pretty-print JSON response
                try:
                    response_data = json.dumps(response.json(), indent=2)
                except Exception:
                    response_data = response.text

                # Save to database
                log_request(
                    url=url,
                    method=method,
                    request_body=body,
                    status_code=response.status_code,
                    response_body=response_data,
                    response_time=response_time
                )

                result = {
                    "url": url,
                    "method": method,
                    "status_code": response.status_code,
                    "response_time": response_time,
                    "response_body": response_data,
                }

            except requests.exceptions.ConnectionError:
                error = "Connection error. Check if the URL is correct and reachable."
            except requests.exceptions.Timeout:
                error = "Request timed out. The server took too long to respond."
            except json.JSONDecodeError:
                error = "Invalid JSON in request body. Please check your formatting."
            except Exception as e:
                error = f"Unexpected error: {str(e)}"

    logs = get_all_logs()
    return render_template("index.html", result=result, error=error, logs=logs)


@app.route("/clear", methods=["POST"])
def clear_logs():
    delete_all_logs()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)