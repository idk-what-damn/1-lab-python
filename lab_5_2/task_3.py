def is_palindrome(word):
    word_str = str(word).lower().replace(" ", "")
    return word_str == word_str[::-1]