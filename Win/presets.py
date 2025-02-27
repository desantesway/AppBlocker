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
                "start": "21:00",
                "end": "06:00",
                "apps": "daily_apps",
                "sites": "daily_sites"
            },{
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

def adult():
    return ""

def custom_sites():
    return [
        "facebook.com", "www.facebook.com" , "login.facebook.com", "www.login.facebook.com", "static.ak.connect.facebook.com",
        "www.static.ak.connect.facebook.com", "fbcdn.net", "www.fbcdn.net", "static.ak.fbcdn.net", "www.static.ak.fbcdn.net", "fbcdn.com", "www.fbcdn.com",
        "youtube.com", "www.youtube.com", "instagram.com", "www.instagram.com", "reddit.com", "www.reddit.com", "i.instagram.com", "tiktok.com", "www.tiktok.com"
            ]

def custom_apps():
    return [
        "spotify", "chrome", "firefox", "opera", "DRAGON BALL", "Red Dead Redemption", "GTA", "GRAND THEFT AUTO", "Spider-Man", "Celeste",
        "balatro", "uno", "ubisoft", "insaniquarium", "sonic", "Stardew Valley", "Neighbours back From Hell", "Spore", "Hollow Knight", "Ghost of Tsushima"
            ]
