class Contact:
    def __init__(self, f_name, l_name, city, state, zip_code, phone, email):
        self.f_name = f_name
        self.l_name = l_name
        self.city = city
        self.state = state 
        self.zip_code = zip_code
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {
                'First Name': self.f_name,
                'Last Name': self.l_name,
                'City': self.city,
                'State': self.state,
                'Zip Code': self.zip_code,
                'Phone Number': self.phone,
                'Email': self.email
            }