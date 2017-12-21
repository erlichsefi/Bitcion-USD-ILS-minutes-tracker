installation steps:
1. Download & install python 3 or higher  https://www.python.org/downloads/
	 - you can follow this link: https://www.youtube.com/watch?v=dX2-V2BocqQ 
2. Add python to Path
     - you can follow this link: https://www.youtube.com/watch?v=Y2q_b4ugPWk 
3. Open an a "commend propmt"
	3.1 type "cmd" at start menu and open it.
	3.2.type each one separately  of the commends below and wait:
		python -m pip install requests
		python -m pip install selenium
		
******starting a script*******
1. locate the folder with the scripts.
2. copy it path of the folder(on the top)
3. open the Commend Propmt and type "cd" and then paste the path to the folder.
	for exemple "cd c:\this\is\path\to\the\folder"
4. to run a script simply type "python" and the name of the script.
  - options: 
"python bit2c.py" to collect ILS-BTC from https://www.bit2c.co.il/Order/index
"python inversting.py"  to collect USD-BTC from https://il.investing.com/currencies/btc-usd
"python api.py" to collect USD-BTC and ILS-BTC from https://api.coindesk.com/v1/bpi/currentprice/ILS.json

Note: the scripts are collect thus values while thay are open.
	  if you will exit the commend propmt it will STOP COLLECTING


