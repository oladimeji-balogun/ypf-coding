

def take_input(): 
    age = input("enter your age here: ")

    try: 
        age = int(age)
        print("yes, this age is valid.")
    except Exception as e: 
        print("invalid age, must be a string.")
        print(e)
        take_input()
    
    

    
take_input()
    