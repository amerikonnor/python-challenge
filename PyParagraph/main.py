import os
import re

textpath = os.path.join("test.txt")


#opens the text file and saves the content to data
with open(textpath , 'r', encoding='utf-8') as text:
    data = text.read()


#split on spaces to get words
words = data.split()
word_count = len(words)

#count letters to get average letters in a word
letters = 0
for word in words:
    letters += len(word)

average_letters = letters/word_count

#split on periods to approximate sentences
sentences = data.split(".")
sentence_count = len(sentences)


#split using more characters to get actual number of sentences
re_sentences = re.split("(?<=[.!?]) +", data)





#print(f'Approximate Word Count: {word_count}')
#print(f'Approximate Sentence Count: {sentence_count}')
#print(f'Average Letter Count: {average_letters:.1f}')
