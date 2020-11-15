import os
import re

textpath = os.path.join("Resources", "paragraph_2.txt")

text = ""
data = ""
#opens the text file and saves the content to data
with open(textpath , 'r', encoding='utf-8') as file:

    text = file.read()

#remove any extra characters, then all the empty strings this might make
lines = text.splitlines()
for line in lines:
    if len(line) == 0:
        lines.remove(line)

for line in lines:
    data = data + f' {line}'

print(text)
print(lines)
print(data)
#split on spaces to get words
words = data.split()
word_count = len(words)


#count letters to get average letters in a word
letters = 0
for word in words:
    letters += len(word)

#average_letters = letters/word_count

#split using re module
sentences = re.split("(?<=[.!?]) +", data)

sentence_count = len(sentences)



#counting words again just in case some weird happened up higher
re_total_words = 0
for sentence in sentences:
    re_words = sentence.split()
    re_total_words += len(re_words)

average_sentence_length = re_total_words/len(sentences)


#print(f'Approximate Word Count: {word_count}')
#print(f'Approximate Sentence Count: {sentence_count}')
#print(f'Average Letter Count: {average_letters:.1f}')
#print(f'Average Sentence Length: {average_sentence_length:.1f}')
