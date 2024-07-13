from typing import List
from collections import defaultdict

class TrieNode:
    def __init__(self) -> None:
        self.children = defaultdict(TrieNode)
        self.count = 0
        self.word = ''


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def add(self, word, freq):
        node = self.root
        for w in word:
            node = node.children[w]
        
        node.word = word
        node.count += freq
    
    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return
        return node
    

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()
        self.temp = ''
        # O(MN) O(MN)
        for word, freq in zip(sentences, times):
            self.trie.add(word, freq)
        
    def input(self, c: str) -> List[str]:
        if c == '#':
            # O(S)
            self.trie.add(self.temp, 1)
            self.temp = ''
            return []
        
        self.temp += c
        # O(S)
        node = self.trie.search(self.temp)
        if not node:
            return []
        
        self.res = []
        # O(MN) O(MN)
        self.dfs(node)
        self.res.sort(key=lambda x: (-x[0], x[1]))
        return [v[1] for v in self.res[:3]]
    
    def dfs(self, node: TrieNode):
        if not node:
            return

        if node.word:
            self.res.append((node.count, node.word))

        for child in node.children:
            self.dfs(node.children[child])