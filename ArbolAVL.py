import os
import subprocess

class Node:
    def __init__(self, value):
        self.value  = value
        self.left   = None
        self.right  = None
        self.height = 0
        self.codigo = None

class AVLTree:
    def __init__(self):
        self.root = None

    #add
        
    def add(self, value):
        self.root = self._add(value, self.root)
    
    def _add(self, value, tmp):
        if tmp is None:
            return Node(value)        
        elif value>tmp.value:
            tmp.right=self._add(value, tmp.right)
            if (self.height(tmp.right)-self.height(tmp.left))==2:
                if value>tmp.right.value:
                    tmp = self.srr(tmp)
                else:
                    tmp = self.drr(tmp)
        else:
            tmp.left=self._add(value, tmp.left)
            if (self.height(tmp.left)-self.height(tmp.right))==2:
                if value<tmp.left.value:
                    tmp = self.srl(tmp)
                else:
                    tmp = self.drl(tmp)
        r = self.height(tmp.right)
        l = self.height(tmp.left)
        m = self.maxi(r, l)
        tmp.height = m+1
        return tmp

    def height(self, tmp):
        if tmp is None:
            return -1
        else:
            return tmp.height
        
    def maxi(self, r, l):
        return (l,r)[r>l]   

    #rotations

    def srl(self, t1):
        t2 = t1.left
        t1.left = t2.right
        t2.right = t1
        t1.height = self.maxi(self.height(t1.left), self.height(t1.right))+1
        t2.height = self.maxi(self.height(t2.left), t1.height)+1
        return t2

    def srr(self, t1):
        t2 = t1.right
        t1.right = t2.left
        t2.left = t1
        t1.height = self.maxi(self.height(t1.left), self.height(t1.right))+1
        t2.height = self.maxi(self.height(t2.left), t1.height)+1
        return t2
    
    def drl(self, tmp):
        tmp.left = self.srr(tmp.left)
        return self.srl(tmp)
    
    def drr(self, tmp):
        tmp.right = self.srl(tmp.right)
        return self.srr(tmp)

    #traversals

    def preorder(self):
        self._preorder(self.root)

    def _preorder(self, tmp):
        if tmp:
            print(tmp.value,end = ' ')
            self._preorder(tmp.left)            
            self._preorder(tmp.right)

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, tmp):
        if tmp:
            self._inorder(tmp.left)
            print(tmp.value,end = ' ')
            self._inorder(tmp.right)

    def postorder(self):
        self._postorder(self.root)

    def _postorder(self, tmp):
        if tmp:
            self._postorder(tmp.left)            
            self._postorder(tmp.right)
            print(tmp.value,end = ' ')

    def DefinirNodos(self, tmp, file):
        if tmp:
            if tmp.left:
                file.write(str(tmp.value) + '->' + str(tmp.left.value) + os.linesep)
            if tmp.right:
                file.write(str(tmp.value) + '->' + str(tmp.right.value) + os.linesep)
            self.DefinirNodos(tmp.left, file)            
            self.DefinirNodos(tmp.right, file)


    def ImprimirArbol(self):
        self._ImprimirArbol(self.root)

    def _ImprimirArbol(self, tmp):
        file = open('arbol.dot', "w")
        file.write("digraph grafica{" + os.linesep)
        file.write("rankdir=TB;" + os.linesep)
        file.write("node [shape = circle];" + os.linesep)
        self.DefinirNodos(self.root, file)
        file.write("}" + os.linesep)
        file.close()
        subprocess.call('dot -Tpng arbol.dot -o arbol.png')
        os.system('arbol.png')


           

#init
t = AVLTree()

#add
t.add(5)
t.add(5)
t.add(10)
t.add(20)
t.add(25)
t.add(30)
t.add(35)
t.add(50)

#print traversals
t.preorder()
print()
t.inorder()
print()
t.postorder()

t.ImprimirArbol()