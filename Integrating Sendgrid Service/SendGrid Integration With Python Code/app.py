import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='swetham182@gmail.com',
    to_emails='s9179906@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('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'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.body)