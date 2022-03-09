# import menpo
# import menpowidgets
# import menpo.io as mio
import preproc
import csv

# path_to_lfpw = Path('/path/to/lfpw/trainset/')

sub_num, photo_num, seq = preproc.create_sub_id()

# shape model
training_shapes = []

# with open('all_points.csv', 'w', encoding='UTF8', newline='') as f:
#     writer = csv.writer(f)
#     print(len(sub_num))
#
#     for i in range(0, 776):
#         filename = preproc.get_filename(sub_num[i], photo_num[i], seq[i])
#         x, y = preproc.prepare_points(filename)
#         for (xp, yp) in zip(x, y):
#             writer.writerow(f"{xp} {yp}")

