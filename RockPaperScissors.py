import random

lives = 5
score = 0
a = ['rock', 'paper', 'scissors']

def HighScore(update):
    scornum = []
    scorupdt = []
    scores = []
    with open('HighScore.txt', 'r') as file:
        for line in file:
            line = line.strip()
            array = line.split('.')
            arrayint = int(array[1])
            scores.append(arrayint)
            scornum.append(array[0])
        for i in scores:
            score = i
            if update > score:
                scores[len(scores) - 1] = update
                print('You got a new highscore!')
                break
        scores.sort()
        for j in scores:
            j = str(j)
            scorupdt.append(j)
    with open('HighScore.txt', 'w') as file2:
        for k in range(len(scores)):
            file2.write(scornum[k] + '.\t' + scorupdt[-k-1] + '\n')
def HighScores():
    with open ('HighScore.txt', 'r') as highScOut:
        for i in highScOut:
            print(i, end = '')
while lives > 0:
    x = random.randint(0,2)
    choice = input('Please choose Rock, Paper or Scissors:').lower()
    if a[x] == 'scissors':
        if choice == 'rock':
            print('I choose Scissors. You win!')
            score += 1
            print('You have', lives, 'lives left.')
        if choice == 'paper':
            print('I choose Scissors. You Lose!')
            lives -= 1
            score += 1
            print('You have', lives, 'lives left.')
        if choice == 'scissors':
            print("I choose Scissors. It's a draw!")
            score += 1
            print('You have', lives, 'lives left.')

    elif a[x] == 'rock':
        if choice == 'rock':
            print("I choose Rock. It's a draw!")
            score += 1
            print('You have', lives, 'lives left.')
        if choice == 'paper':
            print('I choose Rock. You Win!')
            score += 1
            print('You have', lives, 'lives left.')
        if choice == 'scissors':
            print("I choose Rock. You lose!")
            lives -= 1
            score += 1
            print('You have', lives, 'lives left.')

    elif a[x] == 'paper':        
        if choice == 'scissors':
            print('I choose Paper. You win!')
            score += 1
            print('You have', lives, 'lives left.')
        if choice == 'rock':
            print('I choose Paper. You Lose!')
            lives -= 1
            score += 1
            print('You have', lives, 'lives left.')
        if choice == 'paper':
            print("I choose Paper. It's a draw!")
            score += 1
            print('You have', lives, 'lives left.')
    else:
        print('That is not a valid answer. Please try again.')
HighScore(score)
print('You have lost all your lives. I win!')
print('You survived', score, 'rounds.\nEnter x to see high scores or enter to quit!')
see = input().lower()
if see == 'x':
    HighScores()
else:
    quit()

    
    
