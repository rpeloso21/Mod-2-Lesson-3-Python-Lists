# Task 1 

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

submitted_and_attended = []

for i in submitted:
    for x in attended:
        if i == x:
            submitted_and_attended.append(i)

print(f"The students who both submitted their assignments and attended the last class are{submitted_and_attended}.")

# Task 2 

submitted.sort()
attended.sort()

lists_are_the_same = submitted == attended

if lists_are_the_same:
    print("The lists are the same.")

else:
    print("The lists are different")


# Task 3


needs_removed = []

for i in attended:
    if i not in submitted:
        needs_removed.append(i)

for i in needs_removed:
    attended.remove(i)

print(attended)
