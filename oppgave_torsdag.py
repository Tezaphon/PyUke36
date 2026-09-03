import random
from colorama import Fore

pointsGlobal=0
list=[]
#class definition
class QA:
    def __init__(self, question, answer, pointsReward):
        self.question=question
        self.answer=answer
        self.pointsReward=pointsReward
        self.done=False
    def showQuestion(self):
        print("------------------------------------")
        print(self.question)
    def checkAnswer(self, answer):
        self.done=True
        if answer == self.answer:
            print(Fore.GREEN+"Riktig!"+Fore.RESET)
            return self.pointsReward
        else:
            print(Fore.RED+"Feil!"+Fore.RESET)
            return 0

#list definition
#can add new questions by following a blueprint under
#QA("question", "answer", points reward)

list.extend([
    QA("Hva er hovedstaden i Frankrike?", "Paris", 1),
    QA("Hvor mange dager er det i året?","365",1),
    QA("Hvor mange planeter er det i solsystemet","8",1),
    QA("Hvor mange måner Mars har?","2",2),
    QA("Hvor høyt er Galdhøppingen?","2469",4),
    QA("Hvilket år fikk Norge grunnlov?","1814",3)
    ])

#quiz functional parts definition

quizRunning=True
def checkQuiz():
    _notAnsweredQuestionsCounter=0
    for i in list:
        if i.done==False:
            _notAnsweredQuestionsCounter+=1
    if _notAnsweredQuestionsCounter ==0:
        quizRunning=False
        print("====================================")
        print("Quizen er over.")
        print("Poeng - "+str(pointsGlobal))
        print("====================================")

def ask(_points):
    index=random.randint(0, len(list)-1)
    if list[index].done==False:
        list[index].showQuestion()
        svar=input("Ditt svar: ")
        _points+=list[index].checkAnswer(svar)

#runtime

print("Velkommen til en quiz")
start=input("Start?")
while quizRunning==True:
    ask(pointsGlobal)
    checkQuiz()