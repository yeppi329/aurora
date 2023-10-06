from geopy.geocoders import Nominatim
import requests
import geohash


# Geohash를 좌표로 변환
def geohash_to_coordinates(geohash_data):
    location = geohash.decode(geohash_data)
    if location:
        return f"{location[0]}, {location[1]}"
    else:
        return None


# 좌표를 주소로 변환
def coordinates_to_address(coordinates):
    lat, lon = coordinates
    url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}&zoom=18&addressdetails=1"
    response = requests.get(url)
    data = response.json()
    if "address" in data:
        return data["address"]
    else:
        return None


# 좌표를 주소로 변환
def geocoding_reverse(lat_lng_str):
    geolocoder = Nominatim(user_agent="South Korea", timeout=None)
    address = geolocoder.reverse(lat_lng_str)

    return address
