import os
import yfinance as yf
import time

lines = []

with open('all_tickers.txt', 'r') as f:
    lines = f.readlines()

dir = 'prices'
os.makedirs(dir, exist_ok=True)

for line in lines:
    time.sleep(0.01)
    line = line.strip()
    print(line)
    out = dir + '/' + line
    if os.path.exists(out):
        continue
    try:
        ticker = yf.Ticker(line)
        hist = ticker.history(period="max")
        hist.to_csv(out)
    except:
        continue

print('done')