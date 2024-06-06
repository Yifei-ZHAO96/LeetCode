class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1
    
    def get_score(self, word):
        node = self.root
        score = 0
        for char in word:
            node = node.children.get(char)
            if not node: return score
            score += node.count

        return score

class Solution:
    def sumPrefixScores(self, words):
        trie = Trie()
        # 插入所有单词到字典树中
        for word in words:
            trie.insert(word)
        
        result = []
        # 计算每个单词的前缀得分和
        for word in words:
            result.append(trie.get_score(word))
        
        return result

# 示例使用
words = ["a", "ab", "abc", "cab"]
sol = Solution()
print(sol.sumPrefixScores(words))  # 输出应该是 [1, 3, 6, 3]

words = ["abc","ab","bc","b"]
print(sol.sumPrefixScores(words))