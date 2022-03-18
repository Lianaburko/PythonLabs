import lab1_task

def main():
    print('add your k')
    k = int(input())
    print('add your n')
    n = int(input())
    s = input().lower()

    numbers = lab1_task.amount_of_words_in_sentences(s) #list of words_amount in each sentence
    word_list = lab1_task.words_in_text(s) # list of words
    dicti = lab1_task.amount_of_diff_words(word_list) # dictionary of words
    an_list = lab1_task.different_n_gramms(dicti, k) # list of annagamms

    print(f"list of words: {lab1_task.words_in_text(s)}")
    print(f"mean is: {lab1_task.means(numbers)}")
    print(f"median is: {lab1_task.median(numbers)}")
    print(lab1_task.list_of_annagramms(word_list, an_list, n))


if __name__ == "__main__":
    main()
