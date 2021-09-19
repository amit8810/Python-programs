letter = ''' Dear </NAME/>,
         you are selected
         Date : </DATE/>'''
name = input("enter your Name\n")
date = input("enter the Date\n")
letter = letter.replace("</NAME/>" , name)
letter = letter.replace("</DATE/>" , date)
print(letter)         