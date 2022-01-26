from kivymd.uix.screen import MDScreen
import json

from libs.components.circular_avatar_image import CircularAvatarImage
from libs.components.post_card import PostCard

class HomePage(MDScreen):
    profile_picture= 'assets/profile.jpg'

    def on_enter(self):
        self.list_stories()
        self.list_posts()
    
    def list_stories(self):
        with open('assets/data/stories.json') as f_obj:
            data = json.load(f_obj)
            for name in data:
                self.ids.stories.add_widget(CircularAvatarImage(
                    avatar = data[name]['avatar'],
                    name = name
                ))
    
    def list_posts(self):
        with open('assets/data/posts.json') as f_obj:
            data = json.load(f_obj)
            for username in data:
                self.ids.timeline.add_widget(PostCard(
                    username = username,
                    avatar = data[username]['avatar'],
                    profile_pic = self.profile_picture,
                    post = data[username]['post'],
                    caption = data[username]['caption'],
                    likes = data[username]['likes'],
                    comments = data[username]['comments'],
                    posted_ago = data[username]['posted_ago'],
            ))
