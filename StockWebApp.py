#!/usr/bin/env python
# coding: utf-8

# In[1]:


#get_ipython().system('pip install pywebio')


# In[22]:


from pywebio.input import *
from pywebio.output import *


# In[23]:


stock_value = select('About which stock do you want to know?', ['Amazon', 'Netflix','BTC'])


# In[4]:


stock_value


# In[5]:


import pymongo


# In[6]:


import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["UBhack"]


# In[7]:


mycol = mydb["stockFuturePrices"]


# In[18]:


current_price = mycol.find_one()['stock_future']


# In[19]:


from pywebio.output import *
# Text Output
put_text("Current Stock Price: " +  current_price)


# In[ ]:
store_days = list(range(1,91))

if stock_value == 'Amazon':
    days = select('For how many days do you want to hold it?', store_days)
    future_stock_price = mycol.find_one({'' : int(days)+1})['stock_future']
    put_text("Stock Price after " + str(days) + " days: " +  future_stock_price)
    hold = radio('Are you currently holding one?', options=['Yes','No'])
    if hold == 'Yes':
        buy_price = input("Please type at what price did you buy")
        if buy_price < current_price:
            put_text("You are in Profit now")
        else:
            put_text("You are in Loss now")
        
        if buy_price < future_stock_price:
            if future_stock_price > current_price:
                put_text("You will be in profit if you hold these stocks for " + str(days) + " days")
            else:
                put_text("Profit margin will be greater if you sell it now than to sell it after " + str(days) + " days")
        else:
            put_text("You will be in loss if you hold these stocks for " + str(days) + " more days. You can sell it or can consider hold period longer")

        



