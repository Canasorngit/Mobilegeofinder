import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

number = input("\nEnter Mb Number: ")
print()

ch_number = phonenumbers.parse(number, "CH")
number_country = geocoder.description_for_number(ch_number, "en")

service_provider = phonenumbers.parse(number, "RO")
number_provider = phonenumbers.parse(number, "RO")

phone_number = phonenumbers.parse(number)
time_zone = timezone.time_zones_for_number(phone_number)



print("\nLocation/country: ", number_country)
print("---------------------------")
print("\nTimeZone and Region: ", time_zone)
print("---------------------------")
print("Service/Carrier Provider: ", number_provider)
print("---------------------------")
