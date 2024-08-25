import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import phonenumbers
from django.conf import settings
import requests

def validate_password(value):
    if len(value) < 8:
        raise ValidationError(
            _("Password must be at least 8 characters long.")
        )
    if not re.search(r"[A-Z]", value):
        raise ValidationError(
            _("Password must contain at least one uppercase letter.")
        )
    if not re.search(r"[a-z]", value):
        raise ValidationError(
            _("Password must contain at least one lowercase letter.")
        )
    if not re.search(r"[0-9]", value):
        raise ValidationError(
            _("Password must contain at least one number.")
        )
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
        raise ValidationError(
            _("Password must contain at least one special character.")
        )

def validate_phone_number_with_country(value):
    try:
        phone_num = phonenumbers.parse(value)
        if not phonenumbers.is_valid_number(phone_num):
            raise ValidationError(
                _("The phone number entered is not valid for the given country code.")
            )
    except phonenumbers.NumberParseException:
        raise ValidationError(
            _("Invalid phone number format.")
        )
    

def validate_address(address):
    endpoint = "https://maps.googleapis.com/maps/api/geocode/json"
    api_key = settings.GOOGLE_MAPS_API_KEY

    params = {
        'address': address,
        'key': api_key
    }
    print(api_key)
    if not api_key:
        raise ValidationError(_("Google Maps API key is missing. Please configure it in your settings."))


    response = requests.get(endpoint, params=params)
    print(response)

    if response.status_code != 200:
        raise ValidationError(
            _("There was an error contacting the Google Maps API. Please try again.")
        )

    result = response.json()
    print("result",result)

    if not result['results']:
        raise ValidationError(
            _("The address entered is not valid. Please provide a valid address.")
        )

    



