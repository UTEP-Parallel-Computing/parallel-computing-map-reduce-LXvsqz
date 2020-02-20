import re
import pymp
import time

wordKey = ['hate', 'love', 'death', 'night', 'sleep', 'time', 'henry', 'hamlet', 'you', 'my', 'blood', 'poison', 'macbeth', 'king', 'heart', 'honest' ] # key of words to look for

list_of_files = list() # list holding each file


for j in range(1,9): # poulate list holding files
    file = "shakespeare" + str(j) + ".txt"
    list_of_files.append(file)


#-------------------------------------------------------------------------------------##

def parallelWC():
    
    wc = pymp.shared.dict()

    start_time = time.time()
    with pymp.Parallel(8) as p:
        
        finalRT = int()
        finalWC = int()  #FIGURING OUT TIME
        wordTime = int()
        startReadTime = int()
        
        sumLock = p.lock
    
        for word in wordKey: # for every word in key, initialize that word in dictionary to 0
            wc[word] = 0
        
        for file in p.iterate(list_of_files): # for each file, do this
            
            #file_read_time = time.time()
            
            text_file = open(file, "r")  #read mode
            
            startReadTime = time.time()
            
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
                        
                        
        finalRT = time.time() - startReadTime
    total_time = time.time() - start_time
    
    print("Total Operation time: " , total_time)
    #print("Word Count time: " , finalWC)
    print("File Reading time: " , finalRT)
    print(wc)
#------------------------------------------------------------------------------------#

parallelWC()


