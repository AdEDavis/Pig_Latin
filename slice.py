''' This helped me format the .txt files (comp.txt and compound_words.txt)'''
from sys import argv
script, filename = argv #takes argument for a file in the terminal

def slice():
    ''' replaces all tabs with newlines in a given file'''
    with open(filename, 'r+') as file:
      filedata = file.read()
    filedata = filedata.replace('\t','\n')
    with open(filename, 'w') as file:
      file.write(filedata)

def slice_space():
    ''' replaces all spaces in file with no-white-space '''
    with open(filename, 'r+') as file:
      filedata = file.read()
    filedata = filedata.replace(' ','')
    with open(filename, 'w') as file:
      file.write(filedata)

#slice()
#slice_space()

def duplicate():
    '''checks for duplicates within a file
       and prints the duplicates'''
    file = open(filename, 'r+')
    string = str(file.read())
    words = string.split('\n')
    seen = set()
    dups = set()
    for word in words:
        if word in seen:
            if word not in dups:
                print(word)
                dups.add(word)
        else:
            seen.add(word)

#duplicate()
