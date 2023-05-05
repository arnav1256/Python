tree = [["Italy", 1, 2],["France", 3, 4],["Spain", 5, -1],["Austria", -1, 6],["Germany", -1, -1],["Norway", -1, -1],["China", -1, -1]]
order = ["Austria", "China",  "France", "Germany", "Italy", "Norway", "Spain"]
def binarysearch(tree, keyword):
    this = tree[0]
    if this[0] == keyword:
        return True
    elif order.index(this[0]) < order.index(keyword):
        if this[2] != -1:
            return binarysearch(tree[this[2]], keyword)
        else:
            return False
    elif order.index(this[0]) > order.index(keyword):
        if this[1] != -1:
            return binarysearch(tree[this[1]], keyword)
        else:
            return False
    else:
        return binarysearch(tree[this[2]], keyword)

print(binarysearch(tree, "Norway"))
        