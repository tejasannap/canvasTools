import re
import json


regex = (r"id=\"answer_[^\"]*\"\n"
	r"       style=\"\"\n"
	r"      title=\"([^\"]*).>")

file = open("c:\Users\Tejas Annapareddy\canvasTools\canvasTools\quiz.html", "r", encoding="utf8").read().strip()

answerMatch = re.finditer(regex, file)

# for matchNum, match in enumerate(matches, start=1):
    
#     # print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
#     for groupNum in range(0, len(match.groups())):
#         groupNum = groupNum + 1
        
#         # print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
#         print(match.group(groupNum))

# for matchNum, match in enumerate(matches, start=1):

#   print(match.groups())

#   if matchNum % 4 == 0:
#     print()
#   # for groupNum, group in enumerate(match.groups(), start=0):
#   #     print(group)



# original_str = "You selected this answer. This was the correct answer. Option 1"
# selected_answer = ""

# if "You selected this answer. This was the correct answer." in original_str:
#     selected_answer = original_str.replace("You selected this answer. This was the correct answer. ", "")
#     print("Selected answer:", selected_answer)
# else:
#     print("No answer selected.")

# print("Original string:", original_str)

questions = {}

for i in range(5):

    tempanswer = {}
    answer = {}

    a = 0
    b = 0
    tf = False

    for matchNum, match in enumerate(answerMatch, start=0):

        ans = match.groups()
        ans_str = "{ans}".format(ans = ans)
        ans_str = ans_str.lower()
        a = a + 1


        if "true" in ans_str or "false" in ans_str:
            if a == 3:
              b = b + 1
              a = 0

              answer[b] = tempanswer
              tempanswer = {}
            else:
                print(match.groups())
                tempanswer[a] = ans

        elif a == 5:
            b = b + 1
            a = 0

            # print(tempanswer)
            # print()
            answer[b] = tempanswer
            tempanswer = {}
        else:
            print(match.groups())
            tempanswer[a] = ans

    first = { 
    "question": "ques",
    "correct": "correct",
    "ans": answer
    }
        
    
    questions[i] = first




with open("answer.txt", "w") as f:
    json.dump(questions, f, indent = 4)