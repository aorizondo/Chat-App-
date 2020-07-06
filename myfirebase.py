import json
import requests
from kivy.app import App

class Firebase():
    wak = "AIzaSyC8yPB-q8yyBoSk6QjGkNvntZflWQe_EUg" # web api key
    def sign_up(self,email, password):
        try:
            # Send these 4 parameters to the firebase
            # Firebase will return LocalId, idToken and RefreshToken
            signup_url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key=" + self.wak
            data_  = {"email": email, "password": password, "returnSecureToken": True}
            signup_request = requests.post(signup_url, data = data_)
            MyApp = App.get_running_app()
            sign_up_data = json.loads(signup_request.content.decode())
            print(signup_request.ok)
            print(signup_request.content.decode())
            
            if signup_request.ok == True:
                refresh_token = sign_up_data['refreshToken']
                localId = sign_up_data["localId"]
                idToken = sign_up_data["idToken"]
                # Save refreshToken to a file
                with open("refresh_token.txt", "w") as f:
                    f.write(refresh_token)

                with open('email.txt', 'w') as f:
                    f.write(email)

                with open('level.txt', 'r') as f:
                    level = f.read()
                # Save localId to a variable in the main class
                MyApp.local_id = localId
                # Save idtoken to a variable in the main class
                MyApp.id_token = idToken
                # create a new key in the database
                # my_data = 'user'
                my_data = '{"Full_name": "xxxxxx", "messages": ""}'
                cc=requests.patch("https://chatapp-80ce4.firebaseio.com/" + level + ".json" , data= my_data)
                MyApp.ChangeScreen("home")
                
                
                # print("patch is ", test.ok)
            
            if signup_request.ok == False:
                error_data = json.loads(signup_request.content.decode())
                error_message  = error_data["error"]["message"]
                MyApp.root.ids["error_label"].text = error_message
                
           
        except Exception as e:
            print(e)
            
            # LET THE SYSTEM ALERT WHEN THERE IS NO INTERNET CONNECTION
            App.get_running_app().root.ids["error_label"].text = "NO INTERNET CONNECTION"

    def exchange_refresh_token(self, refresh_token):
        refresh_url = "https://securetoken.googleapis.com/v1/token?key=" + self.wak        
        refresh_payload = '{"grant_type":"refresh_token","refresh_token": "%s"}' % refresh_token        
        refresh_req = requests.post(refresh_url, data=refresh_payload)
        id_token = refresh_req.json()["id_token"]
        localId = refresh_req.json()["user_id"]
        # print('here is what i want to see ',refresh_req.content.decode())
        return id_token, localId

   
