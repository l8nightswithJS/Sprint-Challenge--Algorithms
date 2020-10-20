'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
word = ["abcdefghithkthkth"]
def count_th(word):
    #need to sort through all letters in the word[0],
    # TBC
    #base case if length of word is less than 2 characters return 0
    if len(word) < 2:
        return 0
    
    #if word range == "th" return the count 
    if word[:2] == "th":
        return count_th(word[1:]) + 1

    #run function recursively 
    return count_th(word[1:])