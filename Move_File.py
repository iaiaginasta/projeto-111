import os
import shutil

from_dir = "C:/Users/Eleven/OneDrive/Documentos/Byju's/python/projeto 111"
to_dir = "C:/Users/Eleven/OneDrive/Área de Trabalho"

list_of_files = os.listdir(from_dir)

#print (list_of_files)

for file_name in list_of_files:
    raiz, ext = os.path.splitext(file_name)
