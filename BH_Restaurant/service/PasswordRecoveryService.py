import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class PwBackUpEmail:

    def sendEmail(self,remail,pw):
        try:
            print("recover pw")
            sender_email = "mail4kumuditha@gmail.com"
            receiver_email = remail
            password = "mailforkuma123$"

            message = MIMEMultipart("alternative")
            message["Subject"] = "BTH Restaurant - Password Recover Details"
            message["From"] = sender_email
            message["To"] = receiver_email

            # Create the plain-text and HTML version of your message
            text = "Your BTHouse Use Account Password is: " + pw

            # Turn these into plain/html MIMEText objects
            part1 = MIMEText(text, "plain")
            # part2 = MIMEText(html, "html")

            # Add HTML/plain-text parts to MIMEMultipart message
            # The email client will try to render the last part first
            message.attach(part1)
            # message.attach(part2)

            # Create secure connection with server and send email
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(
                    sender_email, receiver_email, message.as_string()
                )
            return "0"

        except:
            print("Something went wrong with the Email Server..!")




