import smtplib
from email.message import EmailMessage
email= EmailMessage() #creating object
email['from']='abc name'
email['To']='abc id'
email['Subject']='abc subject'
email.set_content("The content of email")
with smtplib.SMTP(host='smtp.gmail.com',port=587)as smtp:
    
    smtp.ehlo()   #server object
smtp.starttls()   #to send data between server and client
smtp.login("Email_id","Password")
smtp.send_message(email)  #sending email
print("Email sent successfully")