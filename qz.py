from bs4 import BeautifulSoup
import re
import subprocess
import os

def quizlet(file: str):
    with open(file, 'r') as fp:
        soup = BeautifulSoup(fp, "html.parser")

        questions = soup.find_all("div", class_="question")

        for q in range(len(questions)):

            question = questions[q]

            question_text = question.find("div", class_="question_text user_content")
            question_text = question_text.find("span", style="font-family: times new roman; font-size: 12pt; color: #000000; ").text
            print("//" + question_text)

            answers = question.find_all("div", class_="answer")

            for a in range(len(answers)):
                answer = answers[a]

                answer_text = answer.find("span", style="font-family: times new roman; font-size: 12pt; color: #000000; ").text
                print(answer_text)

            correct = question.find("div", class_="correct_answer")
            correct_text = correct.find("span", style="font-family: times new roman; font-size: 12pt; color: #000000; ").text
            print("/" + correct_text)

        with open("q.txt", "w", encoding="utf8") as file:
            file.write(str(questions[19]))
            # print("File written successfully")


# quizlet()

# List all files in the folder
files = os.listdir('quizzes')

# Print the file names
for file in files:
    quizlet("quizzes/" + file)