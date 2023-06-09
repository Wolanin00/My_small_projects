from flight_data import FlightData
import requests

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "REMOVED"


class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        location_headers = {'apikey': TEQUILA_API_KEY}
        location_param = {
            'term': city_name,
            'location_types': 'city'
        }
        response = requests.get(url=location_endpoint, params=location_param, headers=location_headers)
        location_data = response.json()["locations"]
        code = location_data[0]['code']
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        search_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        location_headers = {'apikey': TEQUILA_API_KEY}
        location_param = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(
            url=search_endpoint,
            params=location_param,
            headers=location_headers
        )

        try:
            data = response.json()['data'][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
