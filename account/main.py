import sys
from PyQt5.QtCore import Qt, QDate, QModelIndex
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QDate, Qt
from ui_main_window import MainWindow
from transaction_manager import TransactionModel
from excel_handler import ExcelHandler
from summary_manager import SummaryManager

class AccountingApp(MainWindow):
    def __init__(self):
        super().__init__()
        self.transactions = []
        self.model = TransactionModel()
        self.trans_table.setModel(self.model)
        
        self.add_btn.clicked.connect(self.add_transaction)
        self.actions['save'].triggered.connect(self.save_data)
        self.actions['load'].triggered.connect(self.load_data)
        self.actions['exit'].triggered.connect(self.close)
        
    def add_transaction(self):
        try:
            if self.trans_type.currentIndex() == 0: 
                transaction = {
                    'date': self.date_edit.date(),
                    'description': self.desc_edit.text(),
                    'amount': float(self.amount_edit.text()),
                    'type': self.type_combo.currentText(),
                    'category': self.category_combo.currentText(),
                    'person': '',
                    'status': ''
                }
            else:  # Give/Take
                transaction = {
                    'date': self.date_edit.date(),
                    'description': self.give_take_desc.text(),
                    'amount': float(self.give_take_amount.text()),
                    'type': 'Debit' if self.give_take_combo.currentText() == 'Given' else 'Credit',
                    'category': 'Money Transfer',
                    'person': self.person_edit.text(),
                    'status': self.give_take_combo.currentText()
                }
                if not transaction['person']:
                    QMessageBox.warning(self, "Warning", "Please enter person/entity name!")
                    return

            self.model.add_transaction(transaction)
            self.clear_fields()
            SummaryManager.update_summary(self.model.transactions, self.summary_labels)
            
        except ValueError:
            QMessageBox.critical(self, "Error", "Invalid amount entered!")

    def save_data(self):
        ExcelHandler.save_to_excel(self, self.model.transactions)

    def load_data(self):
        data = ExcelHandler.load_from_excel(self)
        if data:
            transactions = [{
                'date': QDate.fromString(str(t['Date']), Qt.ISODate),
                'description': t['Description'],
                'amount': t['Amount'],
                'type': t['Type'],
                'category': t['Category'],
                'person': t['Person'],
                'status': t['Status']
            } for t in data]
            
            self.model.load_transactions(transactions)
            SummaryManager.update_summary(transactions, self.summary_labels)

    def clear_fields(self):
        self.amount_edit.clear()
        self.desc_edit.clear()
        self.person_edit.clear()
        self.give_take_amount.clear()
        self.give_take_desc.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AccountingApp()
    window.show()
    sys.exit(app.exec_())