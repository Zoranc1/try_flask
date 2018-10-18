from flask import Flask, render_template,request, redirect 


app = Flask(__name__)

messages = [
    {
    'author':' Richard',
    'text':'Some text'
    },
    {
    'author':'Tony',
    'text':'Diferent text'
    }
    ]


@app.route("/")
def show_hi():
    return render_template("index2.html", data=messages)
    
@app.route("/add" ,methods=["POST"])    
def ack_message():
    message=request.form['msg']
    message_dict ={
        'author':'Me',
        'text':message
    }
    messages.append(message_dict)
    return redirect("/") 
    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug=True)