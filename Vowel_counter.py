def vowel_counter(string):
    """Counts the number of vowels in a given string"""

    vowel_count = 0

    #iterate over given string
    for char in string:
        #check if char is a vowel
        if char in 'aeiou':
            vowel_count += 1

    return vowel_count

def word_counter(sentence):
    """Counts the number of words in given sentence"""

    sentence = sentence.strip() #removes whitespace from beginning and end of sentence

    space_count = 0
    for char in sentence:
        #check if char is single space
        if char in '':
            space_count += 1

    word_count = space_count + 1

    return word_count
    

def main():

 while 1 == 1:

    input_string = input("enter a string: ")

    if input_string == '-1':
        break

    print(vowel_counter(input_string), "vowels in", input_string)
    print(word_counter(input_string), "words in", input_string)

#to exeute main function
if __name__ == '__main__':
        main()
