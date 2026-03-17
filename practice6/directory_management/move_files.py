from pathlib import Path
import shutil

Path("./practice6/data.txt").touch()
Path("./practice6/archive").mkdir(exist_ok=True)


shutil.move("./practice6/data.txt", "./practice6/archive/data_v1.txt")