import random

points=0

class QA:
    def __init__(self, question, answer, pointsReward):
        self.question=question
        self.answer=answer
        self.pointsReward=pointsReward
        self.done=False
    def showQuestion(self):
        print(self.question)
    def checkAnswer(self, answer):
        if answer == self.answer:
            points+=1

list=[]
list.extend([QA("Hva er hovedstaden i Frankrike?", "Paris", 1),QA("Hvor mange dager er det i året?","365",1),QA("Hor mange planeter er det i solsystemet","8",1)])

def ask():
    for i in list:
        i.showQuestion()

ask()
