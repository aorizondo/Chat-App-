from kivy.config import Config
Config.set('graphics', 'width', '350')
from kivy.app import App
from kivy.lang import Builder
from kivymd.theming import ThemeManager
from kivymd.dialog import MDInputDialog, MDDialog
from kivy.uix.widget import Widget
from kivy.uix.button import Button, ButtonBehavior
from kivy.uix.label import Label
from myfirebase import Firebase
from kivy.uix.rst import RstDocument
from kivy.core.audio import SoundLoader
import requests
import json
import re
import time
from kivy.uix.scrollview import ScrollView
from kivymd.list import ILeftBody
from kivy.uix.image import Image
from kivymd.toast import toast
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition, CardTransition
from kivy.clock import Clock
from kivymd.list import ThreeLineListItem, TwoLineAvatarIconListItem, MDList

class Background(Widget):
    pass

class Lecturer(App):
    theme_cls = ThemeManager()
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        self.firebase = Firebase()
        self.sound = SoundLoader.load('pip.mp3')
        return Builder.load_file('main.kv')

    def my_callback(self, text_of_selection, pop_widget):
    	pass

    def on_start(self):
        try:
            with open("refresh_token.txt", "r") as f:
                refresh_token = f.read()
                # Use refresh_token to get a new idToken
            id_token, local_id = self.firebase.exchange_refresh_token(refresh_token)  
            
            self.root.ids["manager"].transition = NoTransition()
            self.ChangeScreen("home")
            self.root.ids["manager"].transition = CardTransition()
            self.firebase_to_file()
            # self.set_message_list()
            self.get_message()
            self.render()
            # Clock.schedule_interval(self.firebase_to_file,10)
            # Clock.schedule_interval(self.get_message,10)

        except Exception as e:
            print(e)    

    def ChangeScreen(self, name):
        screen = self.root.ids['manager']
        screen.current = name
    
    def refresh(self):
        self.ChangeScreen('home')
        self.firebase_to_file()
        self.make_sound()
        # self.remove_list()
        # self.set_message_list()
        self.get_message()
        toast('refreshed')
        
    def lock_menu_button(self):
        screen = self.root.ids.manager
        na = self.root.ids.na
        if screen.current != 'login':
            na.toggle_nav_drawer()
                    
    def make_sound(self):
        if self.sound:
            self.sound.play()
    
    def check_screen(self):
        if self.root.ids.manager.current != 'login':
            self.root.ids.na.toggle_nav_drawer()

    def show_dialog(self):
    	my_dialog = MDDialog(title='About the App', 
    		text='This app is for level advisers only, it enables communication between student and their respective level coodinators',
    		size_hint=[.8,.4], auto_dismiss=False, events_callback=self.my_callback, text_button_ok='I understand')
    	my_dialog.open()

    def show_dialoghelp(self):
        my_dialog = MDDialog(title='What is this ?', 
    		text='To send a message, you have to provide the receivers username, you can also send to multiple users by seperating their usernames with a comma (,)',
    		size_hint=[.8,.4], auto_dismiss=False, events_callback=self.my_callback, text_button_ok='Ok perfect !')
        my_dialog.open()
    def active(self, level):
        with open('level.txt', 'w') as f:
            f.write(str(level))
        print(level,' Adviser')
        
    def set_message_list(self):
        mdlist = MDList(id='mylist')
        scroll = self.root.ids.scroller
        scroll.add_widget(mdlist)
        
    def remove_list(self):
        card = self.root.ids.mdcarde 
        card.clear_widgets()
    
    # def get_message(self, *largs):
    #     mdlist = MDList(id='mdlist')
    #     scroll = ScrollView()
    #     scroll.add_widget(mdlist)
    #     card = self.root.ids.mdcarde 
    #     card.add_widget(scroll)
    #     # let clear the widget  before adding the list
    #     with open('messages.txt', 'r') as f:
    #         junk = f.readlines()
    #     for i in junk:
    #         ni = re.split('~',i)
    #         messe  = ThreeLineListItem(text = ni[0], secondary_text = ni[2])
    #         mdlist.add_widget(messe)
    #         # print("++++++++++++++++++++")
    #         # print(ni)
    #         # print("++++++++++++++++++++")
            
    #     # scroll.remove_widget(mdlist)
    def get_message(self, *largs):
        box_for_text = self.root.ids.box
        with open('messages.txt', 'r') as f:
            faa = f.readlines()
            
        with open('messages.txt', 'r') as f:
            fa = f.read()
            
        if faa == []:
            fa = fa.replace('~', '\n')
            message = RstDocument(text = fa, size_hint= (None,None), size=(250, 100), base_font_size= 20, background_color=(.9,.9,.9,1))
            box_for_text.add_widget(message)
        else:
            for i in faa:
                i = i.replace('~', '\n')
                if i != '\n':
                    message = RstDocument(text = i, size_hint= (None,None), size=(250, 100), base_font_size= 20, background_color=(.93,.93,.93,1))
                    box_for_text.add_widget(message)
        # for i in range(10):
            # print(faa)
        
    def send_message(self):
        try:
            text_field = self.root.ids.send_to
            users_to_send = self.root.ids.users
            students = ''
            if text_field.text and users_to_send.text != '':
                with open('level.txt', 'r') as f:
                    my_username = f.read() + 'L Adviser'

                text_field.text = text_field.text.replace(',' , '.')
                text_for_firebase = my_username + '~__________________~'+ text_field.text
                # with open('messages.txt','a') as f:
                    # f.write(text_for_firebase + str('\n'))
                # self.remove_list()
                # self.get_message()
                un_split_users = users_to_send.text
                list_of_student = re.split(',', un_split_users)
                with open('level.txt', 'r') as f:
                    mylevel =f.read()
                for i in list_of_student:
                    requests.post("https://chatapp-80ce4.firebaseio.com/"+ mylevel+ '_level_students/' +  i + "/messages.json", data=json.dumps(text_for_firebase))
                    requests.post("https://chatapp-80ce4.firebaseio.com/"+ mylevel+'.json', data=json.dumps(text_for_firebase))
                self.firebase_to_file()
                self.get_message()   
                toast('sent')
                
                text_field.text = ''
                users_to_send.text = ''
            else:
                print('')
                toast('Empty Field')
        except Exception as e:
            # toast(str(e))
            pass
            
    def firebase_to_file(self, *largs):
        with open('messages.txt', 'w') as f:
            f.write('')
        with open('level.txt', 'r') as f:
            level1 = f.read()
        data = requests.get('https://chatapp-80ce4.firebaseio.com/'+ level1 + '.json')
        un_split_data = data.content.decode()
       
        list_of_data = []
        arr = []
        li = []
        split_data = re.split(',', un_split_data)
        
        
        for i in split_data:
            without_id = i[24:]
            list_of_data.append(without_id)

        for i in list_of_data:
            i = i.replace('"', '')
            i = i.replace('}', '')
            arr.append(i)
            
        
