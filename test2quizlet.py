import re

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

    group_list = []
    answer = []
  
    for matchNum, match in enumerate(answerMatch, start=1):
          groups = match.groups()
          group_list.extend(groups)
          
          if len(group_list) == 4:
              dictionary = {f"answer_{i+1}": group_list[i] for i in range(4)}
              answer.append(dictionary)
              group_list.clear()
      
        
    first = { 
    "question": ques,
    "correct": correct,
    "ans": answer
    }
        
    
    questions[q] = first



  

print(questions)

# for q in range(len(questions)):

#   print(questions[q])




def write_pairs(pairs: dict, location: str):
    '''Writes question-and-answer pairs to a text file in the Quizlet tab-separated format'''
    with open(location, 'w', encoding="utf8") as f:
        for key in pairs.keys():
            newkey = key.split("&lt;span style=&quot;font-family: times new roman; font-size: 12pt; color: #000000;  &quot;&gt;") 
            f.write(f"{newkey}\t{pairs[key]}\n")



