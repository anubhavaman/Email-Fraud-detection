

import numpy as np 
import pandas as pd
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltp import Preprocessor

df = pd.read_csv('fraud_email_.csv')
df.head()

df.rename(columns={'Text':'Emails'}, inplace=True)
df.isnull().sum()

df.dropna(inplace=True)
#print(df.columns.tolist()) #prints the columns name 
df['Class'].value_counts()
df.shape

sns.countplot(df['Class'])
plt.title("Plot of Target Variable")
plt.show()

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import BernoulliNB
from nltk.corpus import wordnet

pre = Preprocessor(df['Emails']).text_cleaner()

pre[2]

words = pre
plt.figure(figsize = (20,20))
word_cloud  = WordCloud(max_words = 1000 , width = 1600 , height = 800,
               collocations=False).generate(" ".join(words))
plt.imshow(word_cloud,interpolation='bilinear')
plt.axis('off')
plt.show()

X = pre
y = df['Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=True, random_state=42)
print(f'Spliting Completed') 
print(f'X Train: {len(X_train)} X Test: {len(X_test)} y Train: {len(y_train)} y Test: {len(y_test)}')

def fit_predict(model):   
    clf = Pipeline([('tfidf',TfidfVectorizer()),
                   ('clf',model)])


    clf.fit(X_train, y_train)
    print(f'Fitting Model Completed.')
    
    
    Score = clf.score(X_test,y_test)
    print(f'Accuracy: {Score*100}') 
    
    return clf


class Metrics():
    
    def __init__(self, pred):
        self.pred = pred
        
    def cm(self):
        cm = confusion_matrix(y_test, self.pred)
        labels = ['Not Spam','Spam']

        f, ax = plt.subplots(figsize=(5,5))
        sns.heatmap(cm,annot =True, linewidth=.6, linecolor="r", fmt=".0f", ax = ax)

        ax.set_xticklabels(labels)
        ax.set_yticklabels(labels)
        plt.show()

    def report(self):
        class_report = classification_report(y_test, self.pred)
        print(class_report)
        
LR_model = fit_predict(LogisticRegression())

LR_pred = LR_model.predict(X_test)

Metrics(LR_pred).cm()

Metrics(LR_pred).report()

SVC_model = fit_predict(LinearSVC())

SVC_pred = SVC_model.predict(X_test)


Metrics(SVC_pred).cm()

Metrics(SVC_pred).report()

NB_model = fit_predict(BernoulliNB())

NB_pred = NB_model.predict(X_test)


Metrics(NB_pred).cm()

Metrics(NB_pred).report()

import joblib

filename = 'model.joblib'
joblib.dump(LR_model,open(filename,'wb'))

filename2 = 'modelNB.joblib'
joblib.dump(NB_model,open(filename2,'wb'))

with open('model.joblib','rb') as f:
    model = joblib.load(f)

model
with open('modelNB.joblib','rb') as f:
    model2 = joblib.load(f)
model2

'''
import tkinter as tk

from tkinter import ttk

win = tk.Tk()

win.title('Email Fraud Detection')

preg = ttk.Label(win,text ="preg")
preg.grid(row = 0,column = 0,sticky = tk.W)

Preg_Entry = tk.Text(win,width = 16,height = 20)
Preg_Entry.grid(row = 1,column = 0)
email = Preg_Entry.get("1.0","end-1c")
pre2 = Preprocessor(email).text_cleaner()

import pandas as pd
df = pd.DataFrame()
def action():
    global db
    import pandas as pd
    df = pd.DataFrame(columns = ['Emails'])
    df.loc[0,'Emails'] = pre2
print(df.shape)
db = df
output = model.predict(pre2)
if output == 1:
    result = 'Spam'
else:
    result = 'not spam'

Predict_entrybox=ttk.Entry(win,width=16)
Predict_entrybox.grid(row=20,column=1)
Predict_entrybox.insert(1,str(result))
Predict_button=ttk.Button(win,text="Predict",command=Output)
Predict_button.grid(row=20,column=0)

win.mainloop()
'''