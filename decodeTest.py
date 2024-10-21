def encode(message):
    encoded_message = ""
    i = 0

    while (i <= len(message)-1):
        count = 1
        ch = message[i]
        j = i
        while (j < len(message)-1):
            if (message[j] == message[j+1]):
                count = count+1
                j = j+1
            else:
                break
        encoded_message=encoded_message+str(count)+ch
        i = j+1

    return encoded_message

# testing
original_message = "RWWRWBWWWGWWWBWWWBWB"
encoded_message=encode(original_message)
print("original message: ", original_message, " Length = ", len(original_message))
print("encoded message: ", encoded_message, " Length = ", len(encoded_message))
compression_ratio = (len(encoded_message)/len(original_message))*100
print(round(compression_ratio, 2), " % ")
