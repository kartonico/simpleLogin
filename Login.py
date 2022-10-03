import pysimplegui as sg

#Creating a layout:
layout = [
    [sg.Text('User:'), sg.Input('', key='name')],
    [sg.Text('Password:'), sg.input('', key='Pass')],
    [sg.Button('Log in', key='logIn'), sg.Button('Register', key='new')],
    [sg.Text('', key='msg')],
]

#Creating a window:
window = sg.Window('Login', layout)

#Opening the window:
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: #To close the window.
        break

    if values('name') == Name and event == logIn:
        break
        elife values('name') != Name and event == logIn:
            sg.Popup('Your username or password is wrong.')
            
    #test user:
    Name = 'luiz'
    Pass = '123'

window.close()