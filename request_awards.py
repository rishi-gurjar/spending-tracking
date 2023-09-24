# This lists the id, amount, awarding agency, funding agency, award type (null), and recipient for companies that recieved government contracts

import requests
import json
import csv

# Initialize variables
url = "https://api.usaspending.gov/api/v2/search/spending_by_award/"
headers = {'Content-Type': 'application/json', 'API_KEY': 'YOUR_API_KEY'}
page = 1
limit = 100

# Initialize CSV file
csv_file_path = 'awards.csv'
fieldnames = ["Award ID", "Award Amount", "Awarding Agency", "Funding Agency", "Start Date", "End Date", "Recipient Name"]

# Write header to CSV
with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

while True:
    payload = {
        "filters": {
            "time_period": [{"start_date": "2023-01-01", "end_date": "2023-12-31"}],
            "award_type_codes": ["C"]
        },
        "fields": fieldnames,
        "limit": limit,
        "page": page
    }

    response = requests.post(url, headers=headers, json=payload)
    data = json.loads(response.text)

    if 'results' not in data:
        print("No more results or an error occurred.")
        break

    # Append to CSV
    with open(csv_file_path, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for award in data['results']:
            writer.writerow({
                "Award ID": award.get('Award ID', 'N/A'),
                "Award Amount": award.get('Award Amount', 'N/A'),
                "Awarding Agency": award.get('Awarding Agency', 'N/A'),
                "Funding Agency": award.get('Funding Agency', 'N/A'),
                "Start Date": award.get('Start Date', 'N/A'),
                "End Date": award.get('End Date', 'N/A'),
                "Recipient Name": award.get('Recipient Name', 'N/A')
            })

    if len(data['results']) < limit:
        print("Reached the end of the data.")
        break

    total_count = page*100
    print(f"Page {page} done   Total count: {total_count}")
    page += 1

# Read and print CSV to verify
print("Reading and printing CSV content:")
with open(csv_file_path, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(', '.join(row))
