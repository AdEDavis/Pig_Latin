user_input = input('> ')

def translate(user_input):
    from txt import vowels,silent_cluster as silent
    prefix = user_input[0] #ex. 'adam' --> 'a'
    prefix_clust = user_input[0:2] #'chad' --> ch
        if prefix_clust in silent:
            user_input = user_input.replace(prefix_clust, ''); user_input = "{0}-{1}ay".format(user_input,prefix_clust)
        if prefix in vowels:
            user_input = "{0}-way".format(user_input)
        if prefix not in vowels and prefix_clust not in silent:
            user_input = user_input.replace(prefix, ''); user_input = "{0}-{1}ay".format(user_input,prefix)
    print(user_input, end='')

def compound_word(user_input):
    origfile = open('compound_words.txt', 'r+') #open compound_words.txt
    file_cont = origfile.read()
    string_cont = list(file_cont.split('\n')) #converts .txt to a list

    origfile_2 = open('comp.txt','r+') #open comp.txt
    file_contents = origfile_2.read()
    string_no_hyphen = list(file_contents.split('\n')) #converts .txt to a list

    if user_input in string_no_hyphen:
        index = string_no_hyphen.index(user_input)
        index = string_cont[index]; index = index.split('-')
        a,b = index[0], index[1]
        translate(a)
        translate(b)
    else:
        translate(user_input)

compound_word(user_input)
