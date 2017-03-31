class TNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return "{" + str(self.left) + "<-- [" + str(self.data) + "] -->" + str(self.right) + "}"


def create_min_bst(list_sorted):
    len_list = len(list_sorted)
    if len_list == 0:
        return None
    mid_list = len_list / 2
    #print list_sorted[mid_list]
    root = TNode(list_sorted[mid_list])
    root.left = create_min_bst(list_sorted[:mid_list])
    root.right = create_min_bst(list_sorted[mid_list+1:])
    return root

#if __name__ == '__main__':
#    bst = create_min_bst([2, 3, 5, 7, 12, 14, 16])
#    print bst



