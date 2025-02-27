def always():
    return '''
{
    "vacation":false,
    "week":{
        "every_day":[
            {   
                "disabled": false,
                "start": "00:00",
                "end": "00:00",
                "sites": "?www.youtube.com?"
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

def schedule():
    return '''
{
    "vacation":false,
    "week":{
        "every_day":[
            {
                "disabled": true,
                "start": "00:00",
                "end": "00:00",
                "apps": "?stremio?"
            },
            {
                "disabled": false,
                "start": "20:00",
                "end": "06:00",
                "apps": "daily_apps",
                "sites": "daily_sites"
            },
            {   
                "disabled": false,
                "start": "00:00",
                "end": "00:00",
                "sites": "daily_sites"
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
    return ""

def custom_sites():
    return [
        "facebook.com", "www.facebook.com" , "login.facebook.com", "www.login.facebook.com", "static.ak.connect.facebook.com",
        "www.static.ak.connect.facebook.com", "fbcdn.net", "www.fbcdn.net", "static.ak.fbcdn.net", "www.static.ak.fbcdn.net", "fbcdn.com", "www.fbcdn.com",
        "youtube.com", "www.youtube.com", "instagram.com", "www.instagram.com", "reddit.com", "www.reddit.com", "www.animepahe.ru", "animepahe.ru", "aniwave.se", "aniwave.es", 
        "www.aniwave.se", "www.aniwave.es", "i.instagram.com", "tiktok.com", "www.tiktok.com"
            ]

def custom_apps():
    return [
        "Chess", "Spotify", "Discord", "App Store", "Bomb Rush Cyberfunk", "r2modman", "stremio", "balatro", 
        "/Applications/arc.app", "minecraft", "stremio", "/Applications/Safari.app"
        ]
