import pandas as pd
import matplotlib.pyplot as plt
import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv('awards.csv')

def get_stock_ticker_fmp(api_key, company_name):
#    base_url = f"https://financialmodelingprep.com/api/v3/search?query={company_name}&limit=10&exchange=NASDAQ&apikey={api_key}"
    print("Api key is", api_key)
    base_url = f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{company_name}?&limit=120&apikey={api_key}"
    response = requests.get(base_url)
    data = response.json()
    return data

    # Assuming the first match is the most relevant
#    if len(data) > 0:
#        return data
#    else:
#        return None

api_key = os.getenv("FMP_KEY")
company_name = "AAPL"

data = get_stock_ticker_fmp(api_key, company_name)
print(json.dumps(data, indent=2))
