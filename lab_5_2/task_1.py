def count_words(sentence):
    if not sentence or not sentence.strip():
        return 0
    return len(sentence.split())