import shutil
import os

shutil.copy("./practice6/sample.txt", "./practice6/sample_backup.txt")

if os.path.exists("./practice6/sample.txt"):
    os.remove("./practice6/sample.txt")