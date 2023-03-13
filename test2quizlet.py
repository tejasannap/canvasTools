import re

with open("quiz.html", "r", encoding="utf8") as file:
    file_content = file.read()

# Extract questions
question_regex = r"\"textarea_question_text\">&lt;span style=&quot;font-family: times new roman; font-size: 12pt; color: #000000;  &quot;&gt;([\s\S]*?)&lt;[^\"]span&gt;<"
questions = re.findall(question_regex, file_content)

# Extract answers
answer_regex = r"id=\"answer_[^\"]*\"\n       style=\"\"\n      title=\"([^\"]*).>"
answers = re.findall(answer_regex, file_content)
# print(answers)

# Extract correct answers
correct_regex = r"title=\"(.*?)(?:\.*?)(?:. This was the correct answer|. You selected this answer. This was the correct answer.)"
correct_answers = re.findall(correct_regex, file_content)

# Create a list of dictionaries, with each dictionary containing a question and its answers
quiz = []
tf = False
minus2 = False 
x = 0

for question_num, question in enumerate(questions):

    q = question_num
    tempans = "{temp}".format(temp = answers[x]).lower()

    if minus2 and not "true" in tempans or not "false" in tempans: 
        q = q - 2
        minus2 = False

    # nextans = "{temp}".format(temp = answers[x+4]).lower()

    if "true" in tempans or "false" in tempans:
        x = x + 2
        ans = ["True", "False"]
        print("True/False")
        minus2 = True


    else: 
        x = x + 4
        print("Normal Question")
        ans = answers[q * 4:(q + 1) * 4]



    # print(x)
    # print(answers[question_num])
    # if question_num == 1:
    #     x = question_num + 1
    # else:
    # if tf: 
    #     x = question_num - 2
    #     answers_for_question = answers[x * 4:(x + 1) * 4]
    #     tf = False
    # else:
    #     answers_for_question = answers[question_num * 4:(question_num + 1) * 4]
    
    # # Check if any of the answers contain the strings "true" or "false" (case-insensitive)
    # if any("true" in answer.lower() for answer in answers_for_question) or any("false" in answer.lower() for answer in answers_for_question):
    #     answers_for_question = ["True", "False"]
    #     tf = True
    #     minus2 = True
    print(question)
    print(ans)
    print()

    answers_for_question = ans
    correct_answer = correct_answers[question_num]
    question_dict = {
        "question": question,
        "answers": answers_for_question,
        "correct_answer": correct_answer
    }
    quiz.append(question_dict)


# Print the quiz

def printQuiz(): 
    for question_num, question_dict in enumerate(quiz, start=1):
        print(f"Question {question_num}: {question_dict['question']}")
        for answer_num, answer in enumerate(question_dict['answers'], start=1):
            print(f"{answer_num}. {answer}")
        print(f"Correct answer: {question_dict['correct_answer']}\n")




