import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTableView, QHeaderView, QLabel, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class MainWindow2(QWidget):
    def __init__(self):
        super().__init__()

        # Create data frames
        data1 = {'Name': ['John', 'Alice', 'Bob', 'Jane'], 'Age': [25, 32, 18, 41], 'Gender': ['M', 'F', 'M', 'F']}
        self.df1 = pd.read_csv('amazon_data.csv')

        data2 = {'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'], 'Population': [8623000, 4000000, 2700000, 2300000]}
        self.df2 = pd.read_csv('flip_data.csv')

        # Create table models
        self.model1 = QStandardItemModel()
        self.model2 = QStandardItemModel()

        # Set data to models
        self.setTableModelData(self.model1, self.df1)
        self.setTableModelData(self.model2, self.df2)

        # Create table views
        self.tableView1 = QTableView()
        self.tableView2 = QTableView()

        # Set models to table views
        self.tableView1.setModel(self.model1)
        self.tableView2.setModel(self.model2)

        # Set vertical alignment to top for both tables
        self.tableView1.verticalHeader().setDefaultAlignment(Qt.AlignTop)
        self.tableView2.verticalHeader().setDefaultAlignment(Qt.AlignTop)

        # Create labels for data frames
        label1 = QLabel("Amazon")
        label2 = QLabel("Flipkart")

        # Create buttons for adding to wishlist
        button1 = QPushButton("Add to Wishlist")
        button2 = QPushButton("Add to Wishlist")

        # Create layout for each data frame
        layout1 = QVBoxLayout()
        layout1.addWidget(label1)
        layout1.addWidget(self.tableView1)
        layout1.addWidget(button1)
        layout1.setAlignment(button1, Qt.AlignRight)

        layout2 = QVBoxLayout()
        layout2.addWidget(label2)
        layout2.addWidget(self.tableView2)
        layout2.addWidget(button2)
        layout2.setAlignment(button2, Qt.AlignRight)

        # Create main layout and add data frame layouts
        mainLayout = QVBoxLayout()
        mainLayout.addLayout(layout1)
        mainLayout.addLayout(layout2)

        # Set window properties
        self.setLayout(mainLayout)
        self.setWindowTitle('Data Frames')
        self.setGeometry(100, 100, 800, 600)
        self.show()

    def setTableModelData(self, model, df):
        model.clear()
        model.setHorizontalHeaderLabels(list(df.columns))
        for i in range(df.shape[0]):
            row = [QStandardItem(str(df.iloc[i, j])) for j in range(df.shape[1])]
            model.appendRow(row)
df1.(
