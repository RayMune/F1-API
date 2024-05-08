import requests

# Define the URL for the drivers' standings API endpoint
url = "https://ergast.com/api/f1/current/driverStandings.json"

# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Extract the JSON data from the response
    data = response.json()
    
    # Extract the standings data
    standings = data['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']
    
    # Print the top 5 drivers and their points
    print("Top 5 Drivers' Standings:")
    for i in range(5):
        driver = standings[i]['Driver']
        points = standings[i]['points']
        print(f"{i+1}. {driver['givenName']} {driver['familyName']} - {points} points")
else:
    print("Failed to retrieve data. Status code:", response.status_code)
    