import TkEasyGUI as eg
import random

lst = list(range(1, 76))
loglst = list()


# レイアウト定義
layout = [
    [
        eg.Text('', expand_y=True) #抽選した数字を縦の中央に表示
    ],

    [
        eg.Text('', expand_x=True), #抽選した数字を横の中央に表示
        eg.Column([[eg.Text('BINGO', key='bingo', font=('arial', 400))]], expand_y=True),
    ],

    # 履歴
    [
        eg.Frame('履歴', [[eg.Text('', key='log', font=('arial', 10), expand_x=True, expand_y=True)]], expand_x=True)
    ],

    # ボタン各種
    [
        eg.Button('スタート', key='start', size=(10, 3), disabled=False),
        eg.Button('ストップ', key='stop', size=(10, 3), disabled=True),
        eg.Button('リセット', key='reset', pad=(50,0), disabled=False),
        eg.Text('', expand_x=True), #終了ボタンを一番右に配置
        eg.Button('終了')
    ]
]

# ウィンドウの設定
window = eg.Window('bingo ver.1', layout, center_window=True, size=(500, 500), resizable=True)


while True:
    event, values = window.read() # イベントの読み込み


    # 「スタート」ボタンクリックで
    if event == 'start':
        # ストップボタン有効化
        window['stop'].update(disabled=False)
        # スタートボタン無効化
        window['start'].update(disabled=True)
        # リセットボタン有効化
        window['reset'].update(disabled=True)

        # 終了ボタンクリックで終了
        if event == '終了' or event == eg.WIN_CLOSED:
                window.close()
                break


        while True:
            window.refresh()
            event, values = window.read(50)
            r = random.sample(lst, 1)
            window['bingo'].update(r)

            # 終了ボタンクリックで終了
            if event == '終了' or event == eg.WIN_CLOSED:
                window.close()
                break


            # 「ストップ」ボタンクリックで
            if event == 'stop':
                # ストップボタン無効化
                window['start'].update(disabled=False)
                # スタートボタン有効化
                window['stop'].update(disabled=True)
                # リセットボタン有効化
                window['reset'].update(disabled=False)

                if not r in loglst:
                    loglst.append(r)
                    window['log'].update(loglst)
                    break

                while r in loglst:
                    r = random.sample(lst, 1)
                    window['bingo'].update(r)
                    if not r in loglst:
                        loglst.append(r)
                        window['log'].update(loglst)
                        break

                if window['log'].update:
                    print(loglst)
                    break

    # 「リセット」ボタン
    elif event == 'reset':
        window['bingo'].update('BINGO')
        loglst.clear()
        window['log'].update(loglst)


    # 終了ボタンクリックで終了
    elif event == '終了' or event == eg.WIN_CLOSED:
        window.close()
        break