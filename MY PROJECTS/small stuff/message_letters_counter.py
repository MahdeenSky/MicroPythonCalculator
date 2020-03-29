message = """ message goes here """
dictionary = {}
for a in message.lower(): # loops through the lowercase characters of the string
    if a.isalpha(): # if you want numbers change isalpha to isnumeric, or if you want both change it to isalphanumeric
        dictionary.setdefault(a, 1) # sets the value of the key to 1, if it doesn't exist in the dictionary
        if dictionary.get(a) != None: # if a key exists, then it will .get() will not return None
            dictionary[a] += 1 # adds to the counter of the key found
print(dictionary) # prints the dictionary after all the characters has been read