default:
	@cat makefile

env:
	python3 -m venv env; . env/bin/activate; pip install --upgrade pip

update: env
	. env/bin/activate; pip install -r requirements.txt
	bash -c "source env/bin/activate && pip install -r requirements.txt"
ygainers.html:
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=10000 'https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200' > ygainers.html

ygainers.csv: ygainers.html
	env/bin/activate && python3 -c "import pandas as pd; raw = pd.read_html('ygainers.html'); raw[0].to_csv('downloaded_data/ygainers.csv')"

wsjgainers.html:
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=10000 https://www.wsj.com/market-data/stocks/us/movers > wsjgainers.html

wsjgainers.csv: wsjgainers.html
	env/bin/activate && python3 -c "import pandas as pd; raw = pd.read_html('wsjgainers.html'); raw[0].to_csv('wsjgainers.csv')"

gainers:
	env/bin/activate && python3 get_gainer.py $(SRC)

lint:
	 env/bin/python -m  pylint bin/normalize_csv.py bin/gainers/base.py bin/gainers/factory.py bin/gainers/wsj.py bin/gainers/yahoo.py get_gainer.py

test: lint
	 env/bin/python -m  pytest -vv tests
