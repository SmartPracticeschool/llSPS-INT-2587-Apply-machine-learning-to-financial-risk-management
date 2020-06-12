from flask import Flask , render_template , request
app = Flask(__name__) # interfacee between by server and my application wsgi
import pickle
from sklearn.preprocessing import StandardScaler
model = pickle.load(open('svmrisk.pkl','rb'))
scaler = pickle.load(open("scalar.pkl","rb"))
@app.route('/') # bind to an url 
def helloworld():
    return render_template("index.html")
@app.route('/login',methods = ['POST']) # bind to an url 
def admin():
    u = request.form["age"]
    v = request.form["gen"]
    a = request.form["js"]
    b = request.form["hs"]
    c = request.form["sa"]
    d = request.form["ca"]
    e = request.form["cra"]
    f = request.form["dh"]
        #Note while passing t see the order of dataset
    t = [[int(f),int(e),int(d),int(c),int(b),int(a),int(v),int(u)]]
    y=model.predict(scaler.transform(t))
    if(y==0):
        return render_template("index.html", y ="The risk would be "+str(y)+", which is bad.")
    if(y==1):
        return render_template("index.html", y ="The risk would be "+str(y)+", which is good.")
    
@app.route('/user')#url
def user():
    return "hie user"

if __name__ == '__main__' :
    app.run(debug = True)


