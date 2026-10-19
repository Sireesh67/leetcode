class Solution:
    def __init__(self):
        self.encodee = {}
        self.decodee = {}
        self.base = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        if longUrl not in self.encodee:
            shortUrl = self.base + str(len(self.encodee) + 1)
            self.encodee[longUrl] = shortUrl
            self.decodee[shortUrl] = longUrl
        return self.encodee[longUrl]

    def decode(self, shortUrl: str) -> str:
        return self.decodee[shortUrl]