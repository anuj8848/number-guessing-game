from random import randint as rd
import matplotlib.pyplot as plt

print('Number Guess Game')
points_database=[]
total_counts=[]
accuracy_chart=[]

while True:
    count=0
    points=0
    requiredNumber=rd(0,10)
    while True:
        guessedNum=int(input('guess a number: '))
        count=count+1
        if guessedNum==requiredNumber:
            print('congratulation!! you guessed right.')
            points=points+1
            points_database.append(points)
            total_counts.append(count)
            break
        else:
            print('Try again!!!\n')
    print('you want to play it again(y/n)')
    playAgain=input()
    if playAgain=='n':
        print("total points: "+str(points))
        break
    elif playAgain=='y':
        continue


print(points_database)
print(total_counts)
for i in range(len(total_counts)):
    accuracy=points_database[i]/total_counts[i]
    accuracy_chart.append(accuracy)

plt.bar(total_counts,accuracy_chart)

plt.show()
