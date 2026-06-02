import requests

BASE_URL = "https://jsonmock.hackerrank.com/api"


def mostReviewed(city: str) -> str:
    reviews = 0
    restaurant_name = None

    response = requests.get(f"{BASE_URL}/restaurants", {"city": city})
    data = response.json()
    total_pages = data["total_pages"]
    pages_data = [data]

    for page_num in range(2, total_pages + 1):
        response = requests.get(
            f"{BASE_URL}/restaurants", {"city": city, "page": page_num}
        )
        pages_data.append(response.json())

    for page_data in pages_data:
        for restaurant in page_data["data"]:
            user_reviews = int(restaurant["user_rating"]["votes"])
            name = restaurant["name"]

            if user_reviews > reviews:
                reviews = user_reviews
                restaurant_name = name

    return reviews, restaurant_name


def topRatedMovie(origin: str, destination: str) -> str:
    rating = 0
    title = "NONE"

    response = requests.get(f"{BASE_URL}/flights", {"city": city})
    data = response.json()
    total_pages = data["total_pages"]
    pages_data = [data]

    for page_num in range(2, total_pages + 1):
        response = requests.get(
            f"{BASE_URL}/restaurants", {"city": city, "page": page_num}
        )
        pages_data.append(response.json())

    for page_data in pages_data:
        for restaurant in page_data["data"]:
            user_reviews = int(restaurant["user_rating"]["votes"])
            name = restaurant["name"]

            if user_reviews > reviews or (
                user_reviews == reviews and name < restaurant_name
            ):
                reviews = user_reviews
                restaurant_name = name

    return restaurant_name


print(mostReviewed("bangalore"))
