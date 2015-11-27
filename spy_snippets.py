__author__ = 'shengwen'
# Write a function called answer(document, searchTerms)
# which returns the shortest snippet of the document,
# containing all of the given search terms.
# The search terms can appear in any order.

document = "many google employees can program"
searchTerms = ["google", "program"]
# output
# "google employees can program"

def answer(document, searchTerms):
    # your code here
    words = document.split(" ")
    minLen = len(words)
    i, j = 0, len(words) - 1
    while i < j:
        while words[i] not in searchTerms:
            i += 1
        while words[j] not in searchTerms:
            j -= 1
        

    return minLen

