# 3


listOfQuestions = [
    "1. Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie: ",
    "2. W jakich okolicznościach czytasz książki najczęściej?",
    "3. Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?"
    "4. Po książki w jakiej formie sięgasz najczęściej? ",
    "5. Ile książek czytasz średnio w ciągu roku?",
    "6.Jak często średnio czytasz książki? ",
    "7. Po jakie gatunki książek sięgasz najczęściej?"
]
listOfAnswers = [
    ["a. oglądanie telewizji/filmów/seriali", "b. słuchanie muzyki", "c.inne, jakie?"],
    ["a. podczas podróży", "b. podczas pracy/nauki (to ich element)", "c. inne, jakie?"],
    ["a. chęć poszerzenia wiedzy", "b. fakt, że czytanie jest modne", "c. inny, jaki?"],
    ["a. papierowej (tradycyjnej)", "b. e-booki na tablecie/telefonie",
     "c. e-booki na specjalnym czytniku (np. Kindle)"],
    ["a. codziennie", "b. żadnej w całości - jedynie fragmenty", "c. powyżej 10"],
    ["a. codziennie", "b. raz na kilka miesięcy", "c. wcale"],
    ["a. horrory", "b. naukowe", "c. poezję"],

]
listOfAnswersInput = []

for i in range(0, 6):
    print(listOfQuestions[i])
    for j in range(0, 3):
        print(listOfAnswers[i][j])

    userAnwswer = input("Odpowiedz: ")

    if userAnwswer == "a":
        temp = 0
        listOfAnswersInput.append(listOfAnswers[i][temp])
    if userAnwswer == "b":
        temp = 1
        listOfAnswersInput.append(listOfAnswers[i][temp])
    if userAnwswer == "c":
        temp = 2
        if i <= 2:
            whatC = input("Opisz: ")
            whatC = "c. " + whatC
            listOfAnswersInput.append(whatC)
        else:
            listOfAnswersInput.append(listOfAnswers[i][temp])


name = input("Podaj imie i nazwisko:\n")
listOfAnswersInput.append(name)

for i in range(0, 7):
    print(i + 1, ".", listOfAnswersInput[i])