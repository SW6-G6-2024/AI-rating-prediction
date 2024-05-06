def fail():
    return """{
    "pisteList": [
        {
          "id": 1,
          "direction": 9.34534636
        },
        {
          "id": 3,
          "direction": 2.34534636
        },
        {
          "id": 5,
          "direction": 180.34534636
        }
    ],
    "weather": {
        "temperature": 1,
        "weatherCode": 2,
        "windSpeed": 9.407048617566698,
        "windDirection": 158,
        "snowfall": 0,
        "snowDepth": 68.12066453421069,
        "rain": 0,
        "visibility": 1859.8565326225944
    },
    "date": {
        "year": 2023,
        "month": 2,
        "day": 3,
        "hour": 7
    }
    }"""


def fail1():
    return """{
    "pisteList": [
        {
          "id": 1,
          "direction": 9.34534636
          },
        {
          "id": 3,
          "direction": 2.34534636
          },
        {
          "id": 5,
          "direction": 180.34534636
          }
    ],
    "weather": {
        "temperature": 1.2,
        "weatherCode": 2,
        "windSpeed": 9.407048617566698,
        "windDirection": 158,
        "snowfall": 0,
        "snowDepth": 68.12066453421069,
        "rain": 0,
        "visibility": 1859.8565326225944
    },
    "date": {
        "year": 2023,
        "month": 2,
        "day": 3,
    }
    }"""


def succ():
    return """{
    "pisteList": [
        {
          "id": 1,
          "direction": 9.34534636
          },
        {
          "id": 3,
          "direction": 2.34534636
          },
        {
          "id": 5,
          "direction": 180.34534636
          }
    ],
    "weather": {
        "temperature": 7.8,
        "weatherCode": 2,
        "windSpeed": 9.407048617566698,
        "windDirection": 158,
        "snowfall": 0,
        "snowDepth": 68.12066453421069,
        "rain": 0,
        "visibility": 1859.8565326225944
    },
    "date": {
        "year": 2023,
        "month": 2,
        "day": 3,
        "hour": 7
    }
    }"""
