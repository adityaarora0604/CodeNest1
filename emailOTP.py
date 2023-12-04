import random
import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

server.login ('karanjio2001@gmail.com', 'kngykzmsbxvwbzfo')
#you can take any email as you want...
sender='LOVELY PROFESSIONAL UNIVERSITY'
subject='OTP'
otp=''.join ([str(random.randint(0,9)) for i in range (4)])
for i in range (3):
    msg=f'from: {sender}\Subject: {subject} \n\n hello dear student come to your class, \nYour OTP is '+str(otp)
    
    receiver='abinashinduri7883@gmail.com'
    
    server.sendmail (sender, receiver, msg)
    print ("OTP sent to ", receiver)
a=input ("enter your otp >>: ")
if a == otp:
    print ("verified")
    print ("please check your otp again")

else:
    print ("please check your otp again")

server.quit()
