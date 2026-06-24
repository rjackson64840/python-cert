# while — repeats as long as a condition is True

count = 0
while count < 5:
    print(count)
    count += 1   # Python has no ++ operator, use += 1

# break — exit the loop immediately
count = 0
while True:               # infinite loop — only safe with a break inside
    if count >= 5:
        break
    print(count)
    count += 1

# continue — skip the rest of this iteration, go back to the condition
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue          # skip even numbers
    print(count)          # prints 1, 3, 5, 7, 9

# while / else — the else block runs only if the loop exited normally (no break)
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("loop finished without break")
