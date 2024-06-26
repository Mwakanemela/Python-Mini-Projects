import phonenumbers
# from phonenumbers import carrier
from phonenumbers import geocoder

number = "+265886473493"
# The PhoneNumber object that parse produce
phone_number = phonenumbers.parse(number)

 # information about the location that corresponds to a phone number
print(geocoder.description_for_number(phone_number, "en"))