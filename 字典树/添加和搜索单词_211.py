from collections import defaultdict

class WordDictionary:


    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=WordTrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        p=self.root;i=0;l=len(word)
        while i<l:
            c=word[i]
            if p.nexts.__contains__(c):
                p=p.nexts.get(c)
                i+=1
            else:
                break
        while i<l:
            node=WordTrieNode()
            node.index=i
            p.nexts[word[i]]=node
            p=node
            i+=1
        p.isWord=True
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def dfs(index,node):
            """
            ：:type index: Int
            :type node WordTrieNode
            :param index:
            :param node:
            :return:
            """
            if(index==len(word)-1):
                if word[index]=='.':
                    for node1 in node.nexts.values():
                        if node1.isWord:
                            return True
                    return False
                else:
                    node1=node.nexts.get(word[index])
                    return node1 is not None and node1.isWord
                  #  return node.nexts.__contains__(word[index]) and node.nexts[word[index]].isWord

            if index>=len(word):
                return False

            if word[index]=='.':
                res=False
                for node1 in node.nexts.values():
                    res=res or dfs(index+1,node1)
                return res
            else:
                node1=node.nexts.get(word[index])
                return node1 is not None and dfs(index+1,node1)
                # if node.nexts.__contains__(word[index]):
                #     node1=node.nexts.get(word[index])
                #     return dfs(index+1,node1)
                # else:
                #     return False


        if word == None or len(word)==0:
            return False
        return dfs(0,self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

class WordTrieNode:

    def __init__(self):

        self.isWord=False
        self.index=0
        self.nexts=defaultdict(WordTrieNode)

obj=WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")
obj.search("pad")
obj.search("dad")
obj.addWord("xiao")
obj.search("han")
print(obj.search("han"))