sec = int(input())
print("It is", sec // 3600, "hours", (sec - (sec // 3600) * 3600) // 60, "minutes.")