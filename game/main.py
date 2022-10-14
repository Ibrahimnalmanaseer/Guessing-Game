x=True

from game.game import Game



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


