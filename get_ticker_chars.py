

lines = []

with open('all_tickers.txt', 'r') as f:
    lines = f.readlines()

all_chars = set([])
for line in lines:
    for char in line.strip():
        all_chars.add(char)

all_chars = list(all_chars)
all_chars.sort()
print(all_chars)