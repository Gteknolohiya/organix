import PySimpleGUI as sg
import os

def get_folder_path():
    """
    Prompts the user to select a folder directory through a PySimpleGUI window.

    This function uses PySimpleGUI to display a window with a 'Browse' button,
    which opens a directory chooser dialog. The user can select a folder and 
    confirm their choice by clicking 'OK'. The chosen folder path is then returned.
    
    If the user clicks 'Cancel' or closes the window, the function ends and no 
    folder path is returned.

    Returns:
        folder_path (str): The absolute path of the chosen directory. None if the user cancels the operation or chooses an invalid directory.

    Raises:
        sg.PopupError: If the chosen directory does not exist.
    """    
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
            # return None
        elif event == 'OK':
            folder_path = values['-FOLDER-']

            if not os.path.isdir(folder_path):
                sg.PopupError(f'The directory "{folder_path}" does not exist. Please select a valid directory.', font=('Helvetica', 12), text_color='white')
            else:
                window.close()
                return r"{}".format(folder_path)
        else:
            print('Operation canceled.')
            os.system('cls' if os.name == 'nt' else 'clear')
            