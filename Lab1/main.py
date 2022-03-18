from unicodedata import digit
import lab1_task

def main():
    print('Do you want to change K? Default is 4. If no, enter anything you want')
    k = input()
    if k is digit:
        k = int(k)
    else:
        k = 4    

    print('Do you want to change N? Default is 10. If no, enter anything you want')
    n = input()
    if n is digit:
        n = int(n)
    else: 
        n = 10

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
