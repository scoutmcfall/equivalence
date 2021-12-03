import requests
import datetime
def get_report():
    data = requests.get("https://www2.seattle.gov/fire/IncidentSearch/incidentSearchResults.asp")
    print(data)
    return data
    
print(get_report)