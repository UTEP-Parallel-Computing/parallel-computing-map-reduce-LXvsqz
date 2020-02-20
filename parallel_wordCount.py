import re
import pymp





wordDict = pymp.shared.dict()


wordKey = ['hate', 'love', 'death', 'night', 'sleep', 'time', 'henry', 'hamlet', 'you', 'my', 'blood', 'poison', 'macbeth', 'king', 'heart', 'honest' ]


testList = list()

i = 1
list_of_files = list()

file1_words= list()
file2_words = list()
file3_words = list()
file4_words = list()
file5_words = list()
file6_words = list()
file7_words = list()
file8_words = list()

list_of_wordLists = [file1_words,file2_words,file3_words,file4_words,file5_words,file6_words,file7_words,file8_words]


for j in range(1,9):
    file = "shakespeare" + str(j) + ".txt"
    list_of_files.append(file)


def wordOccurance(fileList, fileName):
    text_file = open(fileName, "r")  # read mode
    
    
    for line in text_file: # for every line in file
        
        line = line.strip() 
        line = re.sub(r'[^\w\s]','', line) # remove punctuation
        
        
        line = line.casefold() # make everything lowercase
        words = line.split(" ") # split  by empty string
        #print(words)

        for word in words:#for each word in list of words
            if word in wordKey:
                fileList.append(word)
               
#---------------------------------------------------------------------__---------------##

with pymp.Parallel(1) as p:
    
    # append words to dictionary
    #populateDictionary(wordDict2)
    sumLock = p.lock

    for file in p.iterate(list_of_files): 
        text_file = open(file, "r")  # read mode
        for i in range(0,8):
        
            wordOccurance(list_of_wordLists[i], file)
            
            
        


#---------------------------------------------------------------------__---------------##
print(file2_words)

#wordOccurance(f1_list, "shakespeare1.txt")    
#print(f1_list)
    
#print(wordDict)
