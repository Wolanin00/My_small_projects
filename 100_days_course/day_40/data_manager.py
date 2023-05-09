import requests

sheet_bearer = "REMOVED"
prices_sheet_endpoints = "https://api.sheety.co/001804097fe74cbf3a51ce2c254f8d74/flightDealsCopy/prices"
users_sheet_endpoints = "https://api.sheety.co/001804097fe74cbf3a51ce2c254f8d74/flightDealsCopy/users"
sheet_headers = {
    "Authorization": sheet_bearer
}


class DataManager:

    def __init__(self):
        self.customer_data = None
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=prices_sheet_endpoints, headers=sheet_headers)
        sheet_data = response.json()
        self.destination_data = sheet_data['prices']
        return self.destination_data

    def get_customer_emails(self):
        response = requests.get(url=users_sheet_endpoints, headers=sheet_headers)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    'iataCode': city['iataCode']
                }
            }
            response = requests.put(
                url=f"{prices_sheet_endpoints}/{city['id']}",
                headers=sheet_headers,
                json=new_data
            )
            print(response.text)
