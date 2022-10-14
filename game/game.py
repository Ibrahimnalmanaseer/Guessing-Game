from os import name
from  random import randint
from unittest import result

print('''#####  Hi! welcome to Guessing Game   ##### ''')


player_1=input("Player 1 : Please Enter Your Name ==> ")




class Game :

    result={}
    
    def __init__(self,player):

        self.player=player
        self.number=randint(1,20)
    
    def guess_number(self):
                                                                                                                               
        


            count=5
            scores=[0,2,4,6,8,10]

            while count > 0 :

                guessed_number=int(input(f'Dear {self.player} enter your guess'))
            
                if guessed_number == self.number:

                    Game.result[self.player]=scores[count]
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
                        Game.result[self.player]=scores[count][0]
                    else:
                        print(f'your guess too low ,{count} rounds left')

         


    def display_score(self):

        for i in Game.result:

            print(f'{i} : {Game.result[i]}' )

       








class Player(Game) :

    def __init__(self,player) -> None:
        super().__init__(player)
        self.player=player






        


kkkk=Player(player_1)
print(kkkk.number)
kkkk.guess_number()



print(Player(player_1).display_score())

