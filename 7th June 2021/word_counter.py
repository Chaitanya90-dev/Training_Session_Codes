
string = input("Enter a String: ")

for char in '-.,\n':
    string = string.replace(char," ")

string = string.lower()

# print("\nString in Lower Case: \n")
# print(string)
# print("---------------------------------------------------------")

words_list = string.split()

# print(words_list)

d= {}

for word in words_list:
    if word not in d:
        d[word]=0
    d[word] += 1

print("\nWord Count\n")
print("----------------------------------------------------------------")
print(d,"\n")


word_freq = []

for key,value in d.items():
    word_freq.append((value,key))

word_freq.sort(reverse=True)

print("\nSorted Manner: \n")
print("----------------------------------------------------------------")
print(word_freq, "\n")