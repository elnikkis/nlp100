# coding: utf-8

s = 'I am an NLPer'

def ngram(seq):
    '''bi-gram'''
    ret = []
    for i in range(len(seq) - 1):
        ret.append((seq[i], seq[i+1]))
    ret.append((seq[len(seq)-1], ''))
    return ret

if __name__ == '__main__':
    w_bi = ngram(s.split())
    print(w_bi)

    c_bi = ngram(s.replace(' ', ''))
    print(c_bi)
