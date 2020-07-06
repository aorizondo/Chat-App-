for i in faa:
                i = i.replace('~', '\n')
                if i != '\n':
                    message = RstDocument(text = i, size_hint= (None,None), size=(250, 100), base_font_size= 20, background_color=(.93,.93,.93,1))
                    box_for_text.add_widget(message)