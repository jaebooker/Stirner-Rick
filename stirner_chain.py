import random

def markdown2(word_list, sentence_length):
    chain = []
    random_number = random.randrange(0,len(word_list))
    random_next_word = word_list[random_number]
    chain.append(random_next_word)
    for i in range(0, sentence_length):
        next_word = markdown_double_chained(word_list, random_next_word, chain)
        if next_word:
            chain.append(next_word)
            random_next_word = next_word
        else:
            return chain
    return chain

def markdown_double_chained(word_list, random_next_word, chain):
    unchained = []
    double_unchained = []
    for i in range(1,len(word_list)):
        if random_next_word == word_list[i]:
            if i == len(word_list)-1:
                break
            unchained.append(word_list[i+1])
            double_unchained.append(word_list[i-1])
    if unchained:
        still_unchained = True
        while(still_unchained):
            random_index = random.randrange(0,len(unchained))
            if len(chain) > 1:
                if chain[len(chain)-2] == double_unchained[random_index]:
                    next_word = unchained[random_index]
                    still_unchained = False
            else:
                next_word = unchained[random_index]
                still_unchained = False
        return next_word
    else:
        return None
