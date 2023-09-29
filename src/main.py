import sys
from versioncheck import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QScrollArea
from PySide6 import QtWidgets
import pymysql.cursors
import pymysql
import urllib.request
import webbrowser
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QHeaderView
from PyQt5.QtWidgets import QSizePolicy

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QTableView

from amazon import *
#from sfg import *

#DELETE FROM `wishlist` WHERE username = "suraj";


class ApplicationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_2.clicked.connect(self.sea)
        self.ui.label_2.setText("suraj")
        self.ui.clearbutton1.clicked.connect(self.delhistory)
        self.ui.clear2.clicked.connect(self.delwishlist)
        self.wish()
        self.hist()


    def delhistory(self):
        connection = pymysql.connect(host='localhost', user='root', password='', db='products', port=3306)
            
        # Set up the SQL query
        query = "DELETE FROM history WHERE username = 'suraj' "
        
        # Execute the query and fetch the results into a list of dictionaries
        with connection.cursor() as cursor:
            cursor.execute(query)
                
        connection.commit() 
        # Close the connection
        connection.close()
        self.hist()
        self.update()

    def delwishlist(self):
        connection = pymysql.connect(host='localhost', user='root', password='', db='products', port=3306)
            
        # Set up the SQL query
        query = "DELETE FROM wishlist WHERE username = 'suraj' "
        
        # Execute the query and fetch the results into a list of dictionaries
        with connection.cursor() as cursor:
            cursor.execute(query)
                
        connection.commit() 
        # Close the connection
        connection.close()
        self.wish()
        self.update()

    def sea(self):
        name1 = self.ui.lineEdit.text()
        products = listofproduct(name1)
        # Create and show MainWindow
        self.wind = MainWindow(products,self.size())
        self.wind.show()
        

    def hist(self):
        # Set up the SQL connection
        connection = pymysql.connect(host='localhost', user='root', password='', db='products', port=3306)

        # Set up the SQL query
        sql_query = "SELECT * FROM history"

        # Execute the query and fetch the results into a list of dictionaries
        with connection.cursor() as cursor:
            cursor.execute(sql_query)
            results = cursor.fetchall()

        # Close the connection
        connection.close()

        # Print the results
        buttons = [self.ui.pushButton1, self.ui.pushButton2, self.ui.pushButton3, self.ui.pushButton4, self.ui.pushButton5, self.ui.pushButton6, self.ui.pushButton7, self.ui.pushButton8, self.ui.pushButton9]

        for i in range(len(results)):
            name1 = results[i][0]
            buttons[i].setText(name1)
            image_link = results[i][1]
            buttons[i].clicked.connect(lambda: webbrowser.open(image_link))

    def wish(self):
        # Set up the SQL connection
        connection = pymysql.connect(host='localhost', user='root', password='', db='products', port=3306)

        # Set up the SQL query
        sql_query = "SELECT * FROM wishlist"

        # Execute the query and fetch the results into a list of dictionaries
        with connection.cursor() as cursor:
            cursor.execute(sql_query)
            results = cursor.fetchall()

        # Close the connection
        connection.close()

        # Print the results
        buttons = [self.ui.pushButto1, self.ui.pushButto2, self.ui.pushButto3, self.ui.pushButto4, self.ui.pushButto5, self.ui.pushButto6, self.ui.pushButto7, self.ui.pushButto8, self.ui.pushButto9]

        for i in range(len(results)):
            name1 = results[i][0]
            buttons[i].setText(name1)
            image_link = results[i][1]
            buttons[i].clicked.connect(lambda: webbrowser.open(image_link))


