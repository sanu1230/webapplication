from django.shortcuts import render
from django.http import HttpResponse
# from sklearn.externals import joblib
import joblib
import pandas as pd

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['defaulters']
collection = db['defaultTable']



reloadModel = joblib.load("./model/ModelforDefaulter.pkl")

def index(request):
    temp={}
    temp['student_Yes'] = 0
    temp['balance'] = 729.526495
    temp['income'] = 44361.625074
    context ={"temp": temp}
    return render(request, 'index.html', context)


def predictDefaulter(request):
    if request.method == 'POST':
        temp={}
        temp['student_Yes'] = request.POST.get('studentVal')
        temp['balance'] = request.POST.get('balVal')
        temp['income'] = request.POST.get('incomeVal')

    testData = pd.DataFrame({'x': temp}).transpose()
    result = reloadModel.predict(testData)
    if result == 0:
        results = 'No'
    elif result == 1:
        results = 'Yes'
    context = {"results": results, 'temp':temp}
    return render(request, 'index.html', context)


def viewDatabase(request):
    countofrow = collection.find().count()
    context = {"countofrow": countofrow}
    return render(request, 'viewDB.html', context)


def updateDatabase(request):
    temp={}
    temp['student_Yes'] = request.POST.get('studentVal')
    temp['balance'] = request.POST.get('balVal')
    temp['income'] = request.POST.get('incomeVal')
    temp['default_Yes'] =  request.POST.get('defaulterVal')
    collection.insert_one(temp)
    countofrow = collection.find().count()
    context = {"countofrow": countofrow}
    return render(request, 'viewDB.html', context)
    