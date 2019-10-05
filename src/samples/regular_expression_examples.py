import re



def using_regex(word, sentence):
    for match in re.finditer(word, sentence):
        print("match found from {} to {}".format(match.start(), match.end()))


def using_str_index(word, sentence):
    index = 0;
    while index < len(sentence):
        index = sentence.find(word, index)
        if index == -1:
            break
        print('{} found at {}'.format(word, index))
        index += len(word) 

def using_comprehension(word, sentence):
    print([n for n in range(len(sentence)) if sentence.find(word, n) == n])

if __name__ == '__main__':    
    sentence = "This is a sample sentence to search for include help to search all occurrences"
    word = "to"
    #using_regex(word, sentence)
    #using_str_index(word, sentence)
    using_comprehension(word, sentence)