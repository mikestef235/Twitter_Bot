import tweepy as tp
import time
import os
import pandas as pd

#Let user know script is running
print("Script running now!")

#Login Credentials
consumer_key = 'WGzQES69TbpX2e5yZeXCYDEP6'
consumer_secret = 'U7Z8MgwDPoqrlk68hRRDWcc6o8ocq5HtuxWE3cyvwlV0MlzfeY'
access_token = '1012844363439923206-KPByPm9lfmpOzvZrExqRwneNpY7BV0'
access_secret = 'hVzSQ6JMSZs4ilM31UcLPCgzy6yrASa0WFC33MP0nM6jK'

#Login Through Twitter API
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

#Q+A
#Change working directory
os.chdir('C:/Users/mikes/Documents/ChatBot/iPython_Noteboooks')
#Reading in the files
df = pd.read_csv('QandADf.csv').drop('Unnamed: 0', axis=1)
#Get quetions and answers to tweet today
today_data = df[:5]
#Remove the questions and consider them asked
df  = df[5:]
df.to_csv('QandADf.csv', encoding='utf8')

#Prep the questions and answers for tweeting
for index, row in today_data.iterrows():
    q = 'Question: ' + row['Question'] + '\n'
    a = 'Answer: ' + row['Answer']
    api.update_status(q+a)
    time.sleep(5)

print('Script Finished!')
time.sleep(3)