from tree import Tree

def main():
    root = Tree(4)
    root.insertall(6, 5, 2, 1, 3)
    root.insert(7)
    root.inorder()
    root.preorder()
    root.postorder()
    root.search(8)
    root.search(3)

if __name__ == "__main__":
    main()
