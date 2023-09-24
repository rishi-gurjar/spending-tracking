import requests
import json

url = "https://api.usaspending.gov/api/v2/search/spending_by_award/"
headers = {'Content-Type': 'application/json', 'API_KEY': 'YOUR_API_KEY'}
payload = {
    "filters": {
        "time_period": [{"start_date": "2023-01-01", "end_date": "2023-12-31"}],
        "award_type_codes": ["C"]  # C for Contracts
    },
    "fields": ["Award ID", "Award Amount", "Awarding Agency", "Funding Agency", "Award Type", "Recipient Name"],
    "limit": 100  # Number of results to return
}

response = requests.post(url, headers=headers, json=payload)
data = json.loads(response.text)
#print("RESPONSE TEXT", response.text)

# Extract and print company names, award amount, and action date
for award in data['results']:
    print(f"Award ID: {award['Award ID']}, Amount: {award['Award Amount']}, Awarding Agency: {award['Awarding Agency']}, Funding Agency: {award['Funding Agency']}, Award Type: {award['Award Type']}, Recipient: {award['Recipient Name']}")

# This lists the id, amount, awarding agency, funding agency, award type (null), and recipient for companies that recieved government contracts