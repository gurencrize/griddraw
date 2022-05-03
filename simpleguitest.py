import PySimpleGUI as sg
import components

image = sg.Image(filename="D:\github\griddraw\96778073_p0.png")
vertical = sg.Spin(values=[i for i in range(20)],key="vertical",size=(3,1))
horizontal = sg.Spin(values=[i for i in range(20)],key="horizontal",size=(3,1))
column = sg.Column([[image]],expand_x=True,expand_y=True,scrollable=True,size=(500,500))
layout = [  
            [sg.Text("縦"),vertical,
            sg.Text("横"),horizontal,
            sg.Button('表示更新'),sg.Button('画像読み込み'), sg.Button('白紙画像生成')],
            [column]
        ]
# Create the Window
window = sg.Window('GridDraw', layout,resizable=True)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    elif event == '画像読み込み':
        image.update(filename = components.fileopen(vertical.get(),horizontal.get()),visible=True)
    elif event == '表示更新':
        image.update(filename = components.imagefile.updateImage(vertical.get(),horizontal.get()),visible=True)
    elif event == '白紙画像生成':
        components.imagefile.createWhiteImage(vertical.get(),horizontal.get())

#GUIは良さそうなのでロジック移動しよう！
#画像の拡大/縮小がデフォで付いてないのは悩み

window.close()