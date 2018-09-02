def palindrome(word):
    if word == word[::-1]:
        return True
    return False

if __name__ == '__main__':
    word  = str(input('Escribe una palabra: '))

    result = palindrome(word)

    if result is True:
        print('{} sí es un palindrome'.format(word))
    else:
        print('{} no es un palindrome'.format(word))
