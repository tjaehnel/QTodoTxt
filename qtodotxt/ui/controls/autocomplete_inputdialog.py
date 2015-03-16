import sys
from PySide import QtGui
from qtodotxt.ui.controls.autocomplete_lineedit import AutoCompleteEdit
from datetime import date, timedelta
import collections

class AutoCompleteInputDialog(QtGui.QDialog):
    autocomplete_pairs = collections.OrderedDict([
        ('due:Today', ''),
        ('due:Tomorrow', ''),
        ('due:EndOfWeek', ''),
        ('due:EndOfMonth', ''),
        ('due:EndOfYear', ''),
        ('due:January', ''),
        ('due:February', ''),
        ('due:March', ''),
        ('due:April', ''),
        ('due:May', ''),
        ('due:June', ''),
        ('due:July', ''),
        ('due:August', ''),
        ('due:September', ''),
        ('due:October', ''),
        ('due:November', ''),
        ('due:December', ''),
        ('due:Monday', ''),
        ('due:Tuesday', ''),
        ('due:Wednesday', ''),
        ('due:Thursday', ''),
        ('due:Friday', ''),
        ('due:Saturday', ''),
        ('due:Sunday', ''),

    ])

    def __init__(self, values, parent=None):
        super(AutoCompleteInputDialog, self).__init__(parent)
        self._initUI(values)
        self._populateKeys(self.autocomplete_pairs)

    def _endOfMonth(self, month):
        month %= 12

        eom = date.today().replace(month=month+1, day=1) - timedelta(days=1)
        if eom < date.today():
            eom = eom.replace(year=eom.year+1)
        return 'due:'+ eom.strftime('%Y-%m-%d')

    def _dayOfWeek(self, dow):
        thisDow = date.today().isoweekday()
        addDays = (dow + 7 - thisDow) % 7
        if addDays == 0:
            addDays = 7;
        
        newDate = date.today() + timedelta(days=addDays)
        return 'due:'+ newDate.strftime('%Y-%m-%d')

    def _populateKeys(self, keys):
        today = 'due:' + date.today().strftime('%Y-%m-%d')
        tomorrow = 'due:' + (date.today() + timedelta(days = 1)).strftime('%Y-%m-%d')
        EOW = 'due:' + (date.today() + timedelta((6-date.today().weekday()) % 7)).strftime('%Y-%m-%d')
        EOM = 'due:' + (date.today().replace(month=date.today().month+1, day=1) - timedelta(days=1)).strftime('%Y-%m-%d')
        EOY = 'due:' + (date.today().replace(year=date.today().year+1, month=1, day=1) - timedelta(days=1)).strftime('%Y-%m-%d')

        keys['due:EndOfWeek'] = EOW
        keys['due:EndOfMonth'] = EOM
        keys['due:EndOfYear'] = EOY
        keys['due:Today'] = today
        keys['due:Tomorrow'] = tomorrow
        keys['due:January'] = self._endOfMonth(1)
        keys['due:February'] = self._endOfMonth(2)
        keys['due:March'] = self._endOfMonth(3)
        keys['due:April'] = self._endOfMonth(4)
        keys['due:May'] = self._endOfMonth(5)
        keys['due:June'] = self._endOfMonth(6)
        keys['due:July'] = self._endOfMonth(7)
        keys['due:August'] = self._endOfMonth(8)
        keys['due:September'] = self._endOfMonth(9)
        keys['due:October'] = self._endOfMonth(10)
        keys['due:November'] = self._endOfMonth(11)
        keys['due:December'] = self._endOfMonth(12)
        keys['due:Monday'] = self._dayOfWeek(1)
        keys['due:Tuesday'] = self._dayOfWeek(2)
        keys['due:Wednesday'] = self._dayOfWeek(3)
        keys['due:Thursday'] = self._dayOfWeek(4)
        keys['due:Friday'] = self._dayOfWeek(5)
        keys['due:Saturday'] = self._dayOfWeek(6)
        keys['due:Sunday'] = self._dayOfWeek(7)
        return keys

    def _initUI(self, values):
        self.setWindowTitle("Task Editor")
        vbox = QtGui.QVBoxLayout()

        self._label = QtGui.QLabel("Task:")
        vbox.addWidget(self._label)

        self._edit = AutoCompleteEdit(values, self.autocomplete_pairs)
        vbox.addWidget(self._edit)

        hbox = QtGui.QHBoxLayout()
        okButton = QtGui.QPushButton("Ok")
        okButton.clicked.connect(self.accept)
        cancelButton = QtGui.QPushButton("Cancel")
        cancelButton.clicked.connect(self.reject)
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.resize(500, 100)

    def textValue(self):
        return self._edit.text()

    def setTextValue(self, text):
        self._edit.setText(text)

    def setLabelText(self, text):
        self._label.setText(text)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    values = ['(A)', '(B)', '(C)', '@home', '@call', '@work', '+qtodotxt', '+sqlvisualizer']
    view = AutoCompleteInputDialog(values)
    view.show()
    sys.exit(app.exec_())  
