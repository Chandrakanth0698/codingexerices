import zipfile
import pathlib


def zip_archive(filepaths, des):
    des_path = pathlib.Path(des, "compressed.zip")
    with zipfile.ZipFile(des_path, 'w') as myzip:
        for filepath in filepaths:
            myzip.write(filepath)


if __name__ == "__main":
    zip_archive(filepaths=['ce1.py'], des='zip')
