from present import Present

with open("day02/input.txt") as f:
    data = f.readlines()
    data = [item.strip() for item in data]


paper_needed = 0
ribbon_needed = 0

for item in data:
    length, width, height = item.split("x")
    present = Present(int(length), int(width), int(height))
    paper_needed += present.paper_needed()
    ribbon_needed += present.ribbon_needed()

print(f"Paper needed: {paper_needed}\nRibbon needed: {ribbon_needed}")
