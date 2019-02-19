# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com',587)
 
# start TLS for security
s.starttls()
 
# Authentication
s.login("srjshinde@gmail.com", "xxxxxxxxxxxx")
 
# message to be sent
message="zala reyyy.."
 
# sending the mail
s.sendmail("srjshinde@gmail.com", "srjshinde@gmail.com", message)
 
# terminating the session
s.quit()
