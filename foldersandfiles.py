import os

print(os.getcwd()) # the correbt working dir
print(os.listdir()) # show all the folders and files
os.chdir(r'D:\test1') # change the dir
print(os.getcwd())
os.makedirs("danny\\Dan") # makedirs to make more than one folder


# הגדירו תיקיה חדשה בשולחן העבודה בעזרת פייטון ובתוך התיקייה נא ליצור 3 תיקיות בפקודה אחת
# תוסיפו לאותה תיקיה את הפונקציה MKDIR עם EXCEPTION HANDLER


def ppath():
    print(os.getcwd())

os.chdir(r'C:\Users\hothaifa\Desktop')
ppath()
os.mkdir('osdir')
os.chdir('osdir')
ppath()
os.makedirs(r'hosney\fayek\hothaifa')
try:
    os.mkdir('hodi\\fffff')
except :
    print('=============================ERROR======================')
