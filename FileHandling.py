#                     Openfile                         #
#myFile = open(r"D:\Python Basics\mostafa.txt","a")

#Moods:
#[1] "r" ---> Read (Error if not exist)
#[2] "a" ---> Append values (Create file if not exist)
#[3] "w" ---> Writing (Create file if not exist)
#[4] "x" ---> create file (Error if exist)
#------------------------------------------------------#
#                    Read file                         #

#print(myFile) #---> Print info about file object

#print(myFile.read()) #---> read all file
#print(myFile.read(5)) #---> first 5 char of the file

#print(myFile.readline())  #---> frist line
#print(myFile.readline(3)) #---> frist 3 char of the next line
#print(myFile.readline())  #---> complete the line

#print(myFile.readlines()) #---> read all lines as a list
#print(myFile.readlines(5)) #---> Maximum bytes
#-------------------------------------------------------#
#                         Write                         #

#myFile.write("Hello sasa") #---> delete all file content and write
#L = ["Mostafa\n","Mohamed\n","Ragab\n"]
#myFile.writelines(L) #---> delete all file content and Write a list

#                   write ( append mode )               #
#myFile.write("Good morning\n") #---> add this text on the same content
#-------------------------------------------------------#
#                  Addition info (Append mode)          #
#myFile.truncate(5) #---> keep first 5 chars and delete the rest
#myFile.tell() #---> position of cursor
#myFile.seek(6) #---> move cursor to this position
#myFile.close() #---> close the file
#import os 
#os.remove(r"D:\Python Basics\mostafa.txt") #---> remove the file
