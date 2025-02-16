from MainMenu import MainMenu  # Ensure this import is correct
from UserManager import UserManager  # Ensure UserManager is implemented correctly
from User import user  # Ensure this import is correct and User class exists

class LoginSystem:
    def Login(self):
        print("\n" + "=" * 40)
        print("🛎️  Welcome Back! Please Log In")
        print("=" * 40)

        mailid = input("📧 Enter Email ID: ")
        password = input("🔒 Enter Password: ")
        
        user = UserManager.FindUser(mailid, password)
        if user is None:
            print("\n❌ Invalid Email or Password! Please try again.")
        else:
            print("\n✅ Successfully Logged In! 🎉")
            menu = MainMenu()  # Creating the MainMenu object after successful login
            menu.Start()  # Start the MainMenu

    def Register(self):
        print("\n" + "=" * 40)
        print("📝 Create a New Account")
        print("=" * 40)

        name = input("👤 Name: ")
        mobile = input("📞 Mobile No: ")
        mailid = input("📧 Email ID: ")
        password = input("🔒 Password: ")

        new_user = user(name, mobile, mailid, password)
        UserManager.AddUser(new_user)

        print("\n✅ Registration Successful! You can now log in.")

    def GuestLogin(self):
        print("\n🚀 Guest login is under development. Stay tuned!")

    def validateOption(self, option):
        if option == 1:
            self.Login()
        elif option == 2:
            self.Register()
        elif option == 3:
            self.GuestLogin()
        elif option == 4:
            print("\n🍽️ Thank you for using our Food App. See you next time! 👋")
            exit()
        else:
            print("\n❌ Invalid choice, please retry.")

class FoodApp:
    LoginOptions = {1: "🔑 Login", 2: "📝 Register", 3: "🚀 Guest Login", 4: "❌ Exit"}

    @staticmethod
    def Init():
        print("\n" + "=" * 50)
        print("🍔  WELCOME TO ONLINE FOOD ORDERING  🍕")
        print("=" * 50)

        loginSystem = LoginSystem()  # Initialize the LoginSystem here

        while True:
            print("\n📌 **Main Menu**:")
            for option, name in FoodApp.LoginOptions.items():
                print(f"  {option}. {name}")

            try:
                choice = int(input("\n🛎️ Please Enter Your Choice: "))
                loginSystem.validateOption(choice)
            except ValueError:
                print("\n❌ Invalid Input! Please enter a valid number.")

# Running the app
if __name__ == "__main__":
    FoodApp.Init()

