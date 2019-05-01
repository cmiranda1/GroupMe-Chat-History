from groupy.client import Client
import pandas as pd

class GroupMe(object):
    def __init__(self,token):
        self.token = token
        self.client = Client.from_token(self.token)
        self.group_names= []
    def getChats(self):
        for group in self.client.groups.list_all():
            self.group_names.append(group.name.encode('unicode-escape',errors='replace').decode())
        return self.group_names

    def getDataFrame(self,chat_name,grouplist):
        group = self.client.groups.list()
        chat = group[grouplist.index(chat_name)]
        all = list(chat.messages.list().autopage())
        self.chathistory = pd.DataFrame(columns={'Name','User ID','Attachments','Text','Datetime','Like List'})
        for messages in all:
            if messages.text is not None:

                self.chathistory = self.chathistory.append(pd.DataFrame(
                    {'Name': messages.name, 'User ID': messages.user_id, 'Attachments': str(messages.attachments),
                     'Text': messages.text.encode('utf-8', errors='replace').decode(),
                     'Datetime': str(messages.created_at), 'Like List': ",".join(messages.favorited_by)}, index=[0]),
                                                 sort=False)

            else:

                self.chathistory = self.chathistory.append(pd.DataFrame(
                    {'Name': messages.name, 'User ID': messages.user_id, 'Attachments': str(messages.attachments),
                     'Text': messages.text, 'Datetime': str(messages.created_at),
                     'Like List': ",".join(messages.favorited_by)}, index=[0]), sort=False)

        self.chathistory['Datetime'] = self.chathistory['Datetime'].str.split('+').str[0]
        return self.chathistory

