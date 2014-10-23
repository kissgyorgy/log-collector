from PyQt4.QtGui import QMainWindow, QMessageBox
import requests
from requests.exceptions import ConnectionError
import mainwindow


class MainWindow(mainwindow.Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.send.clicked.connect(self.sendData)

    def sendData(self):
        payload = {
            'timestamp': self.timestamp.dateTime().toMSecsSinceEpoch() / 1000,
            'dim1': self.dim1.value(),
            'dim2': self.dim2.value(),
            'value': self.value.value()
        }
        try:
            res = requests.post(self.url.text(), payload)
        except ConnectionError:
            QMessageBox.critical(self, 'Hiba!', 'A szerver: "%s"\nnem elérhető!'
                                 % self.url.text())
            return

        if res.status_code == 201:
            id = res.json()['id']
            self.statusbar.showMessage('Létrehozva! Azonosító: %d.' % id)
        else:
            self.statusbar.showMessage('Küldés sikertelen! HTTP státusz: %s'
                                       % res.status_code)


def main():
    import sys
    from PyQt4.QtGui import QApplication

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    exitcode = app.exec_()
    sys.exit(exitcode)


if __name__ == '__main__':
    main()
