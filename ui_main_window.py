from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont, QDoubleValidator

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Personal Account Manager")
        self.setGeometry(100, 100, 1200, 800)
        self.setup_ui()
    
    def setup_ui(self):
        # Main Widget and Layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)
        
        # Left Panel - Input Section
        left_panel = QFrame()
        left_panel.setFixedWidth(400)
        left_layout = QVBoxLayout(left_panel)
        
        # Transaction Type Selector
        self.trans_type = QTabWidget()
        self.regular_tab = QWidget()
        self.give_take_tab = QWidget()
        self.trans_type.addTab(self.regular_tab, "Regular Transaction")
        self.trans_type.addTab(self.give_take_tab, "Give/Take Money")
        
        # Regular Transaction Form
        self.setup_regular_tab()
        self.setup_give_take_tab()
        
        # Add Transaction Button
        self.add_btn = QPushButton("➕ Add Transaction")
        self.add_btn.setStyleSheet("""
            QPushButton {
                background: #4CAF50;
                color: white;
                padding: 12px;
                border-radius: 6px;
                font-size: 14px;
            }
            QPushButton:hover { background: #45a049; }
        """)
        
        left_layout.addWidget(self.trans_type)
        left_layout.addWidget(self.add_btn)
        
        # Right Panel - Display Section
        right_panel = QFrame()
        right_layout = QVBoxLayout(right_panel)
        
        # Transaction Table
        self.trans_table = QTableView()
        self.trans_table.setSelectionBehavior(QTableView.SelectRows)
        self.trans_table.setStyleSheet("""
            QTableView {
                background: #f8f9fa;
                alternate-background-color: #e9ecef;
                border: 1px solid #dee2e6;
            }
            QHeaderView::section { background: #e9ecef; }
        """)
        
        # Summary Cards
        self.summary_group = QGroupBox("Financial Summary")
        summary_layout = QHBoxLayout(self.summary_group)
        
        self.summary_labels = {
            'credit': QLabel("Total Credit:\n₹0.00"),
            'debit': QLabel("Total Debit:\n₹0.00"),
            'balance': QLabel("Net Balance:\n₹0.00"),
            'given': QLabel("Money Given:\n₹0.00"),
            'taken': QLabel("Money Taken:\n₹0.00")
        }
        
        for label in self.summary_labels.values():
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("""
                QLabel {
                    background: white;
                    border-radius: 8px;
                    padding: 15px;
                    border: 1px solid #dee2e6;
                    font-weight: 500;
                }
            """)
            summary_layout.addWidget(label)
        
        right_layout.addWidget(self.trans_table)
        right_layout.addWidget(self.summary_group)
        
        # Add Panels to Main Layout
        main_layout.addWidget(left_panel)
        main_layout.addWidget(right_panel)
        
        # Menu Bar
        self.setup_menu()
        
    def setup_regular_tab(self):
        layout = QFormLayout(self.regular_tab)
        layout.setVerticalSpacing(15)
        
        self.date_edit = QDateEdit()
        self.date_edit.setDate(QDate.currentDate())
        self.date_edit.setCalendarPopup(True)
        
        self.amount_edit = QLineEdit()
        self.amount_edit.setValidator(QDoubleValidator())
        
        self.type_combo = QComboBox()
        self.type_combo.addItems(["Credit", "Debit"])
        
        self.category_combo = QComboBox()
        self.category_combo.addItems([
            "Food", "Transport", "Utilities", 
            "Salary", "Other"
        ])
        
        self.desc_edit = QLineEdit()
        
        layout.addRow("Date:", self.date_edit)
        layout.addRow("Amount (₹):", self.amount_edit)
        layout.addRow("Type:", self.type_combo)
        layout.addRow("Category:", self.category_combo)
        layout.addRow("Description:", self.desc_edit)
        
    def setup_give_take_tab(self):
        layout = QFormLayout(self.give_take_tab)
        layout.setVerticalSpacing(15)
        
        self.person_edit = QLineEdit()
        self.give_take_combo = QComboBox()
        self.give_take_combo.addItems(["Given", "Taken"])
        self.give_take_amount = QLineEdit()
        self.give_take_amount.setValidator(QDoubleValidator())
        self.give_take_desc = QLineEdit()
        
        layout.addRow("Person/Entity:", self.person_edit)
        layout.addRow("Type:", self.give_take_combo)
        layout.addRow("Amount (₹):", self.give_take_amount)
        layout.addRow("Description:", self.give_take_desc)
        
    def setup_menu(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        
        save_action = QAction("💾 Save to Excel", self)
        load_action = QAction("📂 Load from Excel", self)
        exit_action = QAction("🚪 Exit", self)
        
        file_menu.addAction(save_action)
        file_menu.addAction(load_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)
        
        self.actions = {
            'save': save_action,
            'load': load_action,
            'exit': exit_action
        }