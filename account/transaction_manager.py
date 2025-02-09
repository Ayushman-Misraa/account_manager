from PyQt5.QtCore import QAbstractTableModel, Qt, QDate, QModelIndex
from PyQt5.QtGui import QColor

class TransactionModel(QAbstractTableModel):
    headers = ["Date", "Description", "Amount", "Type", "Category", "Person", "Status"]
    
    def __init__(self, transactions=None):
        super().__init__()
        self.transactions = transactions or []

    def rowCount(self, parent=None):
        return len(self.transactions)

    def columnCount(self, parent=None):
        return len(self.headers)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            trans = self.transactions[index.row()]
            return [
                trans['date'].toString(Qt.ISODate),
                trans['description'],
                f"₹{trans['amount']:.2f}",
                trans['type'],
                trans['category'],
                trans['person'],
                trans['status']
            ][index.column()]
            
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignCenter if index.column() in [2,3,6] else Qt.AlignLeft

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.headers[section]

    def add_transaction(self, transaction):
        self.beginInsertRows(QModelIndex(), len(self.transactions), len(self.transactions))
        self.transactions.append(transaction)
        self.endInsertRows()

    def load_transactions(self, transactions):
        self.beginResetModel()
        self.transactions = transactions
        self.endResetModel()