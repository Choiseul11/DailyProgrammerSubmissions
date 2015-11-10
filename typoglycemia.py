import random

with open("input.txt","r") as txt:
    text = txt.read()
words = text.split()
scrambled = []

for word in words:
    if word[-3:] == "...":
        end = -3
    elif word[-1] in [",",".","!",";","?","\n"]:
        end = -2
    else:
        end = -1
    if len(word) > 3:
        scrambled.append(word[0]+''.join(random.sample(word[1:end],len(word)-1+end))+word[end:])
    else:
        scrambled.append(word)

print " ".join(scrambled)