class ProductWidget(QWidget):
    product = {}
    def __init__(self, product):
        super().__init__()
        self.product = product
        # Create QLabel for product name
        self.name_label = QLabel(product['name'], self)

        # Create QLabel for product price
        self.price_label = QLabel(" => Rs. "+str(product['price']), self)

        # Load image from URL using QPixmap
        #pixmap = QPixmap()
        #pixmap.loadFromData(urllib.request.urlopen(product["image_link"]).read())
        #pixmap = pixmap.scaled(200,200)
        
        # Create QLabel for image and set pixmap
        #self.image_label = QLabel(self)
        #self.image_label.setPixmap(pixmap)
        
        # Create QPushButton for opening image link in web browser
        self.info_button = QPushButton("Compare", self)
        self.info_button.clicked.connect(self.open1)

        '''def scp(self):
            setval(product['image_link'])'''
        # Set layout for widget
        layout = QHBoxLayout()
        #layout.addWidget(self.image_label)
        layout.addWidget(self.name_label)
        layout.addWidget(self.price_label)
        layout.addWidget(self.info_button)
        self.setLayout(layout)

    def open1(self):
        choiceselected(self.product['image_link'])
        connection = pymysql.connect(host='localhost', user='root', password='', db='products', port=3306)
            
        # Set up the SQL query
        query = "INSERT INTO history (name, link, username) VALUES (%s, %s, %s)"
        df1 = pd.read_csv('amazon_data.csv')
        data100 = []
        nameshort = df1.iloc[0][0]
        data100.append(f"{nameshort[:30]}...")
        data100.append(df1.iloc[0][4])
        data100.append("suraj")
        print(data100)


        # Execute the query and fetch the results into a list of dictionaries
        with connection.cursor() as cursor:
            cursor.execute(query,data100)
                
        connection.commit() 
        # Close the connection
        connection.close()
        self.wind2 = MainWindow2()
        self.wind2.show()


        '''def scp(self):
            setval(product['image_link'])
        # Set layout for widget
        layout = QHBoxLayout()
        #layout.addWidget(self.image_label)
        layout.addWidget(self.name_label)
        layout.addWidget(self.price_label)
        layout.addWidget(self.info_button)
        self.setLayout(layout)'''





class MainWindow(QWidget):
    def __init__(self, products,size):
        super().__init__()
        self.resize(size)
        # Create QVBoxLayout for product widgets
        product_layout = QVBoxLayout()

        # Add ProductWidgets for each product to layout
        for product in products:
            widget = ProductWidget(product)
            product_layout.addWidget(widget)

        # Create scroll area for product layout
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(QWidget())
        scroll_area.widget().setLayout(product_layout)

        # Set layout for main window
        main_layout = QVBoxLayout()
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)


