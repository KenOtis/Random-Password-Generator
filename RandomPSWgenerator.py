import random
import string



def PSWgen():
  #Gather the info 
    Site=input("What is Site do you need the password for? ")
    Username=input("What is the username? ")
    PSWlen=int(input("How long do you want the password to be? "))
    SpecialChar=input("Would you like to include special characters? (y/n) ")
  #Set the chars 
    lower=string.ascii_lowercase
    upper=string.ascii_uppercase
    num=string.digits
    symbols=string.punctuation

    #add the numbers and letters 
    all= lower + upper + num 

    #if special chars is wanted, this will execute
    if SpecialChar == 'y':
       all+= symbols

    #Setting the temporary password 
    temp = random.sample(all,PSWlen)

    #adding the characters to the password 
    PSWD= "".join(temp)

    #printing the password 
    print (PSWD)

     
  

PSWgen()
