import argparse
import requests


class WeatherService:
    GEO_URL = "https://geocoding-api.open-meteo.com/v1/search"
    WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

    def get_weather(self, city: str) -> dict:

        try:
            geo = requests.get(
                self.GEO_URL,
                params={"name": city, "count": 1},
                timeout=5
            )
            geo.raise_for_status()
            results = geo.json().get("results")
            if not results:
                raise ValueError(f"找不到城市：{city}")

            lat = results[0]["latitude"]
            lon = results[0]["longitude"]
            name = results[0]["name"]

        except requests.exceptions.Timeout:
            raise Exception("请求超时,请检查网络")
        except requests.exceptions.ConnectionError:
            raise Exception("网络连接失败")
        except ValueError as e:
            raise Exception(str(e))

        try:
            weather = requests.get(
                self.WEATHER_URL,
                params={
                    "latitude":        lat,
                    "longitude":       lon,
                    "current_weather": "true",
                    "hourly":          "relativehumidity_2m,apparent_temperature"
                },
                timeout=5
            )
            weather.raise_for_status()
            data = weather.json()
            data["_city_name"] = name
            return data

        except requests.exceptions.Timeout:
            raise Exception("天气请求超时")
        except requests.exceptions.ConnectionError:
            raise Exception("网络连接失败")

    def format_weather(self, data, lang="cn"):

        try:
            current = data["current_weather"]
            temperature = current["windspeed"]
            temp_c = current["temperature"]
            wind_speed = current["windspeed"]
            city_name = data.get("_city_name", "")

            humidity = data["hourly"]['relativehumidity_2m'][0]
            feels_like = data["hourly"]["apparent_temperature"][0]

            temp_f = round(int(temperature) * 9/5 + 32, 1)
            feels_f = round(int(feels_like) * 9/5 + 32, 1)

        except (KeyError, IndexError) as e:
            raise Exception(f"天气数据解析失败:{e}")

        if lang == "en":
            return (
                f"\n====== {city_name} Current Weather ======\n"
                f"Temperature : {temp_c}°C / {temp_f}°F\n"
                f"Feels Like  : {feels_like}°C / {feels_f}°F\n"
                f"Humidity    : {humidity}%\n"
                f"Wind Speed  : {wind_speed} km/h\n"
                f"Source      : open-meteo.com\n"
            )
        else:
            return (
                f"\n====== {city_name} 当前天气 ======\n"
                f"当前温度 : {temp_c}°C / {temp_f}°F\n"
                f"体感温度 : {feels_like}°C / {feels_f}°F\n"
                f"湿度     : {humidity}%\n"
                f"风速     : {wind_speed} km/h\n"
                f"数据来源 : open-meteo.com\n"
            )


def main():
    parser = argparse.ArgumentParser(
        description="命令行天气查询工具"
    )

    parser.add_argument(
        "city",
        help="城市名称，例如 Beijing、Shanghai、Singapore"
    )
    parser.add_argument(
        "--lang",
        choices=["cn", "en"],
        default="cn",
        help="显示语言: cn 中文 (默认), en 英文"
    )
    args = parser.parse_args()

    service = WeatherService()

    try:
        data = service.get_weather(args.city)
        result = service.format_weather(data, args.lang)
        print(result)

    except Exception as e:
        print(f"错误：{e}")


if __name__ == "__main__":
    main()