class MainWindow2(QWidget):
    def __init__(self):
        super().__init__()

        # Create data frames
        self.df1 = pd.read_csv('amazon_data.csv')

        self.df2 = pd.read_csv('flip_data.csv')
        pd.set_option('display.max_colwidth', None)
        # Create table models
        self.model1 = QStandardItemModel()
        self.model2 = QStandardItemModel()

        # Set data to models
        self.setTableModelData(self.model1, self.df1.iloc[:, :4])
        self.setTableModelData(self.model2, self.df2.iloc[:, :4])
        # Set section resize mode for tableView1 and tableView2

        # Create table views
        self.tableView1 = QTableView()
        self.tableView2 = QTableView()

        # Set models to table views
        self.tableView1.setModel(self.model1)
        self.tableView2.setModel(self.model2)

        # Set section resize mode for tableView1 and tableView2
        self.tableView1.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Set size policy for table views
        self.tableView1.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        self.tableView2.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)

        # Set vertical alignment to top for both tables
        self.tableView1.verticalHeader().setDefaultAlignment(Qt.AlignTop)
        self.tableView2.verticalHeader().setDefaultAlignment(Qt.AlignTop)
        #self.tableView1.horizontalHeader().setSectionResizeMode(0,Qt.AlignTop.Stretch)
        # Create labels for data frames
        label1 = QLabel("Amazon")
        label2 = QLabel("Flipkart")

        # Create buttons for adding to wishlist
        button1 = QPushButton("Add to Wishlist")
        button2 = QPushButton("Add to Wishlist")
        button3 = QPushButton("Link")
        button4 = QPushButton("Link")
        #button1.clicked.connect(addwishbtn1)
        # Create layout for each data frame
        layout1 = QVBoxLayout()
        layout1.addWidget(label1)
        hboxLayout = QHBoxLayout()
        layout1.addWidget(self.tableView1)
        hboxLayout.addWidget(button4)
        hboxLayout.addWidget(button1)
        hboxLayout.addStretch()
        layout1.addLayout(hboxLayout)
        layout1.setAlignment(button1, Qt.AlignRight)
        layout1.setAlignment(button4, Qt.AlignLeft)

        layout2 = QVBoxLayout()
        layout2.addWidget(label2)
        hboxLayout = QHBoxLayout()
        layout2.addWidget(self.tableView2)
        hboxLayout.addWidget(button3)
        hboxLayout.addWidget(button2)
        hboxLayout.addStretch()
        layout2.addLayout(hboxLayout)
        layout2.setAlignment(button2, Qt.AlignRight)
        layout2.setAlignment(button3, Qt.AlignLeft)

        # Create main layout and add data frame layouts
        mainLayout = QVBoxLayout()
        mainLayout.addLayout(layout1)
        mainLayout.addLayout(layout2)

        # Set window properties
        self.setLayout(mainLayout)
        self.setWindowTitle('Data Frames')
        self.setGeometry(100, 100, 1800, 600)
        self.show()

        def addwishbtn1(self):
            # Set up the SQL connection
            connection = pymysql.connect(host='localhost', user='root', password='', db='products', port=3306)
            
            # Set up the SQL query
            query = "INSERT INTO wishlist (name, link, username) VALUES (%s, %s, %s)"
            df1 = pd.read_csv('amazon_data.csv')
            data100 = []
            nameshort = df1.iloc[0][0]
            data100.append(f"{nameshort[:30]}...")
            data100.append(df1.iloc[0][4])
            data100.append("suraj")
            print(data100)


            # Execute the query and fetch the results into a list of dictionaries
            with connection.cursor() as cursor:
                cursor.execute(query,data100)
                
            connection.commit() 
            # Close the connection
            connection.close()
        
        button1.clicked.connect(addwishbtn1)

        def addwishbtn2(self):
            # Set up the SQL connection
            connection = pymysql.connect(host='localhost', user='root', password='', db='products', port=3306)
            
            # Set up the SQL query
            query = "INSERT INTO wishlist (name, link, username) VALUES (%s, %s, %s)"
            df2 = pd.read_csv('flip_data.csv')
            data100 = []
            nameshort = df2.iloc[0][0]
            data100.append(f"{nameshort[:30]}...")
            data100.append(df2.iloc[0][4])
            data100.append("suraj")
            print(data100)


            # Execute the query and fetch the results into a list of dictionaries
            with connection.cursor() as cursor:
                cursor.execute(query,data100)
                
            connection.commit() 
            # Close the connection
            connection.close()
        
        button2.clicked.connect(addwishbtn2)
        
        df1 = pd.read_csv('amazon_data.csv')
        df2 = pd.read_csv('flip_data.csv')
        image_link1 = df1.iloc[0][4]
        image_link2 = df2.iloc[0][4]
        button4.clicked.connect(lambda: webbrowser.open(image_link1))
        button3.clicked.connect(lambda: webbrowser.open(image_link2))
    def setTableModelData(self, model, df):
        model.clear()
        model.setHorizontalHeaderLabels(list(df.columns))
        for i in range(df.shape[0]):
            row = [QStandardItem(str(df.iloc[i, j])) for j in range(df.shape[1])]
            model.appendRow(row)


def main():
    app = QApplication([])
    application = ApplicationWindow()
    application.show()
    app.exec_()

if __name__ == '__main__':
    main()

