from django.shortcuts import render

card_activities= [
    {
        "name":"Relaxing",
        "img": "/room_shot.jpeg", 
        "url" : "rooms", 
      
        "snippet": """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vel nulla ipsum. Cras cursus finibus urna et porttitor. """,

        "info": """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vel nulla ipsum. Cras cursus finibus urna et porttitor. 
        Praesent id nulla laoreet, fermentum urna nec, congue odio. Curabitur finibus, nunc id condimentum ornare, arcu ligula faucibus nunc, vel finibus nisi metus in felis. 
        Aliquam luctus varius dolor et facilisis. In blandit sapien volutpat nisi ullamcorper, vel dapibus neque finibus. Suspendisse condimentum ex leo, non imperdiet risus placerat et.
        Phasellus dictum, velit non fermentum luctus, eros justo dictum lectus, eget hendrerit mi mi gravida ligula. Donec vulputate massa eu pretium suscipit. 
        Fusce sed mi sit amet nulla laoreet egestas. Maecenas eu vehicula ipsum, nec pulvinar turpis. 
        Pellentesque maximus consequat lectus, in viverra ante imperdiet non. Vivamus dignissim nisi venenatis est feugiat fermentum."""
    },
    {
        "name":"Swimming",
        "img": "/pool_shot.jpeg", 
        "url" : "pool",
       
        "snippet": """Proin consectetur justo nec consectetur sollicitudin. 
        Duis elementum sed neque in laoreet. Proin egestas ligula libero.""",

        "info": """Donec luctus, quam ac luctus porta, dui risus consectetur ligula, nec pulvinar orci justo id est. Proin volutpat enim non ex egestas dignissim. 
        Phasellus laoreet iaculis ante, sit amet aliquet massa fringilla ut. Integer sed felis non risus placerat ultricies non sed dui. 
        Nullam vulputate libero eget enim congue mattis. Nulla auctor tortor euismod rutrum sodales. Phasellus pretium enim ut nisi efficitur placerat. 
        Fusce urna ipsum, maximus sit amet dui et, porta iaculis ante. Donec sit amet ullamcorper mi, eu dignissim mauris. Aenean non neque bibendum, rhoncus nunc vel, aliquet diam.
         Duis convallis id eros vel porta. Nunc vel varius erat. Morbi fringilla libero tortor, quis vulputate odio porttitor blandit"""
    },
    {
        "name":"Hiking",
        "img": "/outdoor_pic.jpeg", 
        "url" : "hicking",
      
        "snippet": """Etiam mollis varius orci at volutpat. Maecenas pretium egestas urna, eu hendrerit erat finibus cursus.
         Sed non condimentum lacus.""",

         "info": """Phasellus auctor feugiat nisi, non finibus eros rhoncus et. 
         Aenean pellentesque mollis rhoncus. Nulla ultrices ante quis odio faucibus vulputate. 
         Etiam ullamcorper ut est ac blandit. Nulla ligula elit, pretium quis urna in, lobortis tristique dui. 
         Phasellus nibh odio, feugiat sed congue in, congue eget diam. 
         Fusce mattis arcu sit amet mauris porttitor consectetur."""
    },
    {
        "name":"Surfing",
        "img": "/ocean_shot.jpeg", 
        "url" : "surffing",

        "snippet": """Phasellus auctor feugiat nisi, non finibus eros rhoncus et. 
        Aenean pellentesque mollis rhoncus. Nulla ultrices ante quis odio. """,

        "info": """Sed aliquet at lorem nec volutpat. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
         Interdum et malesuada fames ac ante ipsum primis in faucibus. Proin accumsan dapibus sem quis porttitor. 
         Vestibulum nec massa lacinia, luctus eros at, luctus elit. Maecenas dui nulla, egestas id dolor quis, tristique pretium massa. 
        In a lacus eu sapien semper viverra. Suspendisse a quam nibh. Morbi facilisis turpis et massa tincidunt, et hendrerit massa euismod"""
    }
    ]


def index(request):
    return render(request, "resort/index.html", {
    "data" : card_activities
    })

def booking(request):
    return render(request, "resort/booking.html")

def activities(request , slug):
    item = next(card for card in card_activities if card["url"] == slug)
    return render(request, "resort/activities.html", {"card": item})
