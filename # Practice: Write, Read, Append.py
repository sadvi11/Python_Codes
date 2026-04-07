# Practice: Write, Read, Append

# 1. WRITE a file
with open("my_costs.txt", "w") as file:
    file.write("EC2: $20\n")
    file.write("S3: $5\n")

# 2. READ it back
with open("my_costs.txt", "r") as file:
    content = file.read()
    print("--- File contents ---")
    print(content)

# 3. APPEND a new line
with open("my_costs.txt", "a") as file:
    file.write("RDS: $17\n")

print("Done! Check your folder for my_costs.txt")
 