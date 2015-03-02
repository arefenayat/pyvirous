import os
def into(i,j=None):
    f=os.listdir(i)
    os.chdir(i)
    for i2 in f:
        if i2!='file.py':
            if os.path.isfile(i2)==True:
                os.remove(i2)

    for i3 in f:
        if i3!='file.py':
            if os.path.isdir(i3)==True:
                into(i3,j='x')
    if j=='x':
        os.chdir('..')
        os.rmdir(i)                
into('.')
 
