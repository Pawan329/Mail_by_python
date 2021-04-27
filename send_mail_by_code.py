# Python code to illustrate Sending mail from
# your Gmail account
import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("your_mail_id", "type_your_password")

# message to be sent
message = "Type_your_message_here"

# sending the mail
s.sendmail("sender_mail", "receiver_mail", message)

# terminating the session
s.quit()
