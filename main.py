#file handiling: navigate, rename ,move copy, remove


import os
from ui import run
from pathlib import Path
import shutil
#print(os.getcwd()) - prints the current working directory

os.chdir ('/Users/Balog David/Desktop/da')


#Path("file21").mkdir(exist_ok = True)


    #shutil.rmtree("file21") to remove files in file21
    #shutil.copy2(file,"file21") copy files to another file

    #shutil.move(file,"da") - moves files to another file

#navigate files
    #f = Path(file)    # name, ext = f.stem,f.suffix
    # splitted = name.split('-')
    # splitted = [s.strip() for s in splitted]
    # new_name = f"{splitted[3]}-{splitted[1]}-{splitted[2]}-{splitted[0]}{ext}"
    # print(file,new_name)
    # f.rename (new_name)



if __name__ == '__main__':
    run()


#todo organize the code so that it uses functions and more files
