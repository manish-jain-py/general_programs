""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def check_binary_search_tree_(root):
    arr = t_inorder(root, [])
    return is_arr_sorted(arr)


def t_inorder(root, arr=[]):
    if root.left:
        t_inorder(root.left, arr)
    arr.append(root.data)
    if root.right:
        t_inorder(root.right, arr)
    return arr


def is_arr_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            continue
        else:
            return False
    return True