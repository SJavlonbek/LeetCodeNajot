def max_num_of_pairs(words):
    z = 0
    set_words = set()

    for word in words:
        teskari = word[::-1]
        if teskari in set_words:
            z += 1
            set_words.remove(teskari)
        else:
            set_words.add(word)

    return z

print(max_num_of_pairs(["cd","ac","dc","ca","zz"]))
print(max_num_of_pairs(["ab","ba","cc"]))