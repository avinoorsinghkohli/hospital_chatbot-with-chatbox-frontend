from app import app
from flask import Flask, render_template, url_for, redirect, flash, get_flashed_messages, request
import requests
import sys
output=[]
image=False
@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method=='POST':
        
        if len(list(request.form.values()))==2:
            
            ans='yes'
            print(ans,'*')
            r=requests.post("http://localhost:5002/webhooks/rest/webhook",json={"message":str(ans)})
            bot_message=""

            for i in r.json():
                
                if "text" in i.keys():
                    bot_message=bot_message+i['text']
                    #print(f"{i['text']}")
                if "image" in i.keys():
                    bot_message=bot_message+i['image']
                    #print(f"{i['image']}")
            
            image=False
            output.extend([("avi",str(list(request.form.values())[1])), ("charlie", bot_message)])
            return render_template("home.html", result=output, image=image)
        else:
            result=list(request.form.values())[0]
            if result.lower() =="restart":
                output.clear()
            else:
                try:
                    print(result)
                    r=requests.post("http://localhost:5002/webhooks/rest/webhook",json={"message":str(result)})
                    print(r)
                    bot_message=""

                    print(r.json())
                    for i in r.json():

                        if "text" in i.keys():

                            bot_message=bot_message+i['text']
                            #print(f"{i['text']}")

                        if "image" in i.keys():
                            bot_message=bot_message+i['image']
                            #print(f"{i['image']}")
                    if bot_message.find("image")!=-1:
                        image=True
                    else:
                        image=False
                    output.extend([("avi", result), ("charlie", bot_message)])


                except:
                    print("Invalid Output\n")
                    print(sys.exc_info()[0])
                    if bot_message.find("image")!=-1:
                        image=True
                    else:
                        image=False
                    output.extend([("avi", result), ("charlie", "Error")])
            
            return render_template("home.html", result=output,image=image)
    return render_template("home.html", result=output, image=image)

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    global output
    output=[]
    result="Hi"
    try:
        print(result)
        r=requests.post("http://localhost:5002/webhooks/rest/webhook",json={"message":str(result)})
        print(r)
        bot_message=""
        print(r.json())
        for i in r.json():
            
            if "text" in i.keys():
                bot_message=bot_message+i['text']
                #print(f"{i['text']}")
            if "image" in i.keys():
                bot_message=bot_message+i['image']
                #print(f"{i['image']}")
            
        output.extend([ ("charlie", bot_message)])
        print(output)
        
        print("asdasd")
    except:
        print("Invalid Output\n")
        print(sys.exc_info()[0])
        output.extend([ ("charlie", "Error")])
    print(output)
    return render_template("home.html", result=output)
    