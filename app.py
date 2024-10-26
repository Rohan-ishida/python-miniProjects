import random

deposite_amt=0

def deposite():
    global deposite_amt
    deposite_amt=int(input("Enter ammout which you want to add to your wallet $"))
    print("\n")
    print(f"Your balence is {deposite_amt}$")
    bet()

def continuation():
    continue_confirmation=input("enter\n1-continue\n2-exit :")
    while True:
        if continue_confirmation=='1':
            bet()
        elif continue_confirmation=='2':
            break
    

def bet():
    global deposite_amt
    dice_no=['1','2','3','4','5','6']

    while True:
       bet_ammt=int(input("Enter money you want to bet $"))
       if bet_ammt<deposite_amt:
           break
       else:
           bet_ammt=int(input("Enter money you want to bet $")) 

    while True:
      bet_no=input("Enter no you want to bet on (1-6) : ")
      if bet_no in dice_no:
          break
      else:
         bet_no=int(input("Enter no you want to bet on (1-6) : ")) 

    bet_excute=random.randrange(1, 6)
    if bet_excute == int(bet_no):
        print("\nYou won :$",bet_ammt*2)
    else:
        deposite_amt=deposite_amt-bet_ammt
        print(f"\nwinning number was :{bet_excute}")
        print(f"You lost :( avilable balence ${deposite_amt}")

    continuation()



def main():
    name=input("Enter your name ")
    print(f"Hello,Welcome to Shalimaar casiono {name} :) \n")
    deposite()

main()
