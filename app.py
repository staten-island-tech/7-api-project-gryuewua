import requests
def catfacts(amount):
    for a in amount:
        response = requests.get(f"https://meowfacts.herokuapp.com/?count={a}")
        if response.status_code != 200:
            print("Error fetching data!")
            return None
        fact = response.json()
        print(fact)

print(catfacts("5"))