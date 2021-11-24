import sys
def input(): return sys.stdin.readline()

n = int(input())
dicT = {}

for _ in range(n):
  center, left, right = input().split()
  dicT[center] = [left, right]


def preorder(node):
  left, right = dicT[node]
  print(node, end = '')
  
  if left != '.':
    preorder(left)

  if right != '.':
    preorder(right)
  return


def inorder(node):
  left, right = dicT[node]
  if left != '.':
    inorder(left)

  print(node, end = '')

  if right != '.':
    inorder(right)
  return


def postorder(node):
  left, right = dicT[node]
  if left != '.':
    postorder(left)

  if right != '.':
    postorder(right)
  
  print(node, end = '')
  return


preorder('A')
print()
inorder('A')
print()
postorder('A')


