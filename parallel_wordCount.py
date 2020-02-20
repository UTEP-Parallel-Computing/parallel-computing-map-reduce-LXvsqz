import re
import pymp


wordKey = ['hate', 'love', 'death', 'night', 'sleep', 'time', 'henry', 'hamlet', 'you', 'my', 'blood', 'poison', 'macbeth', 'king', 'heart', 'honest' ] # key of words to look for

list_of_files = list() # list holding each file

#each list will hold contents from each unique file 

file1_words = list()
file2_words = list()
file3_words = list()
file4_words = list()
file5_words = list()
file6_words = list()
file7_words = list()
file8_words = list()

list_of_wordLists = [file1_words,file2_words,file3_words,file4_words,file5_words,file6_words,file7_words,file8_words]


for j in range(1,9): # poulate list holding files
    file = "shakespeare" + str(j) + ".txt"
    list_of_files.append(file)


#-------------------------------------------------------------------------------------##

def parallelWC():
    wc = pymp.shared.dict()


    with pymp.Parallel(1) as p:
        
        sumLock = p.lock
    
        for word in wordKey: # for every word in key, initialize that word in dictionary to 0
            wc[word] = 0
        
        
        for file in p.iterate(list_of_files): # for each file, do this
            
            text_file = open(file, "r")  #read mode
        
            for line in text_file: # for every line in file. Note doing it this way instead of using re library so i can look for every word in each file
            
                line = line.strip() 
                line = re.sub(r'[^\w\s]','', line) # remove punctuation
            
            
                line = line.casefold() # make everything lowercase
                words = line.split(" ") # split  by empty string
               
               
                for word in words: #for each word in list of words
                    if word in wordKey:
                        sumLock.acquire() # lock any other thread from accessing shared dictionary
                        wc[word] += 1
                        sumLock.release() # release lock when done
                        
    print(wc)
        
#------------------------------------------------------------------------------------#

parallelWC()


