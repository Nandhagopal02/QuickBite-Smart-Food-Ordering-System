from User import user
class UserManager:
    __users = []
    
    @classmethod
    def AddUser(cls, usser):
        if isinstance(usser, user):
            cls.__users.append(usser)
            print("You have been Successfully Registered")
        else:
            print("Invalid Choice")

    @classmethod
    def FindUser(cls, mailid, password):
        for user in cls.__users:
            if user.MailId == mailid and user.Password == password:
                return user
        return None
