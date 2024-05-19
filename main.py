import requests
import ipinfo
token = 'c7d8b6fbdc8dca'
print("WARNING: LOCATIONS ARE RETRIVED FROM THE ISP, MEANING THAT YOU CANNOT GET THE ADDRESS, THIS ALSO MEANS THAT THE PERSON DOES NOT LIVE WHERE THE IP IS LOCATED")
ip = input("IP ADDRESS:\n")
print("Advanced mode or Simple mode?")
mode = input("Advanced for Advanced or Simple for Simple\n").lower()
if mode == "simple":
    handler = ipinfo.getHandler(token)
    details = handler.getDetails(ip)
    substring1 = "domain"
    print("Country: ", details.country_name)
    print("Post Code: ", details.postal)
    print("Region: ", details.region)
    print("City: ", details.city)

    if 'domain' in locals():
        print("Domain: ", details.domain)
    print("Coordinates: ", details.loc)
    if 'abuse' in locals():
        print("Personal Information: ", details.abuse)
    else:
         print("No personal information found, this is common")
elif mode == "advanced":
     handler = ipinfo.getHandler(token)
     details = handler.getDetails(ip)
     print(details.all)
input("Press Enter to exit")