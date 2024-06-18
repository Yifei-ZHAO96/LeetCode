from typing import List
import collections

class TrieNode:
    def __init__(self) -> None:
        self.children = collections.defaultdict(TrieNode)
        self.word = ''
        self.times = 0


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self, word, t):
        cur = self.root
        
        for w in word:
            cur = cur.children[w]
        
        cur.times += t
        cur.word = word
    
    def startsWith(self, word):
        cur = self.root
        
        for w in word:
            cur = cur.children.get(w)
            
            if not cur:
                return None
        
        return cur

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()
        # O(NM) O(NM)
        for s, t in zip(sentences, times):
            self.trie.insert(s, t)

        self.sentence = ''
    
    def input(self, c: str) -> List[str]:
        # O(S) O(S)
        if c == '#':
            self.trie.insert(self.sentence, 1)
            self.sentence = ''
            return []
        
        self.sentence += c
        # O(S)
        cur = self.trie.startsWith(self.sentence)
        
        if not cur:
            return []
        
        res = []
        # O(NM) O(NM)
        self.dfs(cur, res)
        
        res.sort(key=lambda x: (-x[1], x[0]))
        print([v[0] for v in res[:3]])
        return [v[0] for v in res[:3]]
    
    def dfs(self, cur: TrieNode, res: List[str]):
        if cur.word:
            res.append((cur.word, cur.times))
        
        for child in cur.children:
            self.dfs(cur.children[child], res)


obj = AutocompleteSystem(["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2])
obj.input("i") # return ["i love you", "island", "i love leetcode"]
obj.input(" ") # return ["i love you", "i love leetcode"]
obj.input("a") # return []
obj.input("#") # return []
obj.input("i") # return ["i love you", "island", "i love leetcode"]
obj.input(" ") # return ["i love you", "i love leetcode", "i a"]
obj.input("a") # return ["i a"]