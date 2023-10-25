from geopy.geocoders import Nominatim
import requests
import geohash
from PIL import Image, ImageDraw, ImageOps
from io import BytesIO
import base64
import uuid


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


def arbepoint2polygonpoints(image_size, crop_data):
    increase_percentage = 3 / 100.0

    increase_width = image_size[0] * increase_percentage
    increase_height = image_size[1] * increase_percentage

    if crop_data:
        x1 = max(0, image_size[0] * crop_data["cropX"] - increase_width)
        y1 = max(0, image_size[1] * crop_data["cropY"] - increase_height)
        x2 = min(
            image_size[0],
            image_size[0] * (crop_data["cropX"] + crop_data["cropW"]) + increase_width,
        )
        y2 = min(
            image_size[1],
            image_size[1] * (crop_data["cropY"] + crop_data["cropH"]) + increase_height,
        )
        return (x1, y1, x2, y2)
    else:
        return None


# TODO crop 데이터가 풀사이즈면 안돌게 만들어야함
def show_draw_crop(image_url, crop):
    if image_url:
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))
        draw = ImageDraw.Draw(image, "RGBA")
        image_size = image.size
        polygon_points = arbepoint2polygonpoints(image_size, crop)
        fill_color = (255, 0, 0)
        if polygon_points:
            draw.rectangle(polygon_points, outline=fill_color, width=3)

        image_byte_array = BytesIO()
        image.save(image_byte_array, format="PNG")
        image_byte_array.seek(0)
        image_data = base64.b64encode(image_byte_array.getvalue()).decode("utf-8")

        return image_data
    else:
        return ""


def choice_type(shire):
    if shire == "homegood" or shire == "others":
        type_ = "t800"
    elif shire == "place":
        type_ = "mallorn"
    else:
        type_ = None
    return type_


def is_valid_uuid(uuid_str):
    try:
        uuid_obj = uuid.UUID(uuid_str)
        return True
    except ValueError:
        return False
