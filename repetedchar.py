
# print first repeated char https://www.geeksforgeeks.org/find-the-first-repeated-character-in-a-string/
def repeatedChar(string):
  charmap = {}

  for char in string:
    if char in charmap:
      return char
    charmap[char] = 1
  return True



if __name__ == '__main__':
  print(repeatedChar('geksforgeeks'))