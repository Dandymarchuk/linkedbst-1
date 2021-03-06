from linkedbst import LinkedBST

tree = LinkedBST([1, 5, 3, 7, 5, 67, 47, 7, 3])
print()
print()
print("Дерево:")
print()
print(tree)
print("Висота =", tree.height())
print("Чи є дерево збалансоване:", tree.is_balanced())
tree.rebalance()
print()
print("Збалансоване дерево:")
print(tree)
print("Елементи в діапазоні 5-47 ")
print(tree.range_find(5, 47)) # 5 5 7 7 47
print("Найменший елемент більше 5")
print(tree.successor(5))
print("Найбільший елемент менше 7")
print(tree.predecessor(7))