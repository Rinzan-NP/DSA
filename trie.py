class TrieNode:
    def  __init__(self) -> None:
        self.children = {}
        self.end_word = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def add(self, word : str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_word = True

    def search(self, word : str):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end_word  

    def remove(self, word):
        self.recursive_remove(self.root, word, 0)

    def recursive_remove(self, node : TrieNode, word, index):
        if index == len(word):
            if not node.end_word :
                return False
            node.end_word = False
            return len(node.children) == 0
        
        char = word[index]
        if char not in node.children:
            return False
        
        should_delete = self.recursive_remove(node.children[char], word, index + 1)

        if should_delete :
            del node.children[char]
            return len(node.children) == 0 
        
        return False
    
    def add_suffix(self , word):
        for i in range(len(word)):
            s_word = word[i:]
            self.add(s_word)

trie = Trie()
print("Searching apple in trie : " + str({trie.search("apple")}))
trie.add("apple")
print(trie.root.children)
print("apple added!")
print("Searching apple in trie : " + str({trie.search("apple")}))
trie.remove("apple")
print("apple deleted!")
print("Searching apple in trie : " + str({trie.search("apple")}))

        


        

