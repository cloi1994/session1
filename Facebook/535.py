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
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
