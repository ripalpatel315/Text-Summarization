# importing libraries 
import nltk 
nltk.download('punkt')
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 
   
# Input text - to summarize  
text = """The information provided herein is stated to be truthful and consistent, in that any liability, in
terms of inattention or otherwise, by any usage or abuse of any policies, processes, or directions
contained within is the solitary and utter responsibility of the recipient reader. Under no
circumstances will any legal responsibility or blame be held against the publisher for any
reparation, damages, or monetary loss due to the information herein, either directly or indirectly.
Respective authors own all copyrights not held by the publisher. The information herein is offered for informational purposes solely, and is universal as so. The presentation of the information is without contract or any type of guarantee assurance. The trademarks that are used are without any consent, and the publication of the trademark is without permission or backing by the trademark owner. All trademarks and brands within this book are for clarifying purposes only and are the owned by the owners themselves, not affiliated with this document"""
   
# Tokenizing the text 
stopWords = set(stopwords.words("english")) 
words = word_tokenize(text) 
   
# Creating a frequency table to keep the  
# score of each word 
   
freqTable = dict() 
for word in words: 
    word = word.lower() 
    if word in stopWords: 
        continue
    if word in freqTable: 
        freqTable[word] += 1
    else: 
        freqTable[word] = 1
   
# Creating a dictionary to keep the score 
# of each sentence 
sentences = sent_tokenize(text) 
sentenceValue = dict() 
   
for sentence in sentences: 
    for word, freq in freqTable.items(): 
        if word in sentence.lower(): 
            if sentence in sentenceValue: 
                sentenceValue[sentence] += freq 
            else: 
                sentenceValue[sentence] = freq 
   
   
   
sumValues = 0
for sentence in sentenceValue: 
    sumValues += sentenceValue[sentence] 
   
# Average value of a sentence from the original text 
   
average = int(sumValues / len(sentenceValue)) 
   
# Storing sentences into our summary. 
summary = '' 
for sentence in sentences: 
    if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)): 
        summary += " " + sentence 
print(summary) 
