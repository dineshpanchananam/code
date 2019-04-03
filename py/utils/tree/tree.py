class Tree:    
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right
    
    def preorder(self):
        print "preorder:  ",
        self.__xyzorder(-1)
    
    def inorder(self):  
        print "inorder:   ",
        self.__xyzorder()
    
    def postorder(self):
        print "postorder: ",
        self.__xyzorder(1)
    
    def __xyzorder(self, mod=0):
        self.__xyzorderimpl(mod)
        print
    
    def __xyzorderimpl(self, mod):
        if mod == -1: 
            print self.data,
        if self.left != None: 
            self.left.__xyzorderimpl(mod)
        if mod ==  0: 
            print self.data,
        if self.right != None: 
            self.right.__xyzorderimpl(mod)
        if mod ==  1: 
            print self.data,
    
    def insert(self, value):    
        if value < self.data:
            if self.left != None: 
                self.left.insert(value)
            else: 
                self.left = Tree(value)
        else:
            if self.right != None: 
                self.right.insert(value)
            else: 
                self.right = Tree(value)
    
    def insertall(self, *values):
        for value in values:
            self.insert(value)        
   
    def search(self, key):      
        found = self.__searchimpl(key)
        print "searching for", key, ":", ('' if found else 'not ') + 'found'
        return found
        
    def __searchimpl(self, key):  
        if self.data == key:
            return True
        elif self.data > key:
            return False if self.left == None else self.left.__searchimpl(key)
        else:
            return False if self.right == None else self.right.__searchimpl(key)

