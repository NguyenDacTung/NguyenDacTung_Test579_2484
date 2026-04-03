import sys
import os
from PyQt5 import QtWidgets, uic
# Import class xử lý logic của bạn
from playfair_cipher import PlayFairCipher 

class PlayfairApp(QtWidgets.QDialog): # Dùng QDialog vì file .ui của bạn là QDialog
    def __init__(self):
        super(PlayfairApp, self).__init__()
        
        # Đường dẫn đến file .ui
        ui_path = os.path.join(os.path.dirname(__file__), 'playfair.ui')
        uic.loadUi(ui_path, self) # Load trực tiếp file UI

        self.cipher = PlayFairCipher()

        # Giả sử bạn đã đặt tên nút trong Qt Designer là btn_encrypt và btn_decrypt
        # Nếu chưa đặt tên, bạn cần mở Qt Designer đặt lại hoặc sửa tên ở đây
        if hasattr(self, 'btn_encrypt'):
            self.btn_encrypt.clicked.connect(self.handle_encrypt)
        if hasattr(self, 'btn_decrypt'):
            self.btn_decrypt.clicked.connect(self.handle_decrypt)

    def handle_encrypt(self):
        key = self.txt_key.text() # Tên txt_key khớp với hình bạn gửi
        # Giả sử ô nhập liệu là txt_input và ô kết quả là txt_output
        text = self.txt_input.toPlainText()
        
        matrix = self.cipher.create_playfair_matrix(key)
        result = self.cipher.playfair_encrypt(text, matrix)
        self.txt_output.setPlainText(result)

    def handle_decrypt(self):
        key = self.txt_key.text()
        text = self.txt_input.toPlainText()
        
        matrix = self.cipher.create_playfair_matrix(key)
        result = self.cipher.playfair_decrypt(text, matrix)
        self.txt_output.setPlainText(result)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PlayfairApp()
    window.show()
    sys.exit(app.exec_())