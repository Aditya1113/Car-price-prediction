from django.shortcuts import render
from django.http import HttpResponse
import joblib
import pickle
import pandas as pd
with open('car_price_prediction.pkl','rb') as f:
    model=pickle.load(f)

# Create your views here.
def home(request):
    return render(request,'carprice.html')
def car(request)    :
    return render(request,'carprice.html')
def prediction(request):
    if request.method == "POST":
# get all the post parameter
        Present_Price= request.POST['presentprice']
        year = request.POST['year']
        Kms_Driven = request.POST['kmdriven']
        Owner = request.POST['owner']
        Fuel_Type_Petrol = request.POST['fueltype']
        Seller_Type_Individual= request.POST['sellertype']
        Transmission_Manual= request.POST['transmission']
        if Fuel_Type_Petrol=='Petrol':
            Fuel_Type_Petrol=1
            Fuel_Type_Diesel=0
        elif Fuel_Type_Petrol=='Diesel':
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=1 
        else:
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=0 
        if Seller_Type_Individual=='Individual':
            Seller_Type_Individual=1
        else:
            Seller_Type_Individual=0    
        if Transmission_Manual=="Manual":
            Transmission_Manual=1
        else:
            Transmission_Manual=0
        current=2021
        years_old=current-int(year)
        prediction=model.predict([[	float(Present_Price),float(Kms_Driven),Owner,years_old,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Manual]])
        output=round(prediction[0],2)
        param={"output":output}
        return render(request,'output.html',param)     
    
    
