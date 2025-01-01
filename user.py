class User:
    # get user id and json file(data) or properties
    def __init__(self, user_id, username=None, password=None, t_fullname=None, t_birthdate=None, t_phone=None, p_fullname=None, p_contact=None, data=None):
        self.id = user_id
        if isinstance(data, dict): 
            self.username = data.get("username", username)
            self.password = data.get("password", password)
            self.t_fullname = data.get("t_fullname", t_fullname)
            self.t_birthdate = data.get("t_birthdate", t_birthdate)
            self.t_phone = data.get("t_phone", t_phone)
            self.p_fullname = data.get("p_fullname", p_fullname)
            self.p_contact = data.get("p_contact", p_contact)
        else:
            self.username = username
            self.password = password
            self.t_fullname = t_fullname
            self.t_birthdate = t_birthdate
            self.t_phone = t_phone
            self.p_fullname = p_fullname
            self.p_contact = p_contact

    # create dict from user to send as json file
    def to_dict(self):
        user_dic = {
            "user_id": self.id,
            "username": self.username,
            "password": self.password,
            "t_fullname": self.t_fullname,
            "t_birthdate": self.t_birthdate,
            "t_phone": self.t_phone,
            "p_fullname": self.p_fullname,
            "p_contact": self.p_contact
        }
        return user_dic
