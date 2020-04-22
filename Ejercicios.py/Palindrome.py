def palindrome(word):
  word.lower()
  reverse_word = word[::-1]
  if reverse_word == word:
    return True
  else:
    return False  


def run():
    word = str(input("Introduce the word to check if is palindrome or not: "))
    word.lower()

    result = palindrome(word)

    if result:
      print("{} es palindromo".format(word))
    else:
      print("{} no es palindromo".format(word))    

if __name__ == '__main__':
    run()