# this is the reason why i am having white spaces for message fields
        for i in arr:
            # if i != '':
            i  = i.replace(',',' ')
            li.append(i)
            
            
        for i in li:
            with open('messages.txt', 'a') as f:
                f.write(i + '\n')
                    
    def studentslist(self):
        # self.render()
        
        self.ChangeScreen('students')
    # Rendering the student lists, i am so excited to do this, though it's not easy
    def render(self):
        try:
            with open('level.txt', 'r') as f:
                level = f.read()
            lists = self.root.ids.students_list
            data = requests.get('https://chatapp-80ce4.firebaseio.com/'+level+'_level_students.json')
            row_data = json.loads(data.content.decode())
            arr = []
            
            for p_info,student in row_data.items():
                arr.append(student)
            print(arr)
            for p in arr:
                li = ThreeLineListItem(text=p['Username'],
                                secondary_text = str(p['FullName']) + '                       ' + str(p['Phone'] ))
                lists.add_widget(li)
        except Exception as e:
            toast(str(e))
            print(e)
    
    def message_delay(self):
        time.sleep(1)
        self.get_message()
    def log_out(self):
        with open('refresh_token.txt', 'w') as f:
            f.write('')
        
        toast('You Just Log Out')
        self.make_sound()
        self.ChangeScreen('login')
               
Lecturer().run()
