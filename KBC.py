from KBC1 import Questions, Answers


def game():
    i = 0
    Q = 0
    Rs = 0
    while i < 27:
        i = i + 1
        print(Questions[Q])
        Ans = str(input("Enter Your Option!"))
        if Ans == Answers[Q]:
            if Rs == 0:
                Rs = Rs + 5000

            else:
                Rs = Rs * 5
            print("It's the right answer!Your current amount is", Rs, "Rs")

        else:
            if Rs == 0:
                print("It's the wrong answer!You have won nothing!")
                Restart()
                break


            else:
                print("It's the wrong answer!You have won", Rs, "Rs")
                Restart()
                break

        Q = Q + 1


def Restart():
    print("Do want to play again?(y/N)")
    Replay = input()

    if Replay == "y" or Replay == "Y":
        game()


game()