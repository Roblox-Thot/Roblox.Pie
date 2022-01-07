import requests


def get_xsrf(cookie=""):
    """Get the Xsrf token from Roblox with or without a cookie

    :parameter cookie Roblox Cookie  (optional)
    :return xsrf_header for requests to Roblox"""
    xsrf_header = requests.post("https://auth.roblox.com/v2/login", headers={
        "X-CSRF-TOKEN": ""
    }, cookies={
        '.ROBLOSECURITY': cookie
    }).headers['x-csrf-token']
    return xsrf_header
