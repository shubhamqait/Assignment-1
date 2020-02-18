'''Q7) Given a two list of equal sizes create a set such that it shows the element from both lists
in the pair.
Given:
First List [2, 3, 4, 5, 6, 7, 8]
Second List [4, 9, 16, 25, 36, 49, 64]
Expected Outcome:
Result is {(6, 36), (8, 64), (4, 16), (5, 25), (3, 9), (7, 49), (2, 4)}'''


firstList = [2, 3, 4, 5, 6, 7, 8]
secondList = [4, 9, 16, 25, 36, 49, 64]
result = zip(firstList, secondList)
resultSet = set(result)
print(resultSet)
