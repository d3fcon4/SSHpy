from packages.connetion import Connection
import PySimpleGUI as Sg

Sg.theme('DarkAmber')  # Add a touch of color
# All the stuff inside your window.
layout = [
    [
        Sg.Text('Host:'), Sg.Input(
            key='host',
            size=(15, 1),
            background_color='#2D2C2C',
            text_color='#FFFFFF'
        ),
        Sg.Text('Username:'), Sg.Input(
                key='user',
                size=(20, 1),
                background_color='#2D2C2C',
                text_color='#FFFFFF'
        ),
        Sg.Text('Password:'), Sg.Input(
                key='pass_',
                size=(15, 1),
                password_char='*',
                background_color='#2D2C2C',
                text_color='#FFFFFF'
        ),
        Sg.Text('Port:'), Sg.Spin(
                [i for i in range(1, 65535)],
                initial_value=22,
                size=(6, 1),
                key='port',
                background_color='#2D2C2C',
                text_color='#FFFFFF')
    ],
    [
        Sg.Text('Output Command:')
    ],
    [
        Sg.Output(key='output', size=(95, 30), background_color='#2D2C2C', text_color='#1F7A16')
    ],
    [Sg.Text('Enter Command: '), Sg.InputText(
        key='cmd',
        background_color='#2D2C2C',
        text_color='#FFFFFF',
        size=(81, 1)
    )],
    [
        Sg.Button(button_text='Run Command', button_color=('black', 'green'), size=(13, 1), key='run'),
        Sg.Button(button_text='Exit', button_color=('black', 'red'), size=(13, 1), key='exit'),
        Sg.Button(button_text='Clear Fields', button_color=('black', 'orange'), size=(13, 1), key='clear_fields'),
        Sg.Button(button_text='Clear Output', button_color=('black', 'orange'), size=(13, 1), key='clear_output')

    ]
]

# Create the Window
window = Sg.Window('SSHpy', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == Sg.WIN_CLOSED or event == 'exit':  # if user closes window or clicks cancel
        break
    if event == 'run':
        cli = Connection(
            hostname=values['host'],
            username=values['user'],
            password=values['pass_'],
            port=values['port']
        )

        window['output']('')

        cli.connect()

        cli.command_line(values['cmd'])

    if event == 'clear_fields':
        for key in values:
            if key != 'port':
                window[key]('')
    if event == 'clear_output':
        window['output']('')

window.close()
