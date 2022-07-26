# 2. Напишите функцию, которая проверяет: является ли слово палиндромом
def palindrom(word):
    word = word.lower()
    for i in range(int((len(word)/2)+1)):
        if word[i-1] != word[-i]:
            return False
    return True
print(palindrom("шалаш"))
print(palindrom(input("word for palindrom: ?")))
