# HEIC to JPEG Converter
このPythonスクリプトは、指定したフォルダ内のHEIC形式の画像ファイルをJPEG形式に変換します。
変換された画像は同じフォルダに保存されます。

## 必要なライブラリ
pillow_heif
pathlib

## 使い方
- Pythonをインストール
- 必要なライブラリをインストール
  - ```pip install pillow-heif```
- スクリプトのtarget_dir変数に変換したいHEICファイルが含まれるフォルダのパスを指定
- スクリプトを実行

# 注意事項
- このスクリプトはHEIC形式の画像ファイルをJPEG形式に変換しますが、変換後の画像品質やメタデータの保持については保証されませ以外
- jpg,png以外の動作は未確認です
