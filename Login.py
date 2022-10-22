import PySimpleGUI as sg

#Creating layouts:
login = [
    [sg.Text('User:')],
    [sg.Input('', key='name')],
    [sg.Text('Password:')],
    [sg.Input('', key='pass')],
    [sg.Button('Login', key='logIn'), sg.Button('Register', key='new')],
]
register = [
            [sg.Text('Name:')],
            [sg.Input('', key='newname')],
            [sg.Text('Password:')],
            [sg.Input('', key='newpass')],
            [sg.Text('Confirm your password:')],
            [sg.Input('', key='newpass2')],
            [sg.Button('Finish', key='next')]
]

#Creating a window:
window = sg.Window('Login', login)


#Opening the window:
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: #To close the window.
        break
    #user:
    Name = ''
    Pass = ''
    
    #opening the register:
    if event == 'new':
        #Register screen:
        

        window2 = sg.Window('Register', register)


        while True:
            event, values = window2.read()
            if event == sg.WIN_CLOSED:
                break
            
            #Username smal:
            if len(values['newname']) <= 4 and event == 'next':
                sg.Popup('Your name is small.')
            #Password small:
            if len(values['newpass']) <= 5 and event == 'next':
                sg.Popup('Your password is small.')
            
            #Senhas não iguais:
            if values['newpass'] != values['newpass2'] and event == 'next':
                sg.Popup('Senhas não iguais.')
            
            #Box empty:
            if len(values['newname']) == 0 and event == 'next':
                sg.Popup('Your name is empty.')
            if len(values['newpass']) == 0 and event == 'next':
                sg.Popup('Passowrd is empty.')


        window2.close()



    if values['name'] == Name and values['pass'] == Pass and event == 'logIn': #All is ok.
        sg.Popup('Teste feito com sucesso.')
        
    if values['name'] != Name or values['pass'] != Pass and event == 'logIn': #Wrong name/password.
        sg.Popup('Your username or password is wrong.')


window.close()
