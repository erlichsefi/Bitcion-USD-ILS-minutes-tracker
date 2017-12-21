
import requests,json,time,os
output="api_data_USD_ILS.csv"
interval=60

def query():
	url = 'https://api.coindesk.com/v1/bpi/currentprice/ILS.json'
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
	result = requests.get(url, headers=headers)
	response_dict = json.loads(result.content.decode())

	currency=response_dict['bpi']
	USD=currency['USD']['rate']
	ILS=currency['ILS']['rate']
	date=response_dict['time']['updated']
	return date+","+ILS+","+USD
if (os.path.exists(output)):
	print("*    The last output file will be overwriten? ")
	print("*    that's the time to copy it's else where ")
	input( "*         Press Enter To Confiram.")

with open(output,'w',encoding="utf-8") as writer:
    writer.write("TIME,ILS,USD \n")
    while True:
        writer.write(query()+"\n")
        writer.flush()
        time.sleep(interval)
