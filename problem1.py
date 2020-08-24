
def rev_word(sentence):
    words = sentence.split(' ')
    rev_sentence = ' '.join(reversed(words))
    return rev_sentence


if __name__ == "__main__":
    word = 'Hello World'[::-1]
print (rev_word(word))