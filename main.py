import random

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def __find(self, node, parent, value):
        if node is None:
            return None, parent, False
        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)
        if value >= node.data:
            if node.right:
                return self.__find(node.right, node, value)
        return node, parent, False

    def searchMinX(self, node, parent, value):
        if value <= node.data:
            if node.left is not None:
                return self.searchMinX(node.left, node, value)
            if parent is None:
                return None
            return parent.data
        else:
            if node.right is not None:
                return self.searchMinX(node.right, node, value)
            return node.data

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

    def generateTree(self):
        arr = []
        for i in range(15):
            arr.append(random.randint(0, 120))
        self.addNode(Node(arr[15 // 2]))
        for i in arr:
            if i != arr[15 // 2]:
                self.addNode(Node(i))
        self.show_tree(self.root)
        return arr


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


selectMode = int(input("Какое дерево сгенерировать? Введите 1, если двоичное, введите 2, если B+: "))
if selectMode == 1:
    print("Двоичное дерево:")
    print(binTree.generateTree())
    while True:
        selectAction = int(input("Выберите действие: 1. Выполнить постфиксный обход(обход снизу вверх), \n2. Выполнить поиск значения по близости снизу: "))
        if selectAction == 1:
            print("Постфиксный обход (обход снизу вверх)")
            binTree.postordertraversal(binTree.root)
            print()
        if selectAction == 2:
            xKey = int(input("Введите ключ для поиска: "))
            print("Результат поиска: ")
            print(binTree.searchMinX(binTree.root, None, xKey))