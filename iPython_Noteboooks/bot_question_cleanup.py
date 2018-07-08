import re
import os
os.chdir('C:/Users/mikes/Documents/ChatBot/iPython_Noteboooks')

#Opening the supplied questions
with open('bot_questions.txt') as f_input, open('final_questions.txt', 'w') as output:
    for line in f_input:
        #Removing empty questions
        if len(line.strip(' ')) != 5:
            #Matching to remove question numbers
            pattern = re.compile(r"\d+\) ")
            question_number = pattern.findall(line)[0]
            output.write(line.replace(question_number, ''))


