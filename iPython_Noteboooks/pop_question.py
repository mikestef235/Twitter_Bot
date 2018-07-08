import re
import os
os.chdir('C:/Users/mikes/Documents/ChatBot/iPython_Noteboooks')

#Open the quesiton file
with open('test.txt', 'r') as f:
    data = f.read().splitlines(True)
    question = data[0] # Get the question of the day
    
#Remove the question of the day from the file
with open('test.txt', 'w') as f:
    f.writelines(data[1:])

#Write the QOD to text file
with open('qod.txt', 'w') as q:
    q.write(question)