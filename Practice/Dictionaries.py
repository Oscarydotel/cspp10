from pprint import pprint
d = {
    "name":"Ocary",
    "birthyear":"August",
    "grade":10,
    "A period":"Global_pt1",
    "B period":"Global_pt2",
    "C period":"AP Chemistry",
    "D period":"English",
    "E period":"Geomitry"
}
for key in d:
    print(d[key])

pprint(d[input("Input:")])