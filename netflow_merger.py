import csv
import sys


export_data = set()


def open_file(arg_pos, mode='r'):
    return open(sys.argv[arg_pos], mode, encoding='UTF8', newline='')


for i in range(1, len(sys.argv)-1):
    with open_file(mode='r', arg_pos=i) as fr:
        rows = csv.reader(fr)
        header = next(rows)
        for rw in rows:
            export_data.add((rw[0], rw[1], rw[2], rw[3]))

with open_file(mode='w', arg_pos=-1) as fw:
    writer = csv.writer(fw)
    writer.writerow( ('Subject IP Address', 'Subject Port/Protocol', 'Peer IP Address', 'Peer Port/Protocol') )
    for rw in export_data:
        writer.writerow(rw)