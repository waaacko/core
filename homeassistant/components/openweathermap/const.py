"""Consts for the OpenWeatherMap."""
from homeassistant.components.weather import (
    ATTR_FORECAST_CONDITION,
    ATTR_FORECAST_PRECIPITATION,
    ATTR_FORECAST_TEMP,
    ATTR_FORECAST_TEMP_LOW,
    ATTR_FORECAST_TIME,
    ATTR_FORECAST_WIND_BEARING,
    ATTR_FORECAST_WIND_SPEED,
)
from homeassistant.const import (
    DEGREE,
    DEVICE_CLASS_HUMIDITY,
    DEVICE_CLASS_PRESSURE,
    DEVICE_CLASS_TEMPERATURE,
    DEVICE_CLASS_TIMESTAMP,
    LENGTH_MILLIMETERS,
    PERCENTAGE,
    PRESSURE_PA,
    SPEED_METERS_PER_SECOND,
    TEMP_CELSIUS,
)

DOMAIN = "openweathermap"
DEFAULT_NAME = "OpenWeatherMap"
DEFAULT_LANGUAGE = "en"
DEFAULT_FORECAST_MODE = "freedaily"
ATTRIBUTION = "Data provided by OpenWeatherMap"
CONF_LANGUAGE = "language"
ENTRY_NAME = "name"
ENTRY_FORECAST_COORDINATOR = "forecast_coordinator"
ENTRY_WEATHER_COORDINATOR = "weather_coordinator"
ATTR_API_PRECIPITATION = "precipitation"
ATTR_API_DATETIME = "datetime"
ATTR_API_WEATHER = "weather"
ATTR_API_TEMPERATURE = "temperature"
ATTR_API_WIND_SPEED = "wind_speed"
ATTR_API_WIND_BEARING = "wind_bearing"
ATTR_API_HUMIDITY = "humidity"
ATTR_API_PRESSURE = "pressure"
ATTR_API_CONDITION = "condition"
ATTR_API_CLOUDS = "clouds"
ATTR_API_RAIN = "rain"
ATTR_API_SNOW = "snow"
ATTR_API_WEATHER_CODE = "weather_code"
ATTR_API_FORECAST = "forecast"
ATTR_API_THIS_DAY_FORECAST = "this_day_forecast"
SENSOR_NAME = "sensor_name"
SENSOR_UNIT = "sensor_unit"
SENSOR_DEVICE_CLASS = "sensor_device_class"
UPDATE_LISTENER = "update_listener"
COMPONENTS = ["sensor", "weather"]
FORECAST_MODES = ["hourly", "daily", "freedaily"]
MONITORED_CONDITIONS = [
    ATTR_API_WEATHER,
    ATTR_API_TEMPERATURE,
    ATTR_API_WIND_SPEED,
    ATTR_API_WIND_BEARING,
    ATTR_API_HUMIDITY,
    ATTR_API_PRESSURE,
    ATTR_API_CLOUDS,
    ATTR_API_RAIN,
    ATTR_API_SNOW,
    ATTR_API_CONDITION,
    ATTR_API_WEATHER_CODE,
]
FORECAST_MONITORED_CONDITIONS = [
    ATTR_FORECAST_CONDITION,
    ATTR_FORECAST_PRECIPITATION,
    ATTR_FORECAST_TEMP,
    ATTR_FORECAST_TEMP_LOW,
    ATTR_FORECAST_TIME,
    ATTR_FORECAST_WIND_BEARING,
    ATTR_FORECAST_WIND_SPEED,
]
LANGUAGES = [
    "af",
    "al",
    "ar",
    "az",
    "bg",
    "ca",
    "cz",
    "da",
    "de",
    "el",
    "en",
    "es",
    "eu",
    "fa",
    "fi",
    "fr",
    "gl",
    "he",
    "hi",
    "hr",
    "hu",
    "id",
    "it",
    "ja",
    "kr",
    "la",
    "lt",
    "mk",
    "nl",
    "no",
    "pl",
    "pt",
    "pt_br",
    "ro",
    "ru",
    "se",
    "sk",
    "sl",
    "sp",
    "sr",
    "sv",
    "th",
    "tr",
    "ua",
    "uk",
    "vi",
    "zh_cn",
    "zh_tw",
    "zu",
]
CONDITION_CLASSES = {
    "cloudy": [803, 804],
    "fog": [701, 741],
    "hail": [906],
    "lightning": [210, 211, 212, 221],
    "lightning-rainy": [200, 201, 202, 230, 231, 232],
    "partlycloudy": [801, 802],
    "pouring": [504, 314, 502, 503, 522],
    "rainy": [300, 301, 302, 310, 311, 312, 313, 500, 501, 520, 521],
    "snowy": [600, 601, 602, 611, 612, 620, 621, 622],
    "snowy-rainy": [511, 615, 616],
    "sunny": [800],
    "windy": [905, 951, 952, 953, 954, 955, 956, 957],
    "windy-variant": [958, 959, 960, 961],
    "exceptional": [711, 721, 731, 751, 761, 762, 771, 900, 901, 962, 903, 904],
}
WEATHER_SENSOR_TYPES = {
    ATTR_API_WEATHER: {SENSOR_NAME: "Weather"},
    ATTR_API_TEMPERATURE: {
        SENSOR_NAME: "Temperature",
        SENSOR_UNIT: TEMP_CELSIUS,
        SENSOR_DEVICE_CLASS: DEVICE_CLASS_TEMPERATURE,
    },
    ATTR_API_WIND_SPEED: {
        SENSOR_NAME: "Wind speed",
        SENSOR_UNIT: SPEED_METERS_PER_SECOND,
    },
    ATTR_API_WIND_BEARING: {SENSOR_NAME: "Wind bearing", SENSOR_UNIT: DEGREE},
    ATTR_API_HUMIDITY: {
        SENSOR_NAME: "Humidity",
        SENSOR_UNIT: PERCENTAGE,
        SENSOR_DEVICE_CLASS: DEVICE_CLASS_HUMIDITY,
    },
    ATTR_API_PRESSURE: {
        SENSOR_NAME: "Pressure",
        SENSOR_UNIT: PRESSURE_PA,
        SENSOR_DEVICE_CLASS: DEVICE_CLASS_PRESSURE,
    },
    ATTR_API_CLOUDS: {SENSOR_NAME: "Cloud coverage", SENSOR_UNIT: PERCENTAGE},
    ATTR_API_RAIN: {SENSOR_NAME: "Rain", SENSOR_UNIT: LENGTH_MILLIMETERS},
    ATTR_API_SNOW: {SENSOR_NAME: "Snow", SENSOR_UNIT: LENGTH_MILLIMETERS},
    ATTR_API_CONDITION: {SENSOR_NAME: "Condition"},
    ATTR_API_WEATHER_CODE: {SENSOR_NAME: "Weather Code"},
}
FORECAST_SENSOR_TYPES = {
    ATTR_FORECAST_CONDITION: {SENSOR_NAME: "Condition"},
    ATTR_FORECAST_PRECIPITATION: {SENSOR_NAME: "Precipitation"},
    ATTR_FORECAST_TEMP: {
        SENSOR_NAME: "Temperature",
        SENSOR_UNIT: TEMP_CELSIUS,
        SENSOR_DEVICE_CLASS: DEVICE_CLASS_TEMPERATURE,
    },
    ATTR_FORECAST_TEMP_LOW: {
        SENSOR_NAME: "Temperature Low",
        SENSOR_UNIT: TEMP_CELSIUS,
        SENSOR_DEVICE_CLASS: DEVICE_CLASS_TEMPERATURE,
    },
    ATTR_FORECAST_TIME: {
        SENSOR_NAME: "Time",
        SENSOR_DEVICE_CLASS: DEVICE_CLASS_TIMESTAMP,
    },
    ATTR_API_WIND_BEARING: {SENSOR_NAME: "Wind bearing", SENSOR_UNIT: DEGREE},
    ATTR_API_WIND_SPEED: {
        SENSOR_NAME: "Wind speed",
        SENSOR_UNIT: SPEED_METERS_PER_SECOND,
    },
}
