import csv
import sys


export_data = set()


def open_file(arg_pos, mode='r'):
    return open(sys.argv[arg_pos], mode, encoding='UTF8', newline='')


for i in range(1, len(sys.argv)-1):
    with open_file(mode='r', arg_pos=i) as fr:
        rows = csv.reader(fr)
        header = next(rows)
        subjectIp, subjectPort, subjectProtocol, peerIp, peerPort, perrProtocol = header.index('searchSubject.ipAddress'), header.index('searchSubject.portProtocol.port'), header.index(
            'searchSubject.portProtocol.protocol'), header.index('peer.ipAddress'), header.index('peer.portProtocol.port'), header.index('peer.portProtocol.protocol')
        for rw in rows:
            export_data.add(
                (rw[subjectIp], f'{rw[subjectPort]}/{rw[subjectProtocol]}', rw[peerIp], f'{rw[peerPort]}/{rw[perrProtocol]}'))

with open_file(mode='w', arg_pos=-1) as fw:
    writer = csv.writer(fw)
    writer.writerow( ('Subject IP Address', 'Subject Port/Protocol', 'Peer IP Address', 'Peer Port/Protocol') )
    for rw in export_data:
        writer.writerow(rw)