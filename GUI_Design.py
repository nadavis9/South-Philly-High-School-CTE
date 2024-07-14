from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QGridLayout
from PyQt5.QtGui import QIcon, QFont, QPixmap, QMovie
import sys
import random
import hashlib
import binascii

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 700, 400)
        self.setWindowTitle("Noblis Cryptographic Engine")
        self.setWindowIcon(QIcon('Noblis.png'))
        self.setStyleSheet('background-color:white')

        
        

        self.create_widget()

    key = []


    def create_widget(self):

        grid = QGridLayout()

        #define push buttons

        #define hash button
        hash_btn = QPushButton("Hash")
        hash_btn.setFont(QFont("Sanserif", 14, QFont.Weight.Bold))
        hash_btn.setStyleSheet('color:green')
        hash_btn.clicked.connect(self.clicked_hash)
        #define encrypt button
        encrypt_btn = QPushButton("Encrypt")
        encrypt_btn.setFont(QFont("Sanserif", 14, QFont.Weight.Bold))
        encrypt_btn.setStyleSheet('color:green')
        encrypt_btn.clicked.connect(self.clicked_btn)
        #define decrypt button
        decrypt_btn = QPushButton("Decrypt")
        decrypt_btn.setFont(QFont("Sanserif", 14, QFont.Weight.Bold))
        decrypt_btn.setStyleSheet('color:green')
        decrypt_btn.clicked.connect(self.clicked_decrypt)
        #define key generation button
        key_generate_btn = QPushButton("Generate Key")
        key_generate_btn.setFont(QFont("Sanserif", 14, QFont.Weight.Bold))
        key_generate_btn.setStyleSheet('color:green')
        key_generate_btn.clicked.connect(self.clicked_key_generate)

        #define text boxes
        self.encrypt_text = QLineEdit()
        self.encrypt_text.setPlaceholderText("Please enter the message you would like to encrypt")
        self.encrypt_text.setFont(QFont("Times", 10, QFont.Weight.Bold))
        self.encrypt_text.setStyleSheet('color:darkblue')
        self.hash_text = QLineEdit()
        self.hash_text.setPlaceholderText("Please enter the message you would like to hash")
        self.hash_text.setFont(QFont("Times", 10, QFont.Weight.Bold))
        self.hash_text.setStyleSheet('color:darkblue')
        self.decrypt_text = QLineEdit()
        self.decrypt_text.setPlaceholderText("Please enter the message you would like to decrypt")
        self.decrypt_text.setFont(QFont("Times", 10, QFont.Weight.Bold))
        self.decrypt_text.setStyleSheet('color:darkblue')
        self.key_generate_text = QLineEdit()
        self.key_generate_text.setPlaceholderText("Please provide the length of the key you need")
        self.key_generate_text.setStyleSheet('color:darkblue')
        self.key_generate_text.setFont(QFont("Times", 10, QFont.Weight.Bold))

        #define labels
        self.Cipher_text_display = QLabel("Cipher Text")
        self.Cipher_text_display.setFont(QFont("Sanserif", 12, QFont.Weight.Bold))
        self.Cipher_text_display.setStyleSheet('color:green')
        self.message_digest_display = QLabel("Hashed Text")
        self.message_digest_display.setFont(QFont("Sanserif", 12, QFont.Weight.Bold))
        self.message_digest_display.setStyleSheet('color:green')
        self.Plain_text_display = QLabel("Plain Text")
        self.Plain_text_display.setFont(QFont("Sanserif", 12, QFont.Weight.Bold))
        self.Plain_text_display.setStyleSheet('color:green')
        self.Key_generate_display = QLabel("Here is your key")
        self.Key_generate_display.setFont(QFont("Sanserif", 12, QFont.Weight.Bold))
        self.Key_generate_display.setStyleSheet('color:green')
        self.title = QLabel("Welcome to the Noblis Cryptographic Engine")
        self.title.setFont(QFont("Sanserif", 15, QFont.Weight.Bold))
        self.title.setStyleSheet('color:darkblue')

        #import image
        logo = QLabel(self)
        pixmap = QPixmap('Noblis.png')
        logo.setPixmap(pixmap)

        #configure layout
        #first row
        grid.addWidget(logo, 0, 0)
        grid.addWidget(self.title, 0, 1)

        #second row
        grid.addWidget(key_generate_btn, 1, 0)
        grid.addWidget(self.key_generate_text, 1, 1)
        grid.addWidget(self.Key_generate_display, 1, 2)


        #third row
        grid.addWidget(encrypt_btn, 2, 0)
        grid.addWidget(self.encrypt_text, 2, 1)
        grid.addWidget(self.Cipher_text_display, 2, 2)

        #fourth row
        grid.addWidget(decrypt_btn, 3, 0)
        grid.addWidget(self.decrypt_text, 3, 1)
        grid.addWidget(self.Plain_text_display, 3, 2)

        #fifth row
        grid.addWidget(hash_btn, 4, 0)
        grid.addWidget(self.hash_text, 4, 1)
        grid.addWidget(self.message_digest_display, 4, 2)

        self.setLayout(grid)

    
    #execute once encrypt button is pressed
    def clicked_btn(self):
        plain_text = self.encrypt_text.text()
        key = []
        for i in range(len(plain_text)):
            key.append(random.randint(1,100))

        cipher_text = "".join([chr(ord(c1)^ord(c2)) for (c1,c2) in zip(plain_text, str(key))])
        self.Cipher_text_display.setText(cipher_text)
    
    #Execute once hash button is pressed
    def clicked_hash(self):
        plain_text = self.hash_text.text()
        plain_text_formatted = plain_text.encode('utf-8')
        message = hashlib.sha256()
        message.update(plain_text_formatted)
        self.message_digest_display.setText(message.hexdigest())

    def clicked_decrypt(self):
        global key
        Cipher_text = self.decrypt_text.text()
        plain_message = "".join([chr(ord(c1)^ord(c2)) for (c1,c2) in zip(Cipher_text, str(key))])
        self.Cipher_text_display.setText(plain_message)

    def clicked_key_generate(self):
        key_length = self.key_generate_text.text()
        key = []
        for i in range(len(key_length)):
            key.append(random.randint(1,100))
            print(key)
             
        self.Key_generate_display.setText(str(key))
        

        

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())