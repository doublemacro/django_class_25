import time
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(4000)
# Sirul fibonacci
#       0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
#       0  1  2  3  4  5  6   7   8   9  10  11
# n, 1. nr 5 -> 5, 8 -> 21

#  Fn = Fn-1 + Fn-2

# fa-o sa fie mai eficienta:
# nu vrem sa calculam fibonacci(6) de mai multe ori. O calculam o data si o tinem in memorie.

# def fibonacci(n):
#     if n < 2:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)
#
# print(fibonacci())



# memo = [0, 1, 1, 2, 3]
# memo[7] -> 13

"""
memo = {
    0: 0,
    1: 1,
    2: 1,
    ...
    8: 21,....
}
"""

memo = {}

def fibonacci_recursive(n: int):
    # fix la inceput, verificam daca nr fibonacci exista in lista deja
    # daca exista, returneaza numarul stocat, nu-l mai calcula.

    # if n cifra din memo
    # return cifra din memo
    # else calculeaza:
    if n in memo:
        return memo[n]
    else:
        # si salveaza rezultatul
        if n == 0:
            memo[0] = 0
            return 0
        if n == 1:
            memo[1] = 1
            return 1
        result = fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
        memo[n] = result
        return result


start = time.time()
print(fibonacci_recursive(3000))
print("Ran for {}s".format(time.time() - start))



class Leaf:
    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    # nod radacina
    # left_leaf, right_leaf

    def __init__(self):
        self.root_leaf: Leaf = None

    def _insert_number(self, current_node, number):
        if number < current_node.value:
            if current_node.left is not None:
                self._insert_number(current_node.left, number)
            else:
                print("Inserted {} in left leaf, parent node {}".format(number, current_node.value))
                current_node.left = Leaf(number)
        else:
            if current_node.right is not None:
                self._insert_number(current_node.right, number)
            else:
                print("Inserted {} in right leaf, parent node {}".format(number, current_node.value))
                current_node.right = Leaf(number)


    def insert_number(self, number: int):
        if self.root_leaf is None:
            print("inserted {} in root node".format(number))
            self.root_leaf = Leaf(number)
        else:
            current_node = self.root_leaf
            self._insert_number(current_node, number)

    def _calculate_depth(self, current_node, depth, depth_list):
        if current_node.left is not None:
            depth += 1
            self._calculate_depth(current_node.left, depth, depth_list)
        if current_node.right is not None:
            depth += 1
            self._calculate_depth(current_node.right, depth, depth_list)
        if current_node.left is None and current_node.right is None:
            depth_list.append(depth)
            return depth


    def calculate_depth(self):
        if self.root_leaf is None:
            return 0
        current_node = self.root_leaf
        depth = 1
        depth_list = []
        self._calculate_depth(current_node, depth, depth_list)
        depth_list.sort()
        return depth_list[-1]


tree = BinaryTree()
tree.insert_number(8)
tree.insert_number(10)
tree.insert_number(20)
tree.insert_number(200)
tree.insert_number(2000)
tree.insert_number(20000)
tree.insert_number(200000)
tree.insert_number(2000000)
tree.insert_number(20000000)
tree.insert_number(200000000)

print(tree.calculate_depth())




# https://en.wikipedia.org/wiki/Fibonacci_sequence
# https://i.sstatic.net/kgXDS.png
# https://stackoverflow.com/questions/3323001/what-is-the-maximum-recursion-depth-and-how-to-increase-it
# https://emre.me/data-structures/binary-tree/
# https://cdn.emre.me/2019-07-26-binary-tree.png
# https://chatgpt.com/c/68c04c86-5700-8332-b03c-fc10a1233236

