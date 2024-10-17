import TkEasyGUI as eg

# レイアウト定義
layout = [
    [
        eg.Text('', expand_y=True) #抽選した数字を縦の中央に表示
    ],

    [
        eg.Text('', expand_x=True), #抽選した数字を横の中央に表示
        eg.Column([[eg.Text('BINGO', font=('arial', 400))]], expand_y=True),
    ],

    # 履歴
    [
        eg.Frame('履歴', [[eg.Text('', key='log', font=('arial', 50))]],)
    ],

    #　ボタン各種
    [
        eg.Button('スタート', key='start', size=(10, 3), disabled=False),
        eg.Button('ストップ', key='stop', size=(10, 3), disabled=True),
        eg.Button('リセット', key='reset', pad=(50,0)),
        eg.Text('', expand_x=True), #終了ボタンを一番右に配置
        eg.Button('終了')
    ]
]

# ウィンドウの設定
window = eg.Window('bingo ver.1', layout, center_window=True, size=(500, 500), resizable=True)

while True:
    # イベントの読み込み
    event, values = window.read()

    # 「スタート」ボタンクリックで
    if event == 'start':

        # ストップボタン有効化
        window['stop'].update(disabled=False)
        # スタートボタン無効化
        window['start'].update(disabled=True)

    # 「ストップ」ボタンクリックで
    if event == 'stop':

        # ストップボタン無効化
        window['start'].update(disabled=False)
        # スタートボタン有効化
        window['stop'].update(disabled=True)



    # 終了ボタンクリックで終了
    if event == '終了':
        break

    # ウィンドウの×ボタンクリックで終了
    if event == eg.WIN_CLOSED:
        break


# ウィンドウ終了処理
window.close()