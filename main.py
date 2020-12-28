import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
user_id = input('Enter your gmail id: ')
pswd = input('Enter your password: ')
server.login(user_id, pswd)
to_id = input('Whom you want to send the mail? ')
msg = input('Type message here: ')
server.sendmail(user_id, to_id, msg)
