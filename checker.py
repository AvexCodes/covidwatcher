import requests
def check(country: str, updated: int):
    """
        event will be fired every 5 minutes to check if there is a new cases for selected country
    """
    r = requests.get('https://disease.sh/v3/covid-19/countries/{}'.format(country))
    if r.status_code != 200:
        return {"status": r.status_code}
    json = r.json()
    cases = json['cases']
    if updated != json['updated']:
        return {"status": r.status_code, "updated": True, "cases":cases, "epoch":json['updated']}
    else:
        return {"status": r.status_code, "updated": False}
    
def getCurrent(country: str):
    r = requests.get("https://disease.sh/v3/covid-19/countries/{}".format(country))
    return r.json()

def getCurrentVersion():
    r = requests.get("https://raw.githubusercontent.com/AvexCodes/covidwatcher/master/version.json")
    r = r.json()
    return r
