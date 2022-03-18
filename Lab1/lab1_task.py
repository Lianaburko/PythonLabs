    #сколько раз повторяется каждое слово в указанном тексте  - amount_of_diff_words
    #среднее количество слов в предложении 
    #медианное количество слов в предложении 
    #top-K самых часто повторяющихся буквенных N-грам 
    #(K и N имеют значения по-умолчанию 10 и 4, но должна быть возможность задавать их с клавиатуры).

import constants
from audioop import reverse


def words_in_text(text): #list of all words in sentence
    i = 0
    lst = []
    while i < len(text):
        name = ''
        while (i < len(text) and text[i] != ' ' and text[i] not in constants.punctuation):
            name = name + text[i]
            i = i + 1
        if (name != ' ' and name != ''):
            lst.append(name)
        i = i + 1  

    return lst


def different_words(lst): #list of different words in the sentance
    words = set()
    for name in lst:
        words.add(name)

    return words


def amount_of_diff_words(lst): # amount of each word in the sentence
    dict = {}
    for name in lst:
        if name not in dict.keys():
            dict[name] = 1
        else:
            dict[name] += 1

    return dict


def amount_of_words_in_sentences(text): # amount of words in each sentence
    for i in constants.exclusion:
        text = text.replace(i,' ') 
    
    i = 0
    sent_lst = []
    sent_words = 0
    while i < len(text):
        name = ''
        while (i < len(text) and text[i] != ' ' and text[i] not in constants.punctuation):
            name = name + text[i]
            i = i + 1
        if (name != ' ' and name != ''):
            sent_words += 1
        if (i < len(text) and text[i] in constants.end_of_sent):
            if sent_words != 0:
                sent_lst.append(sent_words)    
            sent_words = 0
        i = i + 1   

    return sent_lst


def means(sent_lst):
    sum = 0
    for i in sent_lst:
        sum += i
    if len(sent_lst) != 0:
        mean = sum / len(sent_lst)
    else:
        mean = 'Review your input. Add punctuation'

    return mean    


def median(sent_lst):
    sent_lst.sort()
    if len(sent_lst) != 0:
        if len(sent_lst) % 2 == 0:
            index = int(len(sent_lst) / 2)
        else:
            index = int((len(sent_lst)-1) / 2)    
        median = sent_lst[index]
    else:
        median = 'Review your input. Add punctuation'

    return median


def different_n_gramms(dict, n = 4): 
    an_list = set()
    for word in dict.keys():
        while word != '':
            if len(word) >= n:
                an_list.add(word[0:n])
            else:
                break    
            word = word[1:]

    return an_list


def list_of_annagramms(words, an_list, m = 10):
    an_dict = {}
    for word in words: 
        for an in an_list:
            word_copy = word
            while word_copy != '':
                if an == word_copy[0:len(an)]:
                    if an not in an_dict.keys():
                        an_dict[an] = 1
                    else:
                        an_dict[an] += 1    
                word_copy = word_copy[1:]    

    sorted_tuple = sorted(an_dict.items(), key = lambda x: x[1], reverse = True)

    return sorted_tuple[:m]
