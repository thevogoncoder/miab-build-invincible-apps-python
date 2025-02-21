from temporalio import activity
import requests


@activity.defn
def get_ip() -> str:
    response = requests.get("https://icanhazip.com")
    response.raise_for_status()
    return response.text.strip()

@activity.defn
def get_location_info(ip: str) -> str:
    response = requests.get(f"http://ip-api.com/json/{ip}")
    response.raise_for_status()
    result = response.json()
    return f"{result["city"]}, {result["regionName"]}, {result["country"]}"
