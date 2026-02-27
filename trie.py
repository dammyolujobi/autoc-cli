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


def autocomplete(node:Trie,val:str):
    current = node
    result = []
    for i in val:
        idx = ord(i) - ord('a')
        if current.children[idx] is None:
            return []
        
        current = current.children[idx]
    collect_all(current,prefix=val,results= result)
    value = min(result, key=lambda x: (len(x), x))
    return value

         
def collect_all(node:Trie, prefix:str, results:list):
    if node.is_end:
        results.append(prefix)
    for i in range(26):
        if node.children[i] is not None:
            collect_all(node.children[i],prefix + chr(ord('a') + i),results)



def main():
    node = None
    for i in range(5):
        name = input("Enter the full word: ").lower()
        
        node = insert(node,name)
    prefix = input("Enter the word you want to predict: ")
    print(autocomplete(node,prefix))
   

if __name__ == "__main__":
    main()        