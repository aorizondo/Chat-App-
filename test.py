# import re
# from kivy.uix.scrollview import ScrollView
# text = 'Username~______~how are you'
# print(dir(ScrollView))
# li = re.split('~',text)
# print(li)

# with open('messages.txt', 'r') as f:
#     arr = f.readlines()
# for i in arr:
#     li = re.split('~',i)
#     print(li)
#     for n in li:
#         pass
        # print(n)
#     print(li)

# from kivy.app import App
# from kivymd.theming import ThemeManager
# from kivymd.label import MDLabel
# from kivymd.cards import MDCard
# from kivy.lang import Builder
# from kivymd.list import ILeftBody
# from kivy.uix.image import Image
# from kivy.uix.boxlayout import BoxLayout
# from kivymd.list import OneLineListItem,MDList, TwoLineListItem, ThreeLineListItem, TwoLineAvatarIconListItem

# class AvatarSampleWidget(ILeftBody, Image):
#     pass

# class LISTE(TwoLineAvatarIconListItem):
#         text = 'Hamza'
#         secondary_text = 'Hamz Ahmad sha'

# kv = '''
# #:import MDCard kivymd.cards
# #:import MDList kivymd.list
# #:import TwoLineAvatarIconListItem kivymd.list.TwoLineAvatarIconListItem
# #:import TwoLineListItem kivymd.list.TwoLineListItem

# BoxLayout:
#     orientation: 'vertical'
#     canvas: 
#         Color:
#             rgba: (.1,.1,.1,1)
#         Rectangle:
#             pos: self.pos
#             size: self.size 
#     MDCard:    
        
#         id: card
#         orientation: 'vertical'
#         elevation: 5
#         pos_hint: {'top': .95, 'right':.95}
#         size_hint: .9,.6
        
# '''
# class Test(App):
#     theme_cls = ThemeManager()
#     def build(self):
#         return Builder.load_string(kv)
#     def render(self):
#         card = self.root.ids.card
#         mdlist = MDList(id='list', padding = 20, spacing = 20, size_hint_y = 0.6)
#         item  = TwoLineListItem(text='Saulawa', secondary_text='Dynamic list rendering!!!')
#         mdlist.add_widget(item)
#         card.add_widget(mdlist)
#     def on_start(self):
#         self.render()
#         self.removeit()
#     def removeit(self):
#         self.render()
#         print(self.root.ids.list)
#         # li = self.root.ids.list
        # card = self.root.ids.card
        # card.clear_widgets()
        # li.remove_widget(TwoLineListItem())
        # print("++++++++++++++++++")
        # print(dir(TwoLineListItem))
        # print("++++++++++++++++++")
        
    
# Test().run()
# # people = {1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
# #           2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}
# # arr = []
# # for p_id, p_info in people.items():
# #     # print("\nPerson ID:", p_id)
# #     for key in p_info:
# #         print(key + ':', p_info[key])
# #         arr.append(p_info[key])
# #     # arr.append(p_info['Sex'])
        
# # print(arr)
# #         # print(key + ':', p_info[key])
# # li = ['hmz', 19, 'Male', 'hdz', 13, 'Female',1,11,1,1,1]
# # arr  = []
# # def final(li):
# #     x = 0
# #     y = 3
# #     step = 3
# #     # for item in li:
# #     #     x = 0
# #     #     y = 4
# #     #     step = 3
# #     #     arr.append(li[x:y])
# #     #     x += step
# #     #     y += step
# #     while y < len(li):
# #         arr.append(li[x:y])
# #         x += step
# #         y += step
        
        
        
# # print(arr)
# # final(li)
# # print(arr)        
        
        
li = []
a = ['aminu,ahmad', 'binta,sule', "kabiru,mani"]
for i in a:
    i = i.replace(',', ' ')
    li.append(i)
    print(i +"\n")
# print(li)
    
for i in li:
    # print(i)
    with open('aaaaaa.txt', 'a') as f:
        f.write(i)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        