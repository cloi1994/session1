class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        step = 0
        l = len(beginWord)
        q = [beginWord]
                
        wordList = set(wordList)
        
        if endWord not in wordList:
            return 0
        
        while q != []:
            step += 1
            
            for i in range(len(q)):
                top = q.pop(0)   
                
                newword = list(top) 
                
                for i in range(len(top)):                
                    
                    for alpha in 'abcdefghijklmnopqrstuvwxyz':
                        newword[i] = alpha
                        
                        word = ''.join(newword)
                        
                        if word == endWord:
                            return step + 1
                        
                        if word in wordList:
                            wordList.remove(word)
                            q.append(word)
                                                
                        newword = list(top)
                                      
                    
            
        return 0
