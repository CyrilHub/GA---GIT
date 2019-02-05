import geocoder

destinations = [
"Space Needle",
"Crater Lake",
"Golden Gate Bridge",
"Yosemite National Park",
"Las Vegas, Nevada",
"Grand Canyon National Park",
"Aspen, Colorado Mount Rushmore",
"Yellowstone National Park",
"Sandpoint, Idaho",
"Banff National Park",
"Capilano Suspension Bridge"
]


for desti in destinations:
    g = geocoder.arcgis(desti)
    print(g.latlng) # latlng is a tuple with a length of 2.