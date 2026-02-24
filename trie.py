import random
class TrieNode:
    def __init__(self,val=None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def insert(node:TrieNode, val:str):
        if len(val) == 0:
            return node
        
        if node is None:
            return TrieNode(val[0])
        
        if node.val == val[0]:
            node.left = TrieNode.insert(node.left,val[1:])
        
        else:
            node.right = TrieNode.insert(node.right,val)
        
        return node

def preorder(node: TrieNode):
    if node:
        print(node.val)
        preorder(node.left)
        preorder(node.right)


def main():

    first_val = input("Input first val: ")
    second_val = input("Input second val")

    node = None
    for _ in first_val:
        node = insert(node, first_val.lower())
    for _ in second_val:
        node = insert(node,second_val)

    preorder(node)

if __name__ == "__main__":
    main()        