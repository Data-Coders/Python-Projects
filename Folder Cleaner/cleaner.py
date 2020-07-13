# Importing nessessary modules
import os
import shutil

# defining a Function to move the files to Folder accourding to the extension


def move(filename, foldername):
    # making a try and except to move the file to the folder named with the extension of the filename
    try:
        shutil.move(filename, foldername)
    except shutil.Error as e:
        pass

# defining a function to extract the extension and make a folder named as the Extension


def folder(filename):
    # making variable that helped to extract the extension of the filename
    a = 0
    ext = ""

    # iterating the filename letter by letter to get the extension of the filename
    for k in filename:
        # checking if the filename consist of the "." charecter
        if(a == 0):
            # if the "." charecter is found in the filename the make the variable name "a" to 0
            if(k == "."):
                a = 1
            # if not found then continue
            else:
                continue
        # if value of "a" is 0 then add the charecter to get the file extension
        if (a == 1):
            ext += k

    # try to make the folder if already exist then throw a error
    try:
        os.makedirs(ext)
    # making a except block to catch the error and make the program to run even when the error occurs
    except FileExistsError as e:
        pass
    # calling the move function to move the file to the folder named with its extension
    move(filename, ext)


# getting the file name from the current working Directory
files = os.listdir()

# removing the file name of this Python File
files.remove('cleaner.py')

# iterating the files variable for getting the file names seperatly
for i in files:
    # making a try and except block for passing the file names to Extract the extension of the file and move it to the folder
    try:
        # passing the file name to work on the further process
        folder(i)
    # making the except block to stop breaking down the funtion
    except IndexError as e:
        pass
