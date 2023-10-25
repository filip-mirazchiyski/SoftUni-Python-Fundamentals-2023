count_of_words = int(input())
word = input()
list_of_words = []

for i in range(count_of_words):
    current_word = input()
    list_of_words.append(current_word)
print(list_of_words)

for i in range(len(list_of_words) - 1, -1, -1):
    element = list_of_words[i]
    if word not in element:
        list_of_words.remove(element)
print(list_of_words)