class Codec:
    
    def __init__(self):
        self.short2url = {}
        self.url2counter = {}
        self.counter = 0

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        
        shortUrl = 'tiny.url/' + str(self.counter)
        
        if longUrl not in self.url2counter:
            self.url2counter[longUrl] = shortUrl
            self.short2url[shortUrl] = longUrl
            self.counter += 1
            
        return shortUrl
            
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        
        return self.short2url[shortUrl]
        
import random
class Codec:
    
    def __init__(self):
        self.aplha = 'abcdefghijklmnopqrstuvwxyz'
        self.short2url = {}
        self.url2code = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """    
        
        if longUrl not in self.url2code:
            randStr = self.getRandStr()
            self.url2code[longUrl] = randStr
            self.short2url[randStr] = longUrl
            
        return 'tinyurl.com/' + self.url2code[longUrl]
            
        
    def getRandStr(self):
        
        res = ""
        
        while True:
            for _ in range(6):
                rand_index = random.randint(0,25)
                res += self.aplha[rand_index]
            if res not in self.url2code:
                return res
            res = ""
        
        return res
            
            
    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        
        return self.short2url[shortUrl[-6:]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
