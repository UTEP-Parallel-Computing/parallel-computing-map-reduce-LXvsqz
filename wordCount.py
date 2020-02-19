
import re




wordDict = dict()

# append words to dictionary
wordDict.update({'hate': 0})
wordDict.update({'love': 0}) #words to be looked for
wordDict.update({'death': 0})
wordDict.update({'night': 0})
wordDict.update({'sleep': 0})
wordDict.update({'time': 0})
wordDict.update({'henry': 0})
wordDict.update({'hamlet': 0})
wordDict.update({'you': 0})
wordDict.update({'my': 0})
wordDict.update({'blood': 0})
wordDict.update({'poison': 0})
wordDict.update({'macbeth': 0})
wordDict.update({'king': 0})
wordDict.update({'heart': 0})
wordDict.update({'honest': 0})


j = 1

for j in range(1,9):
    word = "shakespeare" + str(j) + ".txt"
    print(word)


i = 1


for i in range(1,9):
    file_name = "shakespeare" + str(i) + ".txt"


    text_file = open(file_name, "r")  # read mode


    for line in text_file: # for every line in file
        
        line = line.strip() 
        line = re.sub(r'[^\w\s]','', line) # remove punctuation
        
        
        line = line.casefold() # make everything lowercase
        words = line.split(" ") # split  by empty string
        

        for word in words: #for each word in list of words
            if word in wordDict:
                wordDict[word] +=1 
    
    
    
print(wordDict)
