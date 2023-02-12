def find_name(phone_number):
    contactTable=[{"name":"Ahmed","Phone":"0551112222"},{"name":"Saad","Phone":"0551113333"},{"name":"Sultan","Phone":"0551114444"},{"name":"Morad","Phone":"0551115555"},{"name":"Abdullah","Phone":"0551116666"}]
    if not phone_number.isdigit() or len(phone_number) != 10:
        return "This is an invalid number"
    for contact in contactTable:
        if contact['Phone'] == phone_number:
            return "The owner of the number " + phone_number + " is " + contact['name']
    return "Sorry, the number is not found"

