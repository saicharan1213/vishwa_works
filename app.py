from flask import Flask,render_template,url_for,request
import pandas as pd 
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import numpy as np
import dill
# load the model from disk
c = dill.load(open('cv_trans.obj','rb'))
clf = dill.load(open('navibaye.obj', 'rb'))

app = Flask(__name__,template_folder='C:/Users/A.C.E/vishwa_awards/templates')


@app.route('/')
def home():
	return render_template('home.html')



@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        vect = cv.transform(data)    
        my_prediction = clf.predict(vect)
    return render_template('result.html',prediction = my_prediction)

if __name__ == '__main__':
	app.run(debug=False)
    
    
    
    
    
