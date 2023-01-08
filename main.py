import requests
import ipinfo
token = 'c7d8b6fbdc8dca'
print("WARNING: LOCATIONS ARE RETRIVED FROM THE ISP, MEANING THAT YOU CANNOT GET THE ADDRESS, THIS ALSO MEANS THAT THE PERSON DOES NOT LIVE WHERE THE IP IS LOCATED")
ip = input("IP ADDRESS:\n")
print("Advanced mode or Simple mode?")
mode = input("Advanced for Advanced or Simple for Simple\n")
if mode == "simple":
    handler = ipinfo.getHandler(token)
    details = handler.getDetails(ip)
    substring1 = "domain"
    print(details.country_name)
    print(details.postal)
    print(details.region)
    print(details.city)

    if 'domain' in locals():
        print(details.domain)
    else:
        print("No domain found, possibly innacurate")
    print(details.loc)
    if 'abuse' in locals():
        print(details.abuse)
    else:
         print("No personal information found, this is common")
elif mode == "advanced":
     handler = ipinfo.getHandler(token)
     details = handler.getDetails(ip)
     print(details.all)
input("Press Enter to exit")