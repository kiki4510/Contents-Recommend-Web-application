from flask import Blueprint,render_template, request
import pickle
from sklearn.pipeline import Pipeline
from sklearn.pipeline import make_pipeline
import pandas as pd


bp = Blueprint('result', __name__, url_prefix='/result')
model = None
with open('model.pkl','rb') as pickle_file:
   model = pickle.load(pickle_file)

@bp.route('/', methods =['GET','POST'])
def results():
   genre = request.form
   X_test = pd.Series([genre])
   X_test.name='genre'
   enc = model.named_steps['ordinalencoder']
   test_encoded = enc.transform(X_test)
   y_pred = model.predict(test_encoded)
   if y_pred[0] == True :
      return render_template('recommend.html')
   else :
      return render_template('not_recommend.html')