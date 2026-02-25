class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False


def insert(node: Trie, word: str):
    if node is None:
        node = Trie()

    current = node
    for char in word:
        idx = ord(char) - ord('a')
        if current.children[idx] is None:
            current.children[idx] = Trie()

        current = current.children[idx]

    current.is_end = True
    return node

#Incomplete implementation of autocomplete
# def autocomplete(node:Trie,val:str):
#     current = node
#     store = []
#     for i in val:
#         idx = ord(i) - ord('a')
#         if current.children[idx] is None:
#             return []
#         else:
#             store.append(current.children)

#         current = current.children[idx]
        
            
#     print(store)

def main():
    node = None
    name = input("")
    
    node = insert(node,name)
    # autocomplete(node,"da")
   

if __name__ == "__main__":
    main()        