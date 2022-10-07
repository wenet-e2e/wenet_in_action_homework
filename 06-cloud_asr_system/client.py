import wave
import websocket


def on_open(ws):
    ''' 完成客户端与服务端的通信
    提示：
        传输文本: ws.send(str)
        传输二进制: ws.send(bytes, websocket.ABNF.OPCODE_BINARY)
    '''
    pass


ws = websocket.WebSocketApp("ws://127.0.0.1:10086", on_message=lambda _, msg: print(msg))
ws.on_open = on_open
ws.run_forever()
