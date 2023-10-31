def encode(message):
    # Write your code here.
    encoded_message = ""
    c = 1

    if len(message) == 1:
        return message + str(len(message))

    for letter in range(len(message)-1):
        if message[letter] == message[letter+1]:
            c +=1
        else:
            encoded_message += message[letter] + str(c)
            c = 1
    
        if letter + 1 == len(message) - 1:
            encoded_message += message[letter + 1] + str(c)
        
    return encoded_message
