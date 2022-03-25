import csv
import sys


class MyRow:

    equality_condition_typ1_idxs = [1, 3, 4, 5]
    equality_condition_typ2_idxs = [0, 2, 3, 4]
    equality_condition_idxs = {
        1: equality_condition_typ1_idxs, 2: equality_condition_typ2_idxs}

    def __init__(self, row_data: tuple, type_of_row) -> None:
        self.row_data = row_data
        self.row_type = type_of_row

    def __eq__(self, __o: object) -> bool:
        if len(MyRow.equality_condition_typ1_idxs) != len(MyRow.equality_condition_typ2_idxs):
            raise ValueError("Cannot compare. Diff # of cols.")

        for idx in range(len(MyRow.equality_condition_typ2_idxs)):
            my_data, ot_data = self.row_data, __o.row_data
            my_idxs, ot_idxs = MyRow.equality_condition_idxs[self.row_type], MyRow.equality_condition_idxs[__o.row_type]
            if my_data[my_idxs[idx]] != ot_data[ot_idxs[idx]]:
                return False
        return True

    def __hash__(self):
        return 0



export_data = set()


def open_file(arg_pos, mode='r'):
    return open(sys.argv[arg_pos], mode, encoding='UTF8', newline='')


for i in range(1, len(sys.argv)-1):
    with open_file(mode='r', arg_pos=i) as fr:
        rows = csv.reader(fr)
        header = next(rows)
        for rw in rows:
            if len(rw) == 6:
                export_data.add(MyRow((rw[0], rw[1], rw[2], rw[3], rw[4], rw[5].upper()), type_of_row=1))
            else:
                rw3_upper = rw[3].upper()
                rw3, rw4 = rw3_upper.split('/')[0], rw3_upper.split('/')[1]
                export_data.add(MyRow((rw[0], rw[1], rw[2], rw3, rw4), type_of_row=2))
ex1 = None
with open_file(mode='w', arg_pos=-1) as fw:
    writer = csv.writer(fw)
    writer.writerow(('source_asset_name', 'source_ip', 'destination_asset_name', 'destination_ip', 'destination_port', 'ip_protocol'))
    for my_row in export_data:
        if my_row.row_type == 1:
            ex1 = my_row
            writer.writerow(my_row.row_data)
        else:
            new_data = [''] * len(ex1.row_data)
            for i in range(len(MyRow.equality_condition_typ1_idxs)):
                old_idx = MyRow.equality_condition_typ2_idxs[i]
                new_idx = MyRow.equality_condition_typ1_idxs[i]
                new_data[new_idx] = my_row.row_data[old_idx]
            writer.writerow(new_data)