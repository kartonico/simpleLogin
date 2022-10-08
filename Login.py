import PySimpleGUI as sg

#Creating a layout:
layout = [
    [sg.Text('User:'), sg.Input('', key='name')],
    [sg.Text('Password:'), sg.Input('', key='pass')],
    [sg.Button('Login', key='logIn'), sg.Button('Register', key='new')],
    [sg.Text('', key='msg')],
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

    if values['name'] == Name and values['pass'] == Pass and event == 'logIn':
        sg.Popup('Teste feito com sucesso.')
        break

    if values['name'] != Name or values['pass'] != Pass and event == 'logIn': #Name wrong
        sg.Popup('Your username or password is wrong.')
    

window.close()