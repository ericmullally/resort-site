from django.shortcuts import render

card_activities= [
    {
        "name":"Relaxing",
        "img": "/room_shot.jpeg", 
        "url" : "rooms"
    },
    {
        "name":"Swimming",
        "img": "/pool_shot.jpeg", 
        "url" : "pool"
    },
    {
        "name":"Hiking",
        "img": "/outdoor_pic.jpeg", 
        "url" : "hicking"
    },
    {
        "name":"Surffing",
        "img": "/ocean_shot.jpeg", 
        "url" : "surffing"
    }
    ]


def index(request):
    return render(request, "resort/index.html", {
    "data" : card_activities
    })

def booking(request):
    pass

def activities(request , slug):
    return render(request, "resort/activities.html")
