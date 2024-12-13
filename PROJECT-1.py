import random 
user_choice=int(input("enter ur choice : 0 rep rock , 1 rep paper, 2 rep scissors")    )
print(user_choice)

computer_choice=random.randint(0,2)
print(computer_choice) 

if(user_choice==computer_choice):
    print("tie")
elif(user_choice==0 and computer_choice==1):
    print("computer wins") 
elif(user_choice==1 and computer_choice==2):
    print("user wins")
elif(user_choice==2 and computer_choice==0):
    print("user wins")   
else:
    winner='computer' 
    print("winner") 


