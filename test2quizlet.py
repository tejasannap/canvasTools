import re
import json

file = open("quiz.html", "r", encoding="utf8").read().strip()

questionRegex = r"\"textarea_question_text\">&lt;span style=&quot;font-family: times new roman; font-size: 12pt; color: #000000;  &quot;&gt;([\s\S]*?)&lt;[^\"]span&gt;<"

questionMatch = re.finditer(questionRegex, file)

answerRegex = (r"id=\"answer_[^\"]*\"\n"
	r"       style=\"\"\n"
	r"      title=\"([^\"]*).>")

answerMatch = re.finditer(answerRegex, file)
#print(list(answerMatch))

correctRegex = r"title=\"(.*?)(?:\.*?)(?:. This was the correct answer|. You selected this answer. This was the correct answer.)"

correctMatch = re.finditer(correctRegex, file)


questions = {}


# Add values to the nested dictionary
for q,  (cMatch, qMatch) in enumerate(zip(correctMatch, questionMatch), start=0):

    
    first = {}
    
    # ques = "WHat{b}".format(b = i)
    ques = qMatch.groups()
    correct = cMatch.groups()

    # for matchNum, match in enumerate(answerMatch, start=1):

    #   print(match.groups())
  
    
    # for x in range(3): 
    #     answer[x] = "answeris{x}".format(x = x)

    # for x, answerText in enumerate(answerMatch, start=1):
    #   print(x)
    #   answer[x] = answerText.groups()

    # group_list = []
    # aanswer = []
  
    # for matchNum, match in enumerate(answerMatch, start=1):
    #       group = match.groups()
    #       group_list.extend(group)
          
    #       if len(group_list) == 4:
    #           dictionary = {f"answer_{i+1}": group_list[i] for i in range(4)}
    #           aanswer.append(dictionary)
    #           group_list.clear()

    tempanswer = {}
    answer = {}

    a = 0
    b = 0
    tf = False

    for matchNum, match in enumerate(answerMatch, start=1):
        a = a + 1

        ans = match.groups()

        # if tf: 
        #     b = b + 1

        # if a == 2


        # if "true" in ans.lower():
        #     print('')



        if a == 4:
            b = b + 1
            a = 0
            # print(tempanswer)
            # print()
            answer[b] = tempanswer
            tempanswer = {}
        else:
            print(match.groups)
            tempanswer[matchNum] = match.groups()
        # print(ans)

      
    
        
    first = { 
    "question": ques,
    "correct": correct,
    "ans": answer
    }
        
    
    questions[q] = first



  

print(questions)


# for q in range(len(questions)):

#   print(questions[q])




# def write_pairs(pairs: str, location: str):
#     '''Writes question-and-answer pairs to a text file in the Quizlet tab-separated format'''
#     with open(location, 'w', encoding="utf8") as f:
#         f.write(pairs)


# write_pairs(questions, "output.txt")



with open("output.txt", "w") as f:
    json.dump(questions, f, indent = 4)
