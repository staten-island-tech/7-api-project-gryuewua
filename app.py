import requests
def catfacts(amount):
    response = requests.get(f"https://meowfacts.herokuapp.com/?count={amount}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    fact = response.json()
    return fact

print(catfacts("10"))