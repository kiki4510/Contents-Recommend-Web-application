from machine import mean

#머신러닝
from sklearn.model_selection import train_test_split
train, val = train_test_split(mean, test_size=0.2, random_state=2)
features = 'genre'
target = 'recommend'

from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.pipeline import make_pipeline
from category_encoders import OrdinalEncoder
from sklearn.impute import SimpleImputer
rf = make_pipeline(
    OrdinalEncoder(),
    SimpleImputer(strategy='most_frequent'),
    RandomForestClassifier())
X_train = train[features]
y_train = train[target]
X_val = val[features]
y_val = val[target]

rf.fit(X_train, y_train)

import pickle

with open('model.pkl','wb') as pickle_file:
    pickle.dump(rf, pickle_file)