#File: FileHandling.py
#Christian Naclerio

#imported modules
import HelperModule as HM
import time as T
import datetime as DT
import random
import os
import pathlib
import numpy 
import scipy

path="./files/"

def GetFileName():
    milli=str(T.time()*1000)
    fName="File_" + milli + ".txt"
    return fName


def CheckDir():
    doesExist= os.path.exists(path)
    if doesExist==False:
        os.mkdir(path)


def GetRandomNumbers(howMany):
    nums=[]
    for n in range(howMany):
        nums.append(random.randint(1,10000))
    return nums

def GetFile():
    CheckDir()
    fList=os.listdir(path)
    if len(fList)>0:
        fMenu="\nChoose a file to open:\n"
        pos = 1
        for file in fList:
            fMenu += f"{pos}) {file}\n"
            pos+=1
        fMenu += f"{pos}) Exit back to main menu\n"
        fMenu += "Please choose a file to open: "
        choice=0
        while choice<1 or choice>len(fList) + 1:
            choice= HM.GetInt(fMenu)
            if choice<1 or choice>len(fList) + 1:
                print("That is not a valid selection. Please try again!!!")
            elif choice==len(fList) + 1:
                #To exit
                pass
            else:
                #open file to read
                f=open(path + fList[choice-1], "r")
                nums=[]
                lines=f.readlines()
                for num in lines:
                    nums.append(int(num))
                    print(num)
            
    

def AddNumbers():
    fileName=GetFileName()
    amt=0
    while amt<2 or amt>1000:
        amt=HM.GetInt("How many numbers would you like (2-1000)?: ")
        if amt< 2 or amt > 1000:
            print("has to be between 2 and 1000!!!")
    numbers=GetRandomNumbers(amt)
    numbers.sort()
    CheckDir()
    f=open(path + fileName, "w")
    for num in numbers:
        f.write(str(num) + "\n")
    f.close()




menu = "******************************************************************\n"
menu += " File handling\n"
menu +="******************************************************************\n"
menu += "1) Add a file of numbers\n"
menu += "2) Read a file of numbers, calculate stuff\n"
menu += "3) Exit out\n"
menu += "Enter a menu selection: "

keepGoing = True

while keepGoing==True:
    choice=HM.GetInt(menu)
    if choice==1:
        AddNumbers()
    elif choice==2:
        GetFile()
    elif choice==3:
        keepGoing=False
        print("Okay, have a nice day!!!")
        HM.ClickEnter()
    else:
        print("Not a valid selection. Please try again!!!")
