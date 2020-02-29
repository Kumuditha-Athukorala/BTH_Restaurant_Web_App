import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailBTH:

    def sendEmail(self,data):

        if(data.get("o_purpose") == "cancelOrder"):
            try:
                print("cancel order")
                sender_email = "mail4kumuditha@gmail.com"
                receiver_email = data.get("o_email")
                password = "mailforkuma123$"

                message = MIMEMultipart("alternative")
                message["Subject"] = "BTH Restaurant - Order Details"
                message["From"] = sender_email
                message["To"] = receiver_email

                # Create the plain-text and HTML version of your message
                text = """\
                                 Hi,
                                 Thank you for choosing BT-HOUSE."""
                html = """\
                                 <html>
                                   <body>
                                   <h5> Hi, <br>
                                      Thank you for choosing BT-HOUSE. </h5>
                                     <p>We are really sorry, We cannot process your booking right now..!!! <br>
                                     For More Information Please Contact Us :- 08964553425 <br><br>
                                     Thank You.<br>
                                     BT-HOUSE MANAGEMENT
                                     </p>
                                   </body>
                                 </html>
                                 """

                # Turn these into plain/html MIMEText objects
                part1 = MIMEText(text, "plain")
                part2 = MIMEText(html, "html")

                # Add HTML/plain-text parts to MIMEMultipart message
                # The email client will try to render the last part first
                message.attach(part1)
                message.attach(part2)

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

        if(data.get("purpose") == "processOrder"):
            try:
                print("process Order")
                sender_email = "mail4kumuditha@gmail.com"
                receiver_email = data.get("o_email")
                password = "mailforkuma123$"

                message = MIMEMultipart("alternative")
                message["Subject"] = "BTH Restaurant - Order Details"
                message["From"] = sender_email
                message["To"] = receiver_email

                # Create the plain-text and HTML version of your message
                text = """\
                                            Hi,
                                            Thank you for choosing BT-HOUSE."""
                html = """\
                                            <html>
                                              <body>
                                              <h5> Hi, <br>
                                                 Thank you for choosing BT-HOUSE. </h5>
                                                <p>We are happily inform you that, We have processed your booking..!!! <br>
                                                For More Information Please Contact Us :- 08964553425 <br><br>
                                                Thank You.<br>
                                                BT-HOUSE MANAGEMENT
                                                </p>
                                              </body>
                                            </html>
                                            """

                # Turn these into plain/html MIMEText objects
                part1 = MIMEText(text, "plain")
                part2 = MIMEText(html, "html")

                # Add HTML/plain-text parts to MIMEMultipart message
                # The email client will try to render the last part first
                message.attach(part1)
                message.attach(part2)

                # Create secure connection with server and send email
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(
                        sender_email, receiver_email, message.as_string()
                    )
                return "1"

            except:
                print("Something went wrong with the Email Server..!")
