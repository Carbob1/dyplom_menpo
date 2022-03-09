import csv
import glob
path = r"C:\Users\Anna\PycharmProjects\dyplom_1\ThermalFaceDatabase_full"
path_ljson = r"C:\Users\Anna\PycharmProjects\dyplom_1\ThermalFaceDatabase_full\*.ljson"



def prepare_points(filename):
    filename_ljson = rf"{path}\{filename}.ljson"
    f = open(filename_ljson, "r")

    f = f.read().split()  # dziele tekst na fragmenty
    points = f[394:666]  # points twarzy

    for i in range(0, 136, 2):  # usuwanie zbednych nawiasow
        points.pop(i)
        points.pop(i + 2)

    points_2 = []
    for i in points:
        i = i.replace(',', '')
        i = round(float(i))
        points_2.append(i)

    points = points_2

    y = points[0::2]
    x = points[1::2]

    return x, y


def get_filename(sub_num, photo_num, seq):
    return f"irface_sub{sub_num}_seq{seq}_frm{photo_num}.jpg_lfb"


def create_sub_id():
    size = len(glob.glob(path_ljson))//100
    sub_num = []
    photo_id = []
    seq = []
    with open('sub_num.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        for i in range(0, size):
            if glob.glob(path_ljson)[i][81:83] == '07' or glob.glob(path_ljson)[i][81:83] == '06':
                continue
            else:
                sub_num.append(glob.glob(path_ljson)[i][74:77])
                photo_id.append(glob.glob(path_ljson)[i][87:92])
                seq.append(glob.glob(path_ljson)[i][81:83])
                writer.writerow(glob.glob(path_ljson)[i][74:77])


    # return sub_num, photo_id, seq
