import PySimpleGUI as sg

#Creating a layout:
layout = [
    [sg.Text('User:')],
    [sg.Input('', key='name')],
    [sg.Text('Password:')],
    [sg.Input('', key='pass')],
    [sg.Button('Login', key='logIn'), sg.Button('Register', key='new')],
]

#Creating a window:
window = sg.Window('Login', layout)

#test user:
Name = 'luiz'
Pass = '123'

#Opening the window:
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: #To close the window.
        break
    
    if values['name'] == Name and values['pass'] == Pass and event == 'logIn': #All is ok.
        sg.Popup('Teste feito com sucesso.')
        break
    if values['name'] != Name or values['pass'] != Pass and event == 'logIn': #Wrong name/password.
        sg.Popup('Your username or password is wrong.')
    



window.close()

#Register screen:
layout2 = [
    [sg.Text('Your name:')],
    [sg.Input('', key='newname')],
    [sg.Text('Your password:')],
    [sg.Input('', key='newpass')],
    [sg.Text('Confirm your password:')],
    [sg.Input('', key='newpass2')],
    [sg.Button('Finish', key='next')]
]