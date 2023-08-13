import yfinance as yf
import string
import os
import time

def cmp(a, b):
    if len(a) < len(b):
        return -1
    elif len(a) > len(b):
        return 1
    else:
        return ord(a, b)
    
def sort_key(a):
    return (len(a), a)

chars = ['$', '.']
for char in string.ascii_uppercase:
    chars.append(char)
for char in string.digits:
    chars.append(char)
chars = set(chars)
chars = list(chars)
chars = sorted(chars, key=sort_key)
base = len(chars)

dir = 'prices2'
os.makedirs(dir, exist_ok=True)

existing = os.listdir(dir)
existing = sorted(existing, key=sort_key)
last_existing = existing[-1] if len(existing) > 0 else ''
last_existing_sort_key = sort_key(last_existing)

max_len = 10
count = 0
hits = 0
skipped = 0
for i in range(1, max_len + 1):
    # print(i, 'of', max_len)
    # i == len of str
    # max is base^i
    hi = pow(base, i)
    for j in range(hi):
        time.sleep(0.01)
        # j == index of str
        # split j into i parts
        arr = []
        index = j
        for k in range(i):
            m = int(index % base)
            arr.insert(0, chars[m])
            index = int(index / base)
        str = ''.join(arr)
        out = dir + '/' + str
        str_sort_key = sort_key(str)
        skip = False
        if str == '.' or str == '..':
            skip = True
        elif str_sort_key <= last_existing_sort_key:
            # we already processed this one
            skip = True
        elif os.path.exists(out):
            skip = True
        if not skip:
            try:
                ticker = yf.Ticker(str)
                hist = ticker.history(period="max", prepost=True, actions=True, raise_errors=True)
                if hist.shape[0] > 0:
                    hist.to_csv(out)
                    hits = hits + 1
            except:
                pass
        else:
            skipped = skipped + 1
        count = count + 1
        print(str, hits, skipped, count)
        

print('done')