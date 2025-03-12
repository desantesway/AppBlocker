from adult import get_adult

def always():
    return '''
{
    "vacation":false,
    "week":{
        "every_day":[],
        "monday": [],
        "tuesday": [],
        "wednesday": [],
        "thursday": [],
        "friday": [],
        "saturday": [],
        "sunday": []
    }
  }
'''

def schedule():
    return '''
{
    "vacation":false,
    "week":{
        "every_day":[
            {
                "start": "20:00",
                "end": "06:00",
                "apps": "daily_apps",
                "sites": "?www.reddit.com?"
            },
            {
                "start": "00:00",
                "end": "00:00",
                "apps": "?stremio?duckduckgo?",
                "sites": "daily_sites"
            },
            {
                "start": "00:00",
                "end": "17:00",
                "apps": "?steam?hydra?"
            },
            {
                "start": "20:00",
                "end": "23:59",
                "apps": "?steam?hydra?"
            }
        ],
        "monday": [],
        "tuesday": [],
        "wednesday": [],
        "thursday": [],
        "friday": [],
        "saturday": [],
        "sunday": []
    }
  }
'''

def adult():
    adult_list = []
    for line in get_adult().split('\n'):
        if "0.0.0.0" in line:
            adult_list.append(line.split(" ")[1])
    return adult_list

def custom_sites():
    return [
        "facebook.com", "www.facebook.com" , "login.facebook.com", "www.login.facebook.com", "static.ak.connect.facebook.com",
        "www.static.ak.connect.facebook.com", "fbcdn.net", "www.fbcdn.net", "static.ak.fbcdn.net", "www.static.ak.fbcdn.net", "fbcdn.com", "www.fbcdn.com",
        "youtube.com", "www.youtube.com", "instagram.com", "www.instagram.com", "i.instagram.com", "tiktok.com", "www.tiktok.com"
            ]

def custom_apps():
    return [
        "spotify", "chrome", "firefox", "opera", "DRAGON BALL", "Red Dead Redemption", "GTA", "GRAND THEFT AUTO", "Spider-Man", "Celeste",
        "balatro", "uno", "ubisoft", "insaniquarium", "sonic", "Stardew Valley", "Neighbours back From Hell", "Spore", "Hollow Knight", "Ghost of Tsushima"
            ]
