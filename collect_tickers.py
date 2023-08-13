import json

def main():
    print('starting...')

    json_files = ['other-listed_json.json', 'nyse-listed_json.json']
    tickers = set()
    for json_file in json_files:
        with open(json_file, 'r') as f:
            content = f.read()
            parsed = json.loads(content)
            for i in parsed:
                ticker = i['ACT Symbol']
                tickers.add(ticker)
        
    with open('parsed_tickers.txt', 'r') as f:
        content = f.read()
        lines = content.splitlines()
        for line in lines:
            tickers.add(line)

    tickers = list(tickers)
    tickers.sort()
    with open('all_tickers.txt', 'w') as f:
        for ticker in tickers:
            f.write(ticker)
            f.write('\n')

    print('done')

if '__main__' == __name__:
    main()