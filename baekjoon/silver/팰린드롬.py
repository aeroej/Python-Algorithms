import sys

def isPalindrome(word_a, word_b):
  word = word_a + word_b
  if word == word[::-1]:
    print(word)
    sys.exit(0)


if __name__ == "__main__":
  t = int(input())

  for _ in range(t):
    k = int(input())
    words = [sys.stdin.readline().rstrip() for _ in range(k)]
 
    for i in range(k-1):
      for j in range(i+1, k):
        isPalindrome(words[i], words[j])
        isPalindrome(words[j], words[i])

    print("0")

