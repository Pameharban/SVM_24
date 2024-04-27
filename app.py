from flask import Flask,request,render_template
import pickle
import numpy as np
app=Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')
@app.route('/prediction',methods=['GET','POST'])
def predict():
    if request.method =='POST':
        gender=request.form['gender']
        
        age=request.form['age']
        salary=request.form['salary']
        model=pickle.load(open('model.pkl','rb'))
        feature=np.array([[gender,age,salary]])
        prediction=model.predict(feature)
        print (prediction[0])
        return render_template('index.html',pred_res=prediction[0])
if __name__=='__main__':
    app.run()