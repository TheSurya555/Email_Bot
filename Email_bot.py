import smtplib
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = "testsurya89@outlook.com"
receiver_email = "suryakingsahoo60063@gmail.com"
subject = "this is atest case maill send by surya"
body = """"
Dear [Recipient's Name],

I hope this email finds you well. We are excited to extend an invitation to you for [Event/Meeting Name] scheduled for [Date and Time]. This event is [brief description of the event].

Details of the event:
- Date: [Date]
- Time: [Time]
- Venue: [Venue]

We believe that your presence would greatly contribute to the success of this event. Your insights and expertise would be valuable in [mention specific areas/topics that will be discussed].

Please RSVP by [RSVP Deadline] to confirm your attendance. If you are unable to attend, kindly let us know in advance.

We look forward to your participation and hope to see you at [Event Venue].

Thank you for considering our invitation.

Best regards,

[Your Full Name]
[Your Position]
[Your Company]
[Your Contact Information]
"""
password = getpass.getpass("Enter your password:")

# Setup the MIME
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Attach the body to the email
message.attach(MIMEText(body, "plain"))
# Establish a connection to the SMTP server
try:
    with smtplib.SMTP("smtp-mail.outlook.com", 587) as server:  
        # Start the TLS connection (for Gmail)
        server.starttls()
        # Login to your email account
        server.login(sender_email, password)
        # Send the email
        server.send_message(message)
        #server.sendmail(sender_email, receiver_email, message)
    print("Email sent successfully!")
except Exception as e:
    print(f"fail to send mail:{str(e)}")

