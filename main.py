from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
import smtplib
import os

app = Flask(__name__)
Bootstrap5(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


MAIL_ADDRESS = os.environ.get('EMAIL')
MAIL_APP_PW = os.environ.get('PWD')


def send_email(name, email, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MAIL_ADDRESS, MAIL_APP_PW)
        connection.sendmail(
            from_addr=MAIL_ADDRESS,
            to_addrs=MAIL_ADDRESS,
            msg=email_message
        )


if __name__ == '__main__':
    app.run(debug=True)
