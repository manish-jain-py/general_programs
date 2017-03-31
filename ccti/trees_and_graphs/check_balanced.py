class BTNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return "{ " + str(self.left) + "<--" + str(self.data) + "-->" + str(self.right) + "}"

root = BTNode(5)
root.left = BTNode(10)
root.left.left = BTNode(20)
root.left.right = BTNode(25)
root.left.left.left = BTNode(50)
#root.left.left.left.left = BTNode(150)
root.right = BTNode(15)
root.right.right = BTNode(30)
root.right.right.right = BTNode(130)
print root


def postorder(root, balanced=True):
    if root:
        if not postorder(root.left):
            return False
        if not postorder(root.right):
            return False
        diff = visit(root)
        if diff > 1:
            return False
    return balanced


def visit(root):
    if not root:
        return 0
    else:
        if root.left:
            left_height = root.left.height
        else:
            left_height = -1

        if root.right:
            right_height = root.right.height
        else:
            right_height = -1

        root.height = max(left_height, right_height) + 1
        diff = abs(left_height - right_height)
        #print root.data, root.height, diff
    return diff

print postorder(root)

