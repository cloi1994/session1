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

                newWord = list(top)

                for i in range(len(newWord)):
                    for letter in 'abcdefghijklmnopqrstuvwxyz':
                        newWord[i] = letter

                        word = ''.join(newWord)

                        if word == endWord:
                            return step + 1

                        if word not in wordList:
                            continue
                        print word
                        q.append(word)
                        wordList.remove(word)
                    newWord = list(top)
                           
        return 0
