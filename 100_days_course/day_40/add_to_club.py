import requests

print("Welcome in Mathew's Flights Family Club.",
      "We find the best flight deals and email you.",
      sep='\n')
first_name = input("What is your first name? \n").title()
last_name = input("What is your last name? \n").title()

email = 'email1'
email_confirmation = 'email2'

while email != email_confirmation:
    email = input("What is your email? \n")
    email_confirmation = input("Type your email again. \n")

print("You're in the Club! 🛫")


sheety_endpoint = "https://api.sheety.co/001804097fe74cbf3a51ce2c254f8d74/flightDealsCopy/users"
sheety_bearer = "REMOVED"
sheety_headers = {
    'Authorization': sheety_bearer
}
sheety_param = {
    'user': {
        'firstName': first_name,
        'lastName': last_name,
        'email': email
    }
}
response = requests.post(
    url=sheety_endpoint,
    json=sheety_param,
    headers=sheety_headers
)
print(response.text)
