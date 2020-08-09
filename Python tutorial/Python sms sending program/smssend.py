import requests
import json

def send(mobile,msg):
    if type(mobile) is not str:
        return "Please enter valid phone number in string format"
    elif type(msg) is not str:
        return "Please enter valid message in string format"
    f1=open("api.txt","r")
    a=list()
    temp=f1.readline()
    while temp:
        a.append([temp[:32],temp[32:48]])
        temp=f1.readline()
    f1.close()
    response = requests.post('http://www.way2sms.com/api/v1/sendCampaign',{'apikey':a[0][0],'secret':a[0][1],'usetype':'stage','phone': mobile,'message':msg,'senderid':''})
    b=a;
    while response.text.find("\"status\":\"error\"") is not -1:
        if response.text.find("\"message\":\"API and Secret keys are expired.\"") is not -1:
            del a[0];
            response = requests.post('http://www.way2sms.com/api/v1/sendCampaign',{'apikey':a[0][0],'secret':a[0][1],'usetype':'stage','phone': mobile,'message':msg,'senderid':''})
            b=a
        if response.text.find("\"message\":\"Invalid phone number is given.\"") is not -1:
            return "Mobile number is invalid"
        if response.text.find("\"message\":\"API and Secret key verification failed.\"") is not -1:
            print("please checkout this api and secret key. they can not be verified\nAPI key : ",a[0][0],"\n","Secret key : ",a[0][1])
            if len(b)!=1:
                del b[0]
                response = requests.post('http://www.way2sms.com/api/v1/sendCampaign',{'apikey':b[0][0],'secret':b[0][1],'usetype':'stage','phone': mobile,'message':msg,'senderid':''})
            else:
                return "API and secret keys can not matched"
    f1=open("api.txt","w")
    newtext=""
    for i,j in a:
        newtext=newtext+i+j+"\n"
    f1.write(newtext)
    del newtext
    f1.close()
    return "sms successfully sended"

send("919601501725","hello nishla")
