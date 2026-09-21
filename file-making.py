import os
import csv

while True:
    option = int(input("Choose an Option \n1)Create a file\n2)Write file\n3)Read file\n4)Delete file \n5)Exit\nOption : "))

    if(option == 1):
        name = input("Enter your File name :- ")
        fp = open(name,"x")
        if fp:
            print("File created Sucessfully!")
        else:
            print("There was an error in file!")
        fp.close()

    if option == 2:
        f_name = input("Enter your file name :-") 
        if f_name:
           data = input("Enter what you want to write :-")
           w = open(f_name,"w")
           w.writelines(f"{data}")
           w.close()

    if option == 3:
        f_name = input("Enter your file name :-")
        w = open(f_name,"r")
        print(w.readline())
        w.close()
    if option == 4:
        name = input("Enter your File name to delete :- ")
        os.remove(f"{name}")
        print("File deleted sucessfully!!")
    if option == 5:
        print("Exited Sucessfully!!")
        break