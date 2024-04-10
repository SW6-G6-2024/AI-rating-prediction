def fail():
    return """{
    "pisteList": [
        {"pisteId": 1},
        {"pisteId": 3},
        {"pisteId": 5}
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
    "year": 2023,
    "month": 2,
    "day": 3,
    "hour": 7
    }"""


def fail1():
    return """{
    "pisteList": [
        {"pisteId": 1},
        {"pisteId": 3},
        {"pisteId": 5}
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
    "month": 2,
    "day": 3,
    "hour": 7
    }"""


def succ():
    return """{
    "pisteList": [
        {"pisteId": 1},
        {"pisteId": 3},
        {"pisteId": 5}
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
    "year": 2023,
    "month": 2,
    "day": 3,
    "hour": 7
    }"""