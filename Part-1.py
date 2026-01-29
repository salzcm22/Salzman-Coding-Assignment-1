def caesar_cipher(message, shift, encrypt):
    #Defines the alphabet that can be used for the potential letters
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    newMessage = ""

    #Determines whether or not the message will be encrypted or decrypted based on the input
    message = message.upper()
    actual_shift = shift % 27 if encrypt else - (shift % 27)

    #compares the letter in the message to its place in the alphabet
    for letter in message:
        if letter in alphabet:

            #finds the original index for the letter and shifts it by the shift amount, adding the new letter to the new message
            oldIndex = alphabet.index(letter)
            newIndex = (oldIndex + actual_shift) % 27
            newMessage += alphabet[newIndex]
        else:
            newMessage += letter

    #returns the new message comprised of the shifted letters
    return newMessage


def vigenere_cipher(message, keyword, encrypt):

    newMessage = ""
    keyword = keyword.upper()
    key_len = len(keyword)

    #Establishes the alphabet used for the cipher
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "


    #Gives every letter and index for each letter in the message
    for index, letter in enumerate(message.upper()):
        if letter in alphabet:

            #Finds the correct shift based on the specific letter of the keyword
            #and shifts by that much using the caesar_cipher function
            shift = alphabet.index(keyword[index % key_len])
            newMessage += caesar_cipher(letter, shift, encrypt)
        else:
            newMessage += letter
    #returns the new message consisted of the now shifted letters
    return newMessage
