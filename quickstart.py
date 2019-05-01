from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload
from googleapiclient import http
from googleapiclient import discovery
filestr = ''
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']

def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    # Call the Drive v3 API
    qna = str(ai())
    f= open("files/qna.txt","w+")
    f.write(qna)
    file_metadata = {'name': 'qna.txt'}
    media = MediaFileUpload('files/qna.txt',mimetype='text/plain')
    file = service.files().create(body=file_metadata,media_body=media,fields='id').execute()
    print('File ID: %s' % file.get('id'))
    results = service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))


import pandas as pd
name_list = {}
que_dic = {}
tempquedic = {"what is your name?": "He calls me \'LOC ai\' (Local Artificial intelligence Imitant)",
              "who is he":" He is an imaginator, I am not authorised to reveal his name",
              "what are you?":"I am a local artifical intelligence imitant, I imitate my seniors. I am learning",
              "what can you do for me?":"Talk, I can just talk! now"}

#The artificial intelligence imitator
#The software will ask for the commands, with a quirky answer

#input and decode function
def ai():
    print("Hey! Mind telling me your name?")
    name = input()
    if name in name_list.keys():
        print("Welcome back {}".format(name))
    else:
        name_list[name] = {}
        print("Hey {} We've got you covered.".format(name))
        print("What do you want me to remember?")
        #print("I'm new, but can answer a few, can't solve puzzles, but can make you one! ;)")
    '''if name in name_list.keys():
        print("What do you want me to tell you?")
        quet1 = input()
        if (quet1 in name_list[name].keys()) or (quet1 in tempquedic.keys()):
            try:
                print(name_list[name][quet1])
            except KeyError:
                print(tempquedic[quet1])
            except KeyError:
                print("Data not available")
        else:
            print("You never asked told me that, the answer please")
            name_list[name][quet1] = input()
            print("We are done here for now, please login again to see your answer")
'''
    #else:
    print("Your first reminder please")
    quet1 = input()
        #if quet1 in tempquedic.keys():
            #print(tempquedic[quet1])
            #print("This is a core question,please try a different one")
        #else:
    print("Your answer please")
    ans1 = input()
    name_list[name][quet1] = ans1
    print(name_list)
    print("Already attracted? Wanna play more?")
    ansnow = input()
    if (ansnow == "Yes") or (ansnow == "yes"):
        ai()
    else:
        print(name_list)
        #filestr = name_list[0].keys[0] 
        return name_list

            
        #check if the name already exists in the list
        #ifyes ask for password
        #then carry the question answer sequence
        #if not exists, ask for a user sign up
        #add the name to the list
        #and add the
        #add a password to secure its passcode

if __name__ == '__main__':
    main()
