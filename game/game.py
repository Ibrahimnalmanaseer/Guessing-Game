

from  random import randint

class Game :
    result={}
    def __init__(self,player):
        self.player=player
        self.number=randint(1,20)
        self.score = 0
    def guess_number(self):
            count=5
            scores=[0,2,4,6,8,10]
            while count > 0 :
                guessed_number=int(input(f'Dear {self.player} enter your guess'))
                if guessed_number == self.number:
                    self.score=scores[count]
                    print(f'congrats ! , You win the number is {self.number} and your score is : {scores[count]} ')
                 
                    count = 0
                if guessed_number > self.number:
                    count-=1
                    if count == 0:
                        print ('you lose ')
                        Game.result[self.player]=scores[count]
                    else:
                        print(f'your guess too high ,{count} rounds left')
                if guessed_number < self.number:
                    count-=1
                    if count == 0:
                        print ('you lose ')
                        Game.result[self.player]=scores[count]
                    else:
                        print(f'your guess too low ,{count} rounds left')

         


    def display_score(self):

        with open ('./score.txt','a') as file:
            file.write(f'\n Name : {self.player} | Score : {self.score}')

        with open ('./score.txt','r') as f:

            print(f.read())
       





    






x=True

while x :


    
    print('''#####  Hi! welcome to Guessing Game   ##### ''')

    player_1=input("Player 1 : Please Enter Your Name ==> ")
    player=Game(player_1)
    player.guess_number()
    player.display_score()

    ask=input('do you want to play again? y/n ')
    if ask == 'n':
       x=False

       print("Bye , we hope you come soon ")
       player.display_score()









