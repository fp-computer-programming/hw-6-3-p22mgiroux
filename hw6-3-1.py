# Author: MOG 11/15/21

word1 = input("Please input your first word: ")
word2 = input("Please input your first word: ")

list1 = list(word1)
list2 = list(word2)

if list1.sort() == list2.sort():
    print("{} and {} are anagrams.".format(word1, word2))
else:
    print("{} and {} are not anagrams.".format(word1, word2))
