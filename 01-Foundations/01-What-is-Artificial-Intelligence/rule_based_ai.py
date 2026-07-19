def recommend_activity(is_raining, temperature_celsius):
    """Recommend an activity using explicit decision rules."""
    if is_raining:
        return "Read a book or visit a museum."
    if temperature_celsius < 10:
        return "Take a short walk and wear a warm coat."
    if temperature_celsius > 28:
        return "Go swimming or find a cool indoor activity."
    return "Go for a walk or have a picnic."


def main():
    weather_examples = [
        {"is_raining": True, "temperature_celsius": 14},
        {"is_raining": False, "temperature_celsius": 6},
        {"is_raining": False, "temperature_celsius": 22},
        {"is_raining": False, "temperature_celsius": 31},
    ]

    for weather in weather_examples:
        recommendation = recommend_activity(**weather)
        print(
            f"Raining: {weather['is_raining']}, "
            f"Temperature: {weather['temperature_celsius']}°C"
        )
        print(f"AI recommendation: {recommendation}\n")


if __name__ == "__main__":
    main()
