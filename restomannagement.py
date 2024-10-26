name=input("\nWhat is your name = ")

print(f"\nWelcome to Python Resturent {name}\n")

print("========Menue========\n")
print("pizza----200\npasta----120\ntea-------20\ncofee-----80\nmomo------60\n")
print("=====================\n")


menue={
    'pizza':200,
    'pasta':120,
    'tea':20,
    'cofee':80,
    'momo':60, 
      }
tot=0

def order():
    global tot
    food=input("enter a food to buy = ")
    if food in menue:
          tot=tot+menue[food]
          print(f"{food} has been added to cart\n")
          print(f"{food} x 1=",menue[food])  
    else:
          print(f"{food} is not avilable in our resturent ")
    respo()
    

def respo():
    response=input("Do you want to order somthing else(Yes/No)")
    if response == "Yes":
      order()
    else:
      print("=====Bill=====\n")
      res=tot
      print(f"Total = ₹{res}") 

order()

