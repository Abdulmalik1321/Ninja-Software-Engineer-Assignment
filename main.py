# from snapchat_ads.client import SnapchatAdsAPI
import random

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
    

if __name__ == "__main__":
    pusher = UserSegmentPusher('users.db')
    
    user_info = pusher.generate_user_info()
    
    print(user_info)

