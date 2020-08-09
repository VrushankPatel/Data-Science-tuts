import smtplib
def sendmail(msg,destinationaddress):
    
    username = 'ServiceEduwiz@gmail.com'
    password = 'eduwiz@123'
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(username,destinationaddress, msg)
    server.quit()
    return "Success"

sendmail("hllo","vrushankpatel5@gmail.com")
