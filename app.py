import requests
def catfacts(amount):
    response = requests.get(f"https://meowfacts.herokuapp.com/?count={amount}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    data = response.json

print(catfacts("1"))