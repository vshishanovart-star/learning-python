# ('Task 1. Test task')

# Stepan came to get a job, where he was given a test assignment:
# analyze such a table,
# understand how it is built and write a program to display it on the screen.

# Example
# 0 2 4 6  8  10
# 1 3 5 7  9  11
# 2 4 6 8  10 12
# 3 5 7 9  11 13
# 4 6 8 10 12 14
# 5 7 9 11 13 15

# Help Stepan to implement such a program.
# Hint: Pay attention to the column numbers and keep in mind the \t literal for tabs.

for row in range(6):
  for col in range(row, row + 11, 2):
    print(col, end = "\t")
  print("\n" * 2)