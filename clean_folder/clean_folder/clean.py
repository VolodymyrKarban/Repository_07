from pathlib import Path
import shutil
import os


FILE_TIPES = {
    "Images": [".jpg", ".png", ".jpeg", ".svg"],
    "Documents": [".doc", ".docx", ".pdf", ".xlsx", ".txt", ".pptx"],
    "Video": [".mp4", ".mov", ".mkv", ".avi"],
    "Archives": ["Unpack_Archives", ".zip", ".rar", ".gz", "tar"],
    "Programs": [".exe"],
    "Audio": [".mp3", ".ogg", ".wav", ".amr"],
    "4K_Video": [".4k"],
    "Unpack_Archives": [],
    "Unknown_extension": [],
}
TRANS = {1040: 'A', 1072: 'a', 1041: 'B', 1073: 'b', 1042: 'V', 1074: 'v', 1043: 'G', 1075: 'g', 1044: 'D', 1076: 'd',
  1045: 'E', 1077: 'e', 1025: 'E', 1105: 'e', 1046: 'J', 1078: 'j', 1047: 'Z', 1079: 'z', 1048: 'I', 1080: 'i',
    1049: 'J', 1081: 'j', 1050: 'K', 1082: 'k', 1051: 'L', 1083: 'l', 1052: 'M', 1084: 'm', 1053: 'N', 1085: 'n',
      1054: 'O', 1086: 'o', 1055: 'P', 1087: 'p', 1056: 'R', 1088: 'r', 1057: 'S', 1089: 's', 1058: 'T', 1090: 't',
        1059: 'U', 1091: 'u', 1060: 'F', 1092: 'f', 1061: 'H', 1093: 'h', 1062: 'TS', 1094: 'ts', 1063: 'CH', 1095: 'ch',
          1064: 'SH', 1096: 'sh', 1065: 'SCH', 1097: 'sch', 1066: '', 1098: '', 1067: 'Y', 1099: 'y', 1068: '', 1100: '',
            1069: 'E', 1101: 'e', 1070: 'YU', 1102: 'yu', 1071: 'YA', 1103: 'ya', 1028: 'JE', 1108: 'je', 1030: 'I', 1110: 'i',
              1031: 'JI', 1111: 'ji', 1168: 'G', 1169: 'g', 32: '_', 33: '_', 34: '_', 35: '_', 36: '_', 37: '_', 38: '_', 39: '_',
                40: '_', 41: '_', 42: '_', 43: '_', 44: '_', 45: '_', 46: '.', 47: '_', 58: '_', 59: '_', 60: '_', 61: '_', 62: '_', 
                63: '_', 64: '_', 91: '_', 92: '_', 93: '_', 94: '_', 123: '_', 124: '_', 125: '_', 126: '_', 127: '_'} 

def translate(name):
    return name.translate(TRANS)

def unpack(archive_path, path_to_unpack):
    shutil.unpack_archive(archive_path, path_to_unpack)

def move_file(in_path, to_path):
    with open(in_path, "rb") as fh:
        file_memory = fh.read()
    with open(to_path, "wb") as fh:
        fh.write(file_memory)

def made_categori(path, dict_file_tipes):
    for categori in dict_file_tipes:
        try:
            os.mkdir(os.path.join(path, categori))
        except:
            pass

def clear_empty_folders(path):
    for root, dir, files in os.walk(path):
        ok = False
        for categori in FILE_TIPES:
            if os.path.join(path, categori) == root:
                ok = True
        if ok == False:
            try:
                os.rmdir(root)
                clear_empty_folders(path)
            except:
                pass

def sorted(path: Path):
    made_categori(path,FILE_TIPES)#Сразу делаем порядок в папках создаем разделы
    #i = 0
    for root, dir, files in os.walk(path):
        for filename in files:
            file_path = Path(os.path.join(root, filename))
            category = "Unknown_extension"
            for file_tipe, extension in FILE_TIPES.items():
                if file_path.suffix in extension:
                    category = file_tipe
            #i = i + 1
            #print( "Путь:= ", root, " Имя файла:= ", filename," Название:= ",file_path.stem, " Раcширение:= ", file_path.suffix, " Категория:= ",category,)
            #print("Откуда пишем:>", file_path)
            #print("Что и куда пишем:>",Path(os.path.join(path, category, translate(filename)))," ", i, "-Й файл")
            filename_norm = translate(filename)
            if file_path != Path(os.path.join(path, category, filename_norm)):
                #print("remuve, Усли не совпали или если в папке категории не тот файл или не правильное имя то перезапись \n")
                move_file(file_path, Path(os.path.join(path, category, filename_norm)))
                if category == "Archives":
                    unpack(file_path, Path(os.path.join(path, FILE_TIPES[category][0], filename_norm )))
                    #print(file_path,"  >>> архив уже в папке Archives делаем ему unpack в папку FILE_TIPES[category][0] >> ",Path( os.path.join(path, FILE_TIPES[category][0], filename_norm)), )
                os.remove(file_path) #И удаляем перемещенный файл.
            clear_empty_folders(path)#Удаляем пустые папки в каждой поддиректории

path = Path("C:/Testfolder")
sorted(path)
