'''Test score program
gets the score and processes the score'''

def getScore():
    scores=[]


    while True:

        score = input("Enter the Test score  or Enter x to exit ")
        if score.lower()=='x':
            break
        else :
            if int(score) >= 0  and int(score) <= 100:
                scores.append(int(score))
            else:
                print("Please enter a valid score")

    return scores

def processScore(scoresList):
    lenScoreList= len(scoresList)
    total=0
    average =0
    if lenScoreList == 0:
        print("Please enter scores to process the marks")
    else:
        for marks in scoresList:
            total+=marks

        average = total/lenScoreList

    print("total:\t",total)
    print("average:\t",int(average))


def main():
    print("The Test scores Program")
    print("my name is ",__name__)
    scoresList=[]

    scoresList=getScore()

    print("ScoreList:", scoresList)
    scorelen= len(scoresList)
    if scorelen!=0:
        processScore(scoresList)
    else:
        print("please enter test scores")




if __name__== "__main__":
    main()








