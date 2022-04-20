import sys
from PyQt5.QtWidgets import *
from data import instructors, departments
from create import save


class University(QDialog):
    def store(self):
        response = QMessageBox()

        name = self.nameInput.text()
        department = self.departmentOptions.currentText()
        salary = int(self.salaryInput.text())

        try:
            values = (name, department, salary)

            saved = save(values)
            response.setWindowTitle("Success")
            response.setText("Instructor added successfully!")
            response.setIcon(QMessageBox.Information)
            response.setStandardButtons(QMessageBox.Ok)

            row = self.table.rowCount()+saved.rowcount
            self.table.setItem(row, 0, QTableWidgetItem(name))
            self.table.setItem(row, 1, QTableWidgetItem(department))
            self.table.setItem(row, 2, QTableWidgetItem(f"{salary}"))

            self.nameInput.setText("")
            self.salaryInput.setValue(0)

        except Exception as e:
            response.setWindowTitle("Error")
            response.setText(f"{e}")
            response.setDetailedText(f"{e}")
            response.setIcon(QMessageBox.Critical)
            response.setStandardButtons(QMessageBox.Close)

        x = response.exec_()

    def create(self):
        self.form = QGroupBox("Add instructor")

        f = QFormLayout()
        self.nameInput = QLineEdit()
        self.salaryInput = QSpinBox()

        self.departmentOptions = QComboBox()
        options = []
        for d in departments:
            options.append(d[0])

        self.departmentOptions.addItems(options)

        f.addRow(QLabel("Name"), self.nameInput)
        f.addRow(QLabel("Select department"), self.departmentOptions)
        f.addRow(QLabel("Salary"), self.salaryInput)

        self.form.setLayout(f)
        self.buttons = QDialogButtonBox(
            QDialogButtonBox.Save | QDialogButtonBox.Close)

    def index(self):
        self.table = QTableWidget()
        self.table.setRowCount(len(instructors))
        self.table.setColumnCount(3)

        self.table.setHorizontalHeaderItem(0, QTableWidgetItem("Name"))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem("Dept. Name"))
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem("Salary"))

        # fetch and display instructors
        row = 0
        for instructor in instructors:
            self.table.setVerticalHeaderItem(
                row, QTableWidgetItem(f"{instructor[0]}"))
            self.table.setItem(row, 0, QTableWidgetItem(instructor[1]))
            self.table.setItem(row, 1, QTableWidgetItem(instructor[2]))
            self.table.setItem(row, 2, QTableWidgetItem(f"{instructor[3]}"))
            row += 1

        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def __init__(self):
        super().__init__()
        # setting window properties
        self.departmentOptions = None
        self.salaryInput = None
        self.table = None
        self.buttons = None
        self.nameInput = None
        self.form = None
        self.title = f"University instructors"
        self.setWindowTitle(self.title)

        self.create()
        self.buttons.accepted.connect(self.store)
        self.buttons.rejected.connect(self.reject)

        self.index()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.form)
        self.layout.addWidget(self.buttons)
        self.layout.addWidget(self.table)
        self.setLayout(self.layout)

        self.show()


def main():
    app = QApplication(sys.argv)
    ex = University()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
