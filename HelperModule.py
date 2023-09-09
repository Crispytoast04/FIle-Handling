#File: HelperModule.py
#Chris Naclerio

def GetString(prompt):
    '''
    Get a string from the user. Prompt is what the
    user sees when they are being asked for input.
    '''
    value=""
    while value=="":
        value=input(prompt)
        if len(value)==0:
            print("Your entry cannot be empty. Please try again!!!")
    return value

def GetChar(prompt):
    '''
    Get Character from User, calls GetString.
    '''
    value=GetString(prompt)
    return value[0]

def GetLowerChar(prompt):
    '''
    Get Lowercase Character from user, calls GetChar which calls GetString
    ''' 
    value=GetChar(prompt).lower()
    return value

def GetInt(prompt):
    '''
    Get an integer from the user. Calls GetString and then attempts to
    convert it to an integer.
    ''' 
    valid=False
    value=""
    while valid==False:
        try:
            value=int(GetString(prompt))
            valid=True
        except ValueError:
            print("That is not a valid integer. Please try again!!!")
    return value

def GetFloat(prompt):
    '''
    Get's a float from the user. Calls GetString and tries to convert
    it to a float. 
    '''
    valid=False
    value=""
    while valid==False:
        try:
            value=float(GetString(prompt))
            valid=True
        except ValueError:
            print("That is not a valid float. Please try again!!!")
    return value

def ClickEnter():
    '''
    Click enter to continue function.
    '''
    input("Click enter to continue...")

if __name__=="__main__":
    val=GetString("Enter a string: ")
    print(f"{type(val)} is: {val}")
    val=GetChar("Enter a character: ")
    print(f"{type(val)} is: {val}")
    val=GetLowerChar("Enter y or n to continue: ")
    print(f"{type(val)} is: {val}")   
    val=GetInt("Enter a whole number: ")
    print(f"{type(val)} is: {val}")
    val=GetFloat("Enter a decimal number: ")
    print(f"{type(val)} is: {val}")       