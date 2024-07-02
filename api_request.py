import requests
import csv

# Initial setup
url = "http://api.mediastack.com/v1/news"
params = {
    'access_key': 'YOUR_API_KEY',
    'categories': '-general,-sports',
    'sort': 'published_desc',
    'limit': 10
}

# Make the GET request
response = requests.get(url, params=params)

# Check the response
if response.status_code == 200:
    data = response.json().get('data', [])
    
    # Create the CSV file
    with open('news.csv', mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(['Title', 'Description', 'URL'])
        
        # Write the data
        for item in data:
            writer.writerow([item['title'], item['description'], item['url']])
    print("Data successfully written to news.csv")
elif response.status_code == 403:
    print("Error 403: Forbidden. Check your API key and permissions.")
    print(response.json())  # Print the response details for debugging
else:
    print(f"Error {response.status_code}: {response.reason}")
    print(response.json())  # Print the response details for debugging
