task_list=[]
no_task=int(input("\nhow many task u want to complete today = \n"))
n=1
for i in range(0,no_task):
    task=input("enter your task = ")
    task_list.append(task)
    print(f"{task} has been updated as {n}th task\n")
    n+=1
print("\n",task_list,"\n")

while True:
   print("1-add\n2-delete\n3-view\n4-update\n5-exit\n")
   choice=input("enter a valid choice =")
   if choice=='1':
      task=input("new task?? ")
      task_list.append(task)
      print(f"{task_list}, has been added to list..")
   elif choice=='2':
      dele=input("what u want to delete from task list :")
      if dele in task_list:
         task_list.remove(dele)
         print(task_list)
      else:
        print(f"{dele},task is not in to do list :(")
   elif choice=='3':
      print(task_list,"\n")
   elif choice=='4':
      up=input("enter what you want to update :")
      up_index=task_list.index(up)
      if up in task_list:
        exc=input("what u want to replace with : ")
        task_list[up_index]=exc
        print("\n",task_list)
      else:
        print("task not found :(")
   elif choice=='5':
      break
   else:
    print("wrong input..")