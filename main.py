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

    def searchMinX(self, node, parent, value, flag):
        if value <= node.data:
            if node.left is not None:
                return self.searchMinX(node.left, node, value, flag)
            if parent is None or (flag and node.data > value):
                return None
            return parent.data
        else:
            if node.right is not None:
                return self.searchMinX(node.right, node, value, flag)
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
        for i in range(14):
            arr.append(random.randint(0, 120))
        self.addNode(Node(arr[14 // 2]))
        for i in arr:
            if i != arr[14 // 2]:
                self.addNode(Node(i))
        self.show_tree(self.root)
        return arr

    def show_tree(self, node):
        def height(node):
            if node is None:
                return 0
            else:
                return max(height(node.left), height(node.right)) + 1
        print('ПРАВОЕ ПОДДЕРЕВО')

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
        print('ЛЕВОЕ ПОДДЕРЕВО')

    def postordertraversal(self, node):
        if node:
            self.postordertraversal(node.left)
            self.postordertraversal(node.right)
            print(node.data, end=" ")







binTree = Tree()



selectMode = int(input("Какое дерево сгенерировать? Введите 1, если двоичное, введите 2, если B+: "))
if selectMode == 1:
    print("Двоичное дерево:")
    print(binTree.generateTree())
    while True:
        selectAction = int(input("Выберите действие: 1. Выполнить постфиксный обход(обход снизу вверх), \n2. Выполнить поиск значения по близости снизу: \nВаш выбор: "))
        if selectAction == 1:
            print("Постфиксный обход (обход снизу вверх)")
            binTree.postordertraversal(binTree.root)
            print()
        if selectAction == 2:
            xKey = int(input("Введите ключ для поиска: "))
            print("Результат поиска: ")
            print(binTree.searchMinX(binTree.root, None, xKey, False))
