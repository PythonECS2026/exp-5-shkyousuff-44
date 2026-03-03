# AIM: Task List Manager
# Coder:
# Date:

print("--- Task List Manager ---")
tasks = ["Sleep", "Getup", "Brush"]
print(f"Original Tasks: {tasks}")

# Write your code here
# TODO: Add & Print new Task from user

# TODO: Edit & Print task selected by User

# TODO: Remove & Print a Task selected by User

# TODO: Sort & Print the Tasks
tasks = ["Sleep", "Getup", "Brush"]
print(f"Original Tasks: {tasks}")
tasks.append(input())
print(f"Tasks after Adding: {tasks}")
edit_index = int(input())
tasks[edit_index] = input()
print(f"Tasks after Editing: {tasks}")
tasks.pop(0)
print(f"Tasks after Removing: {tasks}")
tasks.sort()
print(f"Tasks after Sorting: {tasks}")
