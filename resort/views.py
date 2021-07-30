from django.shortcuts import render

card_activities= [
    {
        "name":"Relaxing",
        "img": "/room_shot.jpg", 
        "url" : "rooms"
    },
    {
        "name":"Swimming",
        "img": "/pool_shot.jpg", 
        "url" : "pool"
    },
    {
        "name":"Hiking",
        "img": "/outdoor_pic.jpg", 
        "url" : "hicking"
    },
    {
        "name":"Surffing",
        "img": "/ocean_shot.jpg", 
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
