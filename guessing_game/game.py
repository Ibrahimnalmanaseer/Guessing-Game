from  random import randint

class GuessingGame :
    result={}
    def __init__(self,player):
        self.player=player
        self.number=randint(1,20)
        self.score = 0
        self.guessed_number=''
    def guess_number(self):
            count=5
            scores=[0,2,4,6,8,10]
            while count > 0 :
                

                try:
                    self.guessed_number=int(input(f'Dear {self.player} enter your guess between (1-20)  '))
                    if self.guessed_number == self.number:
                        self.score=scores[count]
                        print(f'congrats ! , You win the number is {self.number} and your score is : {scores[count]} ')
                    
                        count = 0
                    if self.guessed_number > self.number:
                        count-=1
                        if count == 0:
                            print ('you lose ')
                            
                        else:
                            print(f'your guess too high ,{count} rounds left')
                    if self.guessed_number < self.number:
                        count-=1
                        if count == 0:
                            print ('you lose ')
                            
                        else:
                            print(f'your guess too low ,{count} rounds left')
                except ValueError:
                         print('The provided value is not an integer')
                         continue

         


    def display_score(self):

        with open ('./score.txt','a') as file:
            file.write(f'\n Name : {self.player} | Score : {self.score}')

        with open ('./score.txt','r') as f:

            print(f.read())
       





    



player =GuessingGame('ehab')
print('game')
player.guessed_number=10
print(player.guess_number)










