def frequency_analysis(message, alphabet):
    frequency = {}

    #Assigns every element in the alphabet equal to zero in the frequency dictionary
    for letter in alphabet:
        frequency[letter] = 0

    count = 0

    #gets an accurate number for the amount of letters in the message
    for letter in message.upper():
        if letter in alphabet:
            frequency[letter] += 1
            count += 1

    #gets the correct frequency for each letter that appears in the message
    if count > 0:
        for letter in frequency:
            frequency[letter] = frequency[letter] / count

    #returns the frequency
    return frequency


def cross_correlation(Set1, Set2, alphabet):
    correlation = 0.0
    i = 0
    #finding the cross correlation between two sets given a specific alphabet
    for letter in alphabet:
        correlation += Set1[letter] * Set2[letter]
        i += 1
    return correlation


def get_caesar_shift(enc_message, expected_dist):

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

    frequency = frequency_analysis(enc_message, alphabet)

    #Placeholders for the best possible phi and shift
    phi = -1.0
    best_shift = 0

    #Iterates through every possible shift
    for shift in range(27):
        tempPhi = 0.0

        #Iterates through and accesses the index of every letter in alphabet
        for i, letter in enumerate(alphabet):

            #accesses the frequency of the letter
            freq = frequency.get(letter, 0)

            #Shifts the letter to find the best combination
            index = (i - shift) % 27
            decrypted = alphabet[index]

            expected = expected_dist.get(decrypted, 0)

            #Cross correlation between the letters
            tempPhi += freq * expected


        #If it has the strongest correlation, then it becomes the new best possible shift option
        if tempPhi > phi:
            phi = tempPhi
            best_shift = shift


    #Prints the most likely shift
    return best_shift


def get_vigenere_keyword(enc_message, size, expected_dist):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    keyword = ""

    #Makes sure there are the same number of columns as letter in the keyword
    columns = [""] * size

    #Iterates through every letter and index of that letter in the message
    for i, letter in enumerate(enc_message):

        #Organizes each letter into their own column depending on the keyword length
        index = i % size
        columns[index] += letter

    #Goes through each column and gets the correct shift number in order to determine the keyword letter
    for column in columns:
        shift = get_caesar_shift(column, expected_dist)
        letter = alphabet[shift]
        keyword += letter

    #Returns the correct keyword to be used to decryption
    return keyword
