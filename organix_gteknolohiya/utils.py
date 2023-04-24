import speech_recognition as sr
import PySimpleGUI as sg
import os

def ask_name():
    while True:
        text = recognize_speech("What would you like the files to be renamed as?").title()
        file_name = text
        text = recognize_speech(f"The filename you mentioned is {file_name}. Are you sure this is what you want to rename the files as? Yes/No: ")
        if text == "yes":
            return file_name
        elif text == "no":
            print("Going back to the last question...")
        else:
            print("Invalid option! Try again!")


def get_folder_path():
    sg.theme('DarkTeal9')
    sg.theme_background_color('#0f172a')

    layout = [
        [sg.Text('OrganiX', font=('Helvetica', 20), justification='center', text_color='white', background_color='#0f172a')],
        [sg.Text('Please select a folder directory to use:', font=('Helvetica', 12), text_color='white', background_color='#0f172a')],
        [sg.Input(key='-FOLDER-', enable_events=True, font=('Helvetica', 12)), sg.FolderBrowse(button_text='_Browse_', button_color=('black', '#e2e8f0'), font=('Helvetica', 12))],
        [sg.HorizontalSeparator()],
        [sg.Button('Cancel', font=('Helvetica', 12), button_color=('white', '#0f172a')), sg.Button('OK', font=('Helvetica', 12), button_color=('black', '#e2e8f0'))],
    ]

    window = sg.Window('Voice-automated File Management System', layout, resizable=True, size=(500, 200))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            window.close()
            return None
        elif event == 'OK':
            folder_path = values['-FOLDER-']

            if not os.path.isdir(folder_path):
                sg.PopupError(f'The directory "{folder_path}" does not exist. Please select a valid directory.', font=('Helvetica', 12), text_color='white')
            else:
                window.close()
                return r"{}".format(folder_path)

folder_path = get_folder_path()

if folder_path is not None:
    print(f'Selected folder path: {folder_path}')
else:
    print('Operation canceled.') 


def recognize_speech(message):
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print(message)
        print("Speak now...")

        while True:
            audio = r.listen(source)

            try:
                text = r.recognize_google(audio, language='en-US')
                print(f"You said: {text}")
                return text
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service: {e}")