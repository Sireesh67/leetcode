class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()

        for i in emails:
            a,b = i.split("@")
            a = a.split("+")[0]
            a= a.replace(".", "")
            s.add(a+"@"+b)
        return len(s)        