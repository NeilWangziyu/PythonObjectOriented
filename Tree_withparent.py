# https://hujiaweibujidao.github.io/blog/2014/05/09/python-data-structures---c4-trees/
class TreeNode:
    def __init__(self, key, val, left=None, right = None, parent = None):
        self.key = key
        self.val = val
        self.leftchild = left
        self.rightchild = right
        self.parent = parent


    def hasLeftChild(self):
        return self.leftchild

    def hasRightChild(self):
        return self.rightchild

    def isLeftChild(self):
        return self.parent.leftchild == self

    def isRightChild(self):
        return self.parent.rightchild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.leftchild or self.rightchild)

    def hasAnyChildren(self):
        return self.rightchild or self.leftchild

    def hasBothChildren(self):
        return self.rightchild and self.leftchild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.val = value
        self.leftchild = lc
        self.rightchild = rc
        if self.hasLeftChild():
            self.leftchild.parent = self
        if self.hasRightChild():
            self.rightchild.parent = self


class RBTreeNode:
    pass




class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def print_node(self, node):
        if node.parent:
            print([node.key, node.val, node.parent.key])
        else:
            print([node.key, node.val])

    def inorder(self, node):
        if node.leftchild:
            self.inorder(node.leftchild)
        self.print_node(node)
        if node.rightchild:
            self.inorder(node.rightchild)

    def levelorder(self, node):
        nodes = []
        nodes.append(node)
        while nodes:
            current_node = nodes.pop(0)
            self.print_node(current_node)
            if current_node.leftchild:
                nodes.append(current_node.leftchild)
            if current_node.rightchild:
                nodes.append(current_node.rightchild)


    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, currentNode):
        if key <  currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftchild)
            else:
                currentNode.leftchild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightchild)
            else:
                currentNode.rightchild = TreeNode(key, val, parent=currentNode)

    def __setitem__(self, key, value):
        self.put(key, value)






class AVLTree(BinarySearchTree):
    pass


if __name__ == "__main__":
    print('test bst')
    mytree = BinarySearchTree()
    mytree[3]="red"
    mytree[4]="blue"
    mytree[6]="yellow"
    mytree[2]="at"
    mytree[5]='dog'
    mytree[1]='cat'
    mytree.inorder(mytree.root)
    print("----------")
    mytree.levelorder(mytree.root)

