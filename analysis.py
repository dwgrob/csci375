from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from config import SQLALCHEMY_DATABASE_URI
import os

app = Flask(__name__)

# Using the same configuration thats in testapp.py to access the database
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Making classes to use for the analysis, for now it doesn't directly call from the database cause i dont know how
class Users:
    # Defining some attributes of the user, this will be changes to call the database
    def __init__(self, id, income, assets, liabilities, tags):
        self.id =  id
        self.income = income
        self.assets = assets
        self.liablilities = liabilities
        self.tags = tags

    # Creating a projection for the user over a certain amount of months
    def Projection(self):
        moneyIn = self.income
        moneyOut = self.liablilities
        moneyCurrent = self.assets
        growth = moneyIn * 12
        depreciation = moneyOut * 12
        netChange = growth - depreciation
        newMoney = moneyCurrent + netChange

        print(f"{self.id} your starting asset total is {self.assets}.")
        print(f"If your income and liabilities stays the same over the next 12 months, your net change in value will be {netChange} with your assets being worth {newMoney}")
        print(f"Based on the tags of different income, assets and liability types you have some reccomended blogs are {self.tags}")
        # For the self.tags that can be changes with a call to the blog table in the database and return blogs with the same tags

user1 = Users(1, 2000, 1000, 2050, ['studentLoan', 'carLoan', 'rent', 'investments', 'partTimeJob'])
user2 = Users(2, 100, 50000, 3000, ['studentLoan', 'rent', 'investments', 'fullTimeJob'])
user3 = Users(3, 0, 10000, 1000, ['studentLoan', 'rent'])

user1.Projection()
user2.Projection()
user3.Projection()
