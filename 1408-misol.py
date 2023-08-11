def stringMatching(words):
    words1=[]
    for word1 in words:
        for word2 in words:
            if word1!=word2 and word1 in word2:
                words1.append(word1)
                break
    return words1

print(stringMatching(["mass","as","hero","superhero"]))