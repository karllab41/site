def subsets(L):
    allsets = [[]]
    for elt in L:
        for subset in allsets[:]:
             allsets.append(subset + [elt])
    return allsets
