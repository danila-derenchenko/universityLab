class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def __find(self, node, parent, value):
        if node is None:
            return None, parent, False
        if value == node.data:
            return node, parent, True
        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)
        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)
        return node, parent, False

    def addNode(self, obj):
        if self.root is None:
            self.root = obj
            return obj
        s, p, flag_find = self.__find(self.root, None, obj.data)
        if not flag_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj
        return obj

    def del_leaf(self, s, p):
        if p.left == s:
            p.left = None
        elif p.right == s:
            p.right = None

    def delOneChild(self, s, p):
        if p.left == s:
            if s.left is None:
                p.left = s.right
            elif s.right is None:
                p.left = s.left
        elif p.right == s:
            if s.left is None:
                p.right = s.right
            elif s.right is None:
                p.right = s.left
    def findMin(self, node, parent):
        if node.left:
            return self.findMin(node.left, node)
        return node, parent

    def delNode(self, key):
        s, p, flag_find = self.__find(self.root, None, key)
        if not flag_find:
            return None
        if s.right is None and s.left is None:
            self.del_leaf(s, p)
        elif s.left is None or s.right is None:
            self.delOneChild(s, p)
        else:
            sr, pr = self.findMin(s.right, s)
            s.data = sr.data
            self.delOneChild(sr, pr)
    def getTreeDepth(self, node):
        if node is None:
            return
        v = [node]
        depth = 0
        while v:
            vn = []
            for x in v:
                if x.left:
                    vn += [x.left]
                if x.right:
                    vn += [x.right]
            v = vn
            depth += 1
        return depth

    def show_tree(self, node):
        def height(node):
            if node is None:
                return 0
            else:
                return max(height(node.left), height(node.right)) + 1
        print('Правое поддерево')

        def print_tree(node, space=0):
            if node is None:
                return
            space += 5
            print_tree(node.right, space)
            print(' ' * space + '->', node.data)
            print_tree(node.left, space)

        if node is None:
            return

        max_height = height(node)
        print_tree(node)
        print('Левое поддерево')

    def postordertraversal(self, node):
        if node:
            self.postordertraversal(node.left)
            self.postordertraversal(node.right)
            print(node.data, end=" ")


v = [20, 10, 35, 15, 17, 27, 24, 8, 30]

binTree = Tree()
for x in v:
    binTree.addNode(Node(x))

binTree.show_tree(binTree.root)
print("Постфиксный обход: ")
binTree.postordertraversal(binTree.root)