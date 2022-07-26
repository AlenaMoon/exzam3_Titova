# 2. Напишите функцию, которая проверяет: является ли слово палиндромом
def palindrom(word):
    word = word.lower()
    for i in range(int((len(word)/2)+1)):
        if word[i-1] != word[-i]:
            return False
    return True
print(palindrom("шалаш"))
print(palindrom(input("word for palindrom: ?")))

def palindrom(word):
    word=word.lower()
    if len(word)<= 1:
        return True
    if word[0] != word[-1]:
        return False
    else:
        return palindrom(word[1:-1])
print(palindrom(input("word for palindrom: ?")))
#                 # word for palindrom: ?  ASDdsa
