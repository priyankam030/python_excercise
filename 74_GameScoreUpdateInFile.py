import random

def game():
    score = random.randint(1, 100)
    print(f"Your score is: {score}")

    hiScoreFile = open("hiscore.txt", "r")
    hiScore = hiScoreFile.read()
    hiScoreFile.close()
    
    if(hiScore != ""):
        hiScore = int(hiScore)
    else:
        print("There is no high score")
        hiScore = 0

    if(score > hiScore):
        hiScoreFile = open("hiscore.txt", "w")
        hiScoreFile.write(str(score))
        hiScoreFile.close()
        print(f"Highest score is: {score}")
    else:
        print(f"Highest score is: {hiScore}")

    return score


game()

