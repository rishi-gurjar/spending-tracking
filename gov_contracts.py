import requests
import json
# Define the API endpoint and parameters
endpoint_append = "awards/count/federal_account/"
endpoint = (f"https://api.usaspending.gov/api/v2/{endpoint_append}")
print("NAME", endpoint)

toptier_code = "ASST_NON_NNX17AJ96A_8000"  # Replace with the agency's toptier code
#fiscal_year = 2015  # Replace with the desired fiscal year
#params = '"fiscal_year": fiscal_year'
# Make the API request
response = requests.get(f"{endpoint}{toptier_code}/", params={})

# Check if the request was successful
if response.status_code == 200:
    try:
        # Parse the JSON response
        data = json.loads(response.text)
        
        # Print the data
        print(json.dumps(data, indent=4))
    except json.JSONDecodeError:
        print("Failed to decode JSON.")
else:
    print(f"Failed to get data. HTTP Status Code: {response.status_code}")
