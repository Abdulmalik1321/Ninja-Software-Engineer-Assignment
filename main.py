# from snapchat_ads.client import SnapchatAdsAPI
import random
import sqlite3

class UserSegmentPusher:
    
    def __init__(self, db_path):
        self.db_path = db_path
        # self.api = SnapchatAdsAPI(client_id='client_id', client_secret='client_secret', refresh_token='refresh_token')
        
    def generate_user_info(self):
        id = random.randint(1, 1000)
        user_info = {
            'id': id,
            'username': 'User' + str(id),
            'email': 'User' + str(id) + '@example.com'
        }
        return user_info
    def store_user_info(self, user_info):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("INSERT INTO users VALUES (?, ?, ?)", (user_info['id'], user_info['username'], user_info['email']))
        conn.commit()
        conn.close()
    

if __name__ == "__main__":
    pusher = UserSegmentPusher('./Ninja-Software-Engineer-Assignment/userinfo.db')
    
    user_info = pusher.generate_user_info()
    
    pusher.store_user_info(user_info)
    
    print(user_info)

