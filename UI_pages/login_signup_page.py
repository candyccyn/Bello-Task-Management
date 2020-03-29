import sys 
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class SignUpWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setColor()
        self.username_label = QLabel("Username: ")
        self.username_label.setFont(QFont("Century Gothic", 10))
        self.username_lineEdit = QLineEdit()
        self.password_label = QLabel("Password: ")
        self.password_label.setFont(QFont("Century Gothic", 10))
        self.password_lineEdit = QLineEdit()
        self.confirm_pass_label = QLabel("Confirm Password: ")
        self.confirm_pass_label.setFont(QFont("Century Gothic", 10))
        self.confirm_pass_lineEdit = QLineEdit()
        self.signup_btn = QPushButton("SIGN UP")
        self.signup_btn.clicked.connect(self.signUP)
        self.isHasUser = False
        self.signup_btn.setFont(QFont("Moon", 10,QFont.Bold))
        self.signup_layout = QFormLayout()
        self.username_label.setContentsMargins(30,30,10,15)
        self.username_lineEdit.setContentsMargins(0,30,30,15)
        self.signup_layout.addRow(self.username_label, self.username_lineEdit)
        self.password_label.setContentsMargins(30,0,10,15)
        self.password_lineEdit.setContentsMargins(0,0,30,15)
        self.signup_layout.addRow(self.password_label, self.password_lineEdit)
        self.confirm_pass_label.setContentsMargins(30,0,10,25)
        self.confirm_pass_lineEdit.setContentsMargins(0,0,30,25)
        self.signup_layout.addRow(self.confirm_pass_label,self.confirm_pass_lineEdit)
        self.signup_layout.addRow(self.signup_btn) 
        self.setLayout(self.signup_layout)
    def setColor(self):
        self.pal = QPalette()
        self.setAutoFillBackground(True)
        self.pal.setColor(QPalette.Window,QColor(196,196,196))
        self.setPalette(self.pal)
    def signUP(self):
        if(self.isHasUser == True):
            print("Success Sign Up")
        else:
            dialog = QDialog(self)
            dialog.setWindowTitle("Error")
            layout = QVBoxLayout()
            errMessage = QLabel(self)
            errMessage.setText("This number is already registered")
            close = QPushButton('Close')
            close.clicked.connect(dialog.close)
            layout.addWidget(errMessage)
            layout.addWidget(close)
            dialog.setLayout(layout)
            dialog.show()
            print("Error Message")
class LoginWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setColor()
        self.username_label = QLabel("Username: ")
        self.username_label.setFont(QFont("Century Gothic", 10))
        self.username_lineEdit = QLineEdit()
        self.password_label = QLabel("Password: ")
        self.password_label.setFont(QFont("Century Gothic", 10))
        self.password_lineEdit = QLineEdit()
        self.login_btn = QPushButton("LOG IN")
        self.login_btn.clicked.connect(self.login)
        #self.login_btn.setFixedSize(100,30)
        self.login_layout = QFormLayout()
        self.username_label.setContentsMargins(30,50,10,25)
        self.username_lineEdit.setContentsMargins(0,50,30,25)
        self.login_layout.addRow(self.username_label, self.username_lineEdit)
        self.password_label.setContentsMargins(30,0,10,35)
        self.password_lineEdit.setContentsMargins(0,0,30,35)
        self.login_layout.addRow(self.password_label, self.password_lineEdit)
        self.login_btn.setFont(QFont("Moon", 10,QFont.Bold))
        self.login_layout.addRow(self.login_btn)
        self.setLayout(self.login_layout)
    def setColor(self):
        self.pal = QPalette()
        #self.color_white = QColor((196,196,196))
        self.setAutoFillBackground(True)
        self.pal.setColor(QPalette.Window,QColor(196,196,196))
        self.setPalette(self.pal)
    def login(self):
        print("LOG IN success")
class Login_Signin_Page(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.tabWidget = QTabWidget()
        self.login= LoginWidget()
        self.tabWidget.setFixedSize(313,263)
        self.signup = SignUpWidget()
        self.tabWidget.setFont(QFont("Moon", 8))
        self.tabWidget.addTab(self.login, "LOG IN")
        self.tabWidget.addTab(self.signup, "SIGN UP")
        self.setWindowTitle("Bello project")
        self.label = QLabel("Bello")
        self.layout = QVBoxLayout()
        self.setContentsMargins(150,60,20,140)
        self.label.setContentsMargins(140,0,0,25)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.tabWidget)
        self.label.setFont(QFont("Moon", 24,QFont.Bold))
        self.setLayout(self.layout)
        self.icon_Bello = QPixmap("images/iconBello.png")

    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)
        p.setPen(QColor(255,219,128))
        p.setBrush(QColor(255,219,128))
        p.drawEllipse(QPoint(20,350), 125, 125)
        p.drawEllipse(QPoint(620,140), 125, 125)
        p.drawPixmap(QRect(248,60,40,40),self.icon_Bello)
        p.end()
    
def main():
    app = QApplication(sys.argv)
    w = Login_Signin_Page()
    w.setFixedSize(640, 480)
    w.show()
    return app.exec_()
if __name__ == "__main__":
    sys.exit(main())