__author__ = 'shengwen'
# Write a function called answer(document, searchTerms)
# which returns the shortest snippet of the document,
# containing all of the given search terms.
# The search terms can appear in any order.

document = "many google employees can program"
searchTerms = ["google"]
# output
# "google employees can program"

def answer(document, searchTerms):
    # your code here
    words = document.split(" ")
    dict = {i:[] for i in searchTerms}
    for (i,word) in list(enumerate(words)):
        if word in searchTerms:
            dict[word].append(i)
    min_score = 2 * len(words)
    result = None
    for key in dict.keys():
        for i in dict[key]:
            indices = []
            for other_key in dict.keys():
                dists = [abs(i - x) for x in dict[other_key]]
                indices.append(dict[other_key][dists.index(min(dists))])
            score = max(indices) - min(indices) + 1
            if score < min_score:
                min_score = score
                result = [min(indices), max(indices)]
    return " ".join(words[result[0]:result[1] + 1])


print answer(document, searchTerms)