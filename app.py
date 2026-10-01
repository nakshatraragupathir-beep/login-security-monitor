from flask import Flask, render_template, request
import sqlite3
from datetime import datetime

app = Flask(__name__)

USERNAME = "admin"
PASSWORD = "admin123"

failed_attempts = 0


def save_login(username, ip_address, status, login_time, attempts):

    connection = sqlite3.connect("login_monitor.db")

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO login_logs
        (username, ip_address, status, login_time, failed_attempts)
        VALUES (?, ?, ?, ?, ?)
    """, (username, ip_address, status, login_time, attempts))

    connection.commit()
    connection.close()


@app.route("/", methods=["GET", "POST"])
def login():

    global failed_attempts

    message = ""

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        ip_address = request.remote_addr
        login_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if username == USERNAME and password == PASSWORD:

            failed_attempts = 0
            message = "Login successful!"

            save_login(
                username,
                ip_address,
                "SUCCESS",
                login_time,
                failed_attempts
            )

            print("================================")
            print("LOGIN SUCCESS")
            print("Username :", username)
            print("IP Address :", ip_address)
            print("Time :", login_time)
            print("================================")

        else:

            failed_attempts += 1
            message = "Invalid username or password!"

            save_login(
                username,
                ip_address,
                "FAILED",
                login_time,
                failed_attempts
            )

            print("================================")
            print("FAILED LOGIN")
            print("Username :", username)
            print("IP Address :", ip_address)
            print("Time :", login_time)
            print("Failed Attempts :", failed_attempts)

            if failed_attempts >= 3:
                print("SECURITY ALERT: Suspicious login detected!")

            print("================================")

    return render_template("login.html", message=message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

