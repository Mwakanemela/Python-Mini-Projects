import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder

number = "+265886473493"
phone_number = phonenumbers.parse(number)
print(geocoder.description_for_number(phone_number, "en"))