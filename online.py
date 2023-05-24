import random
import json
import re


file = open("quiz.html", "r", encoding="utf8").read().strip()

questionRegex = r"\"textarea_question_text\">&lt;span style=&quot;font-family: times new roman; font-size: 12pt; color: #000000;  &quot;&gt;([\s\S]*?)&lt;[^\"]span&gt;<"
questionMatch = re.finditer(questionRegex, file)
questions = {}

answerRegex = (r"id=\"answer_[^\"]*\"\n"
	r"       style=\"\"\n"
	r"      title=\"([^\"]*).>")

answerMatch = re.finditer(answerRegex, file)
rawanswers = {}
#print(list(answerMatch))

correctRegex = r"title=\"(.*?)(?:\.*?)(?:. This was the correct answer|. You selected this answer. This was the correct answer.)"

correctMatch = re.finditer(correctRegex, file)

temp = {}
answers = {}

group = 0
tf = False
a = 0
add = False

for ansNum, ansMatch in enumerate(answerMatch, start=0):
     rawanswers[ansNum] = ansMatch.groups()

for x in range(len(rawanswers)):

    if not add:
        temp = {}
    ans = rawanswers[x]
    ans_str = "{ans}".format(ans = ans).lower()
    print(a)
    # print(ans)

    if tf: 
        temp[a] = "False"
        answers[group] = temp
        tf = False
        add = False
        group = group + 1
        a = 0
        continue

    if "true" in ans_str or "false" in ans_str:
        temp[a] = "True"
        tf = True
        add = True
    elif a == 5:
        answers[group] = temp
        group = group + 1
        add = False
        a = 0
    else:
        temp[a] = ans
        add = True

    a = a + 1


# for ansNum, ansMatch in enumerate(answerMatch, start=0):
        
#         ans = ansMatch.groups()
#         ans_str = "{ans}".format(ans = ans).lower()
#         a = a + 1
#         temp = group 
#         print("ran")



#         if "true" in ans_str or "false" in ans_str and not tf:
#             if not tf:
#                 group = group + 1
#                 tf = True
#             elif tf: 
#                 answerstest[a] = ans
#                 a = 0

#         elif a == 5:
#              group = group + 1
             
#         else: 
#              answerstest[a] = ans
#              a = 0
#         print(ans)

#         if not temp == group:
#              an[group] = answerstest
#              answerstest = {}


# print(an)   
# print(group)
# print(answers)
        

        # a = a + 1

        # if "true" in ans_str or "false" in ans_str:
        #     if a == 3:
        #         a = 0
        #         print("max")
        #     else: 
        #         print("true no max")
        #         answer[a] = ans
        # elif a == 5: 
        #     a = 0

        # # answer[ansNum] = "Computer Networking Level {x}".format(x = random.randrange(0, 100))
        # print(a)

# Add values to the nested dictionary
# for i,  (cMatch, qMatch) in enumerate(zip(correctMatch, questionMatch), start=0):
   
#     question = qMatch.groups()
#     correctans = cMatch.groups()
    
#     answer = {}
#     a = 0
    
#     for ansNum in range(3): 
#         answer[ansNum] = "Computer Networking Level {x}".format(x = random.randrange(0, 100))
#         # print(ansNum)


#     tempquestion = { 
#     "question": question,
#     "correct": correctans,
#     "ans": answer
#     }
        
    
#     questions[i] = tempquestion

# # print(questions) 


with open("online.txt", "w") as f:
    json.dump(answers, f, indent = 4)