from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    return render_template('index.html')

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run('0.0.0.0',port=8000,debug=True)
