

# This was a pretty straightforward and cool solution, changing the
# select the first 0 to k string letters, reverse them, add the next K to 2k characters, as it is. THen reverse the left string, this should only be done if the string has some value
return s[:k][::-1] + s[k:2*k] + self.reverseStr(s[2*k:], k) if s else ""
