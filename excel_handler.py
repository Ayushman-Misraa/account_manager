import pandas as pd
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import Qt, QDate

class ExcelHandler:
    @staticmethod
    def save_to_excel(parent, transactions):
        try:
            path, _ = QFileDialog.getSaveFileName(
                parent, "Save File", "", "Excel Files (*.xlsx)"
            )
            if path:
                df = pd.DataFrame([{
                    'Date': t['date'].toString(Qt.ISODate),
                    'Description': t['description'],
                    'Amount': t['amount'],
                    'Type': t['type'],
                    'Category': t['category'],
                    'Person': t['person'],
                    'Status': t['status']
                } for t in transactions])
                
                df.to_excel(path, index=False)
                QMessageBox.information(parent, "Success", "Data saved successfully!")
                
        except Exception as e:
            QMessageBox.critical(parent, "Error", f"Save failed: {str(e)}")

    @staticmethod
    def load_from_excel(parent):
        try:
            path, _ = QFileDialog.getOpenFileName(
                parent, "Open File", "", "Excel Files (*.xlsx)"
            )
            if path:
                df = pd.read_excel(path)
                required = ['Date', 'Description', 'Amount', 'Type', 'Category', 'Person', 'Status']
                
                if not all(col in df.columns for col in required):
                    QMessageBox.critical(parent, "Error", "Invalid file format!")
                    return None
                
                return df.to_dict('records')
                
        except Exception as e:
            QMessageBox.critical(parent, "Error", f"Load failed: {str(e)}")
            return None