# 基於ffmpeg做的簡易轉檔器

import os
import re
import subprocess
import sys
from datetime import timedelta, datetime
from PySide2.QtGui import (
    Qt,
    QFont
)
from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QGridLayout,
    QFileDialog,
    QMessageBox,
    QLabel,
    QLineEdit,
    QPushButton,
    QProgressBar
)

app = QApplication(sys.argv)
root = QWidget()
# root.setFixedSize(0, 0)
grid = QGridLayout(root)
root.setLayout(grid)

dur_delta, now_delta = None, None


def getFilePath():
    path, _ = QFileDialog.getOpenFileName(root)
    inputpath.setText(path)
    # 預設把輸入檔名設成輸出檔名
    outputpath.setText(os.path.basename(inputpath.text()))


def transform_file():
    global dur_delta, now_delta

    if outputpath.text() == '' and inputpath.text() == '':
        QMessageBox.warning(root, 'Error', '缺失輸入檔案與輸出檔名')
        return
    elif outputpath.text() == '':
        QMessageBox.warning(root, 'Error', '缺失輸出檔名')
        return
    elif inputpath.text() == '':
        QMessageBox.warning(root, 'Error', '缺失輸入檔案')
        return

    os.chdir(os.path.dirname(inputpath.text()))

    args = [
        'ffmpeg',
        '-y',  # overwrite if file exist
        '-i',
        os.path.basename(inputpath.text()),
        '-b' if bitrate.text() != '' else '',
        f'{bitrate.text()}' if bitrate.text() != '' else '',
        '-r' if frame.text() != '' else '',
        f'{frame.text()}' if frame.text() != '' else '',
        '-s' if resolution.text() != '' else '',
        f'{resolution.text()}' if resolution.text() != '' else '',
        outputpath.text(),
    ]

    process = subprocess.Popen(
        [*filter(lambda x: x != '', args)],
        encoding='utf-8',
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True
    )

    # reference -> https://www.geeksforgeeks.org/python-re-search-vs-re-match/
    for line in process.stdout:
        DurationMatches = re.search(
            r'Duration: (\d+:\d+:\d+.\d+)',
            str(line).strip()
        )
        if DurationMatches:
            duration = datetime.strptime(
                DurationMatches.group().split(': ')[1], "%H:%M:%S.%f"
            )
            dur_delta = timedelta(
                hours=duration.hour, minutes=duration.minute, seconds=duration.second
            )
            bar.setValue(0)

        timeMatches = re.search(
            r'time=(\d+:\d+:\d+.\d+)',
            str(line).strip()
        )
        if timeMatches:
            t2 = datetime.strptime(
                timeMatches.group().split('=')[1], "%H:%M:%S.%f"
            )
            now_delta = timedelta(
                hours=t2.hour, minutes=t2.minute, seconds=t2.second
            )
            bar.setValue(
                int((now_delta.total_seconds() / dur_delta.total_seconds()) * 100)
            )
    else:
        bar.setValue(100)


Linput = QLabel('input', root)
Linput.setAlignment(Qt.AlignLeft)
Linput.setFont(QFont('Arial', 10))
grid.addWidget(Linput, 0, 0)

inputpath = QLineEdit()
inputpath.setFont(QFont('Arial', 10))
grid.addWidget(inputpath, 0, 1)

getfile = QPushButton('pick video')
getfile.setFont(QFont('Arial', 10))
getfile.clicked.connect(getFilePath)
grid.addWidget(getfile, 0, 2)

Loutput = QLabel('output', root)
Loutput.setAlignment(Qt.AlignLeft)
Loutput.setFont(QFont('Arial', 10))
grid.addWidget(Loutput, 1, 0)

outputpath = QLineEdit()
outputpath.setFont(QFont('Arial', 10))
grid.addWidget(outputpath, 1, 1)

Lbitrate = QLabel('bit rate', root)
Lbitrate.setAlignment(Qt.AlignLeft)
Lbitrate.setFont(QFont('Arial', 10))
grid.addWidget(Lbitrate, 2, 0)

bitrate = QLineEdit()
bitrate.setFont(QFont('Arial', 10))
grid.addWidget(bitrate, 2, 1)

Lresolution = QLabel('resolution', root)
Lresolution.setAlignment(Qt.AlignLeft)
Lresolution.setFont(QFont('Arial', 10))
grid.addWidget(Lresolution, 3, 0)

resolution = QLineEdit()
resolution.setFont(QFont('Arial', 10))
grid.addWidget(resolution, 3, 1)

Lframe = QLabel('frame', root)
Lframe.setAlignment(Qt.AlignLeft)
Lframe.setFont(QFont('Arial', 10))
grid.addWidget(Lframe, 4, 0)

frame = QLineEdit()
frame.setFont(QFont('Arial', 10))
grid.addWidget(frame, 4, 1)

bar = QProgressBar()
bar.setRange(0, 100)  # 進度條範圍
bar.setValue(100)  # 進度條預設值
grid.addWidget(bar, 5, 1)

run = QPushButton('run')
run.setFont(QFont('Arial', 10))
run.clicked.connect(transform_file)
grid.addWidget(run, 6, 1)

root.show()
sys.exit(app.exec_())
