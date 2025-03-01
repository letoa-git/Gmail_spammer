import smtplib


toaddrs = 'sandroaleqsaniani1@gmail.com'
fromaddrs = 'twifk163@gmail.com'
message = 'sandro aizete'

with smtplib.SMTP('smtp.gmail.com', '587') as smtpserver:
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login('twifk163@gmail.com', 'yyeh zhhm gjwa kfag')

    for i in range(10000):
        smtpserver.sendmail(fromaddrs, toaddrs, message)
        print(i)
