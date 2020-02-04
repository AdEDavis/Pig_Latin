# CREATE A SCRIPT WHICH CONVERTS TEXT TO PIG LATIN
'''
RULES:
In words that begin with consonant sounds,
the initial consonant or consonant cluster is moved to the end of the word,
and "ay" is added, as in the following examples:
beast ? east-bay
dough ? ough-day
happy ? appy-hay
question ? estion-quay
In words that begin with vowel sounds or silent consonants,
the syllable "way" is simply added to the end of the word.
In some variants, the syllable "ay" is added, without the "w" in front.
Sometimes the vowel will be moved and followed by the syllable "hay".
another? another-way or another-ay
if? if-way or if-ay

In compound words or words with two distinct syllables,
each component word or syllable is sometimes transcribed separately.
For example: birdhouse would be ird-bay-ouse-hay.


string_cont[index]
string_no_hyphen[index]
'''

user_input = input('> ')
#user_input = user_input.split(' ')

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
