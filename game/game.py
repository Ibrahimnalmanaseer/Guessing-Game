from  random import randint

print('''#####  Hi! welcome to Guessing Game   ##### ''')


player_1=input("Player 1 : Please Enter Your Name ==> ")


[[0,2],2,4,6,8,10]





class game :


    
    def __init__(self,player_1):

        self.player_1=player_1
        self.number=randint(1,20)
    
    def guess_number(self):
        count=5
        while count > 0 :
            guessed_number=int(input(f'Dear {self.player_1} enter your guess'))
        
            if guessed_number == self.number:

                print(f'congrats ! , You win the number is {self.number}')
                count = 0 

            if guessed_number > self.number:
                

                
                count-=1
                if count == 0:
                   print ('you lose ')

                else:   
                    print(f'your guess too high ,{count} rounds left')



            if guessed_number < self.number:
                
                count-=1
                if count == 0:
                   print ('you lose ')
                else:
                    print(f'your guess too low ,{count} rounds left')
               
               

game(player_1).guess_number()     


print(result={
    

})