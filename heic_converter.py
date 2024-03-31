"""
heicをjpgにコンバートするpythonスクリプト
"""

from PIL import Image
import pillow_heif
from pathlib import Path


target_dir = Path(r"フォルダのパスを入力")  # ここにディレクトリのパスを入力してください
convert_type = "jpg"  # 対応：JPG, PNG, BMP, TIFF, GIF, PPM, PGM, PBM, PNM
print(f"変換を開始しています：{target_dir}")


# 動画の変換処理
def heic_convert(filepath, convert_type):
    heic_file = pillow_heif.read_heif(filepath)
    image = Image.frombytes(
        heic_file.mode,
        heic_file.size,
        heic_file.data,
        "raw",
        heic_file.mode,
        heic_file.stride,
    )
    # image.saveのリファレンス通りの入力形式に合わせる
    save_format = "JPEG" if convert_type == "jpg" else convert_type.upper()
    image.save(f"{target_dir}\\{file_name}.{convert_type}", save_format)


# ディレクトリ内のheicファイルを捜索
for filepath in target_dir.iterdir():  # is_file()で直下のディレクトリのみになる
    if filepath.is_file() and filepath.suffix == ".heic":
        print(filepath)
        file_name = filepath.stem
        heic_convert(filepath, convert_type)
        break
    else:
        print(f"heicファイルがありません")
input(f"終了します：{target_dir}")
