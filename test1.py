#!/usr/bin/env python3
import serial
import time

# シリアルポート設定
port = "COM8"  # 環境に応じて変更（例: /dev/ttyUSB0）
baudrate = 2400
bytesize = serial.EIGHTBITS  # データ長: 8ビット
parity = serial.PARITY_NONE  # パリティ: なし
stopbits = serial.STOPBITS_ONE  # ストップビット: 1ビット
 
 
try:
    # シリアルポートを開く
    ser = serial.Serial(
        port=port,
        baudrate=baudrate,
        bytesize=bytesize,
        parity=parity,
        stopbits=stopbits,
        timeout=1
    )
    print(f"{port} を開きました (ボーレート: {baudrate}, データ長: {bytesize}, パリティ: {parity}, ストップビット: {stopbits})")

    # ASCIIコードをバイト配列で送信（A, B, CR）
    message = bytes([0x41, 0x0D])  # 'A', キャリッジリターン
    ser.write(message)
    print(f"送信: {message.decode('ascii', errors='replace')}")

    # 必要に応じて少し待機
    time.sleep(5)

    # 受信データの確認（必要に応じて）
    if ser.in_waiting > 0:
        response = ser.read(ser.in_waiting).decode('ascii', errors='replace')
        print(f"受信: {response}")

except serial.SerialException as e:
    print(f"エラー: {e}")
finally:
    # シリアルポートを閉じる
    if 'ser' in locals() and ser.is_open:
        ser.close()
        print("シリアルポートを閉じました")