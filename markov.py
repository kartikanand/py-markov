import random
import re


def get_tokens(text):
    pat = re.compile(r'[\r\n\.,\-\'"]')

    text = text.strip()
    text = re.sub(pat, ' ', text)
    text = text.lower()

    return text.split()


def markov(text):
    """ get markov dictionary  """
    tokens = get_tokens(text)

    d = {}
    for i in range(len(tokens)-2):
        key = tokens[i] + ' ' + tokens[i+1]
        d[key] = tokens[i+2]

    return d

def get_random_sentence(d):

    sentence = ''

    key = random.choice(list(d.keys()))
    sentence += key

    nxt = d.get(key, None)

    while nxt:
        sentence = sentence + ' ' + nxt
        key = ' '.join(sentence.rsplit(None, 2)[-2:])

        nxt = d.get(key, None)

    return sentence

s = input()
d = markov(s)

print(get_random_sentence(d))

