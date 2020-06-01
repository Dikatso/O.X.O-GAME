# Dikatso Moshweunyane
# 25 May 2020
# OXO GUI

import sys
from PyQt5.QtWidgets import* # imports PyQt5 modules
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class OXO_GUI(QWidget):
    def __init__(self,parent = None):
        QWidget.__init__(self, parent)
        self.setGeometry(250,250,600,300)
        self.setWindowTitle("OXO GAME")
        
        # Create QLabels
        self.heading_label = QLabel("~~~~~ O X O GAME ~~~~~")
        self.heading_label.setFont(QFont("Courier New Bold Italic",20,10))
        self.heading_label.setAlignment(Qt.AlignHCenter)
        
        self.grid_heading_label = QLabel("THE GAME")
        self.grid_heading_label.setAlignment(Qt.AlignHCenter)
        self.grid_heading_label.setFont(QFont("Courier New Bold",15,7))
        
        self.server_label = QLabel("SERVER :")
        self.server_label.setFont(QFont("Courier New Bold",13,5))
        
        self.shape_label = QLabel("YOUR SHAPE        ----------------------------->  ")
        self.shape_label.setAlignment(Qt.AlignVCenter)
        self.shape_label.setFont(QFont("Courier New Bold",13,5))
        
        self.server_messages_label = QLabel("SERVER MESSAGES ")
        self.server_messages_label.setAlignment(Qt.AlignHCenter)
        self.server_messages_label.setFont(QFont("Courier New Bold",13,5))
        
        
        #Create QLine Edit Box
        self.server_input = QLineEdit()
        
        # Create Pushbuttons and ToolButton
        self.connect_button = QPushButton("Connect")        
        self.quit_button = QPushButton("Quit")
        
        self.shape_button = QToolButton()
        self.shape_button.setIconSize(QSize(40,45))
        self.shape_button.setIcon(QIcon("nought.gif"))
        
        
        # Create QTextEdit for reading server messages 
        self.server_messages = QPlainTextEdit("* * * * * * * * * * Server Messages Will Be Displayed Here * * * * * * * * * *")
        self.server_messages.setFont(QFont("Courier New Bold"))
        self.server_messages.setReadOnly(True)
        
        # Create Playing Board
        playing_board_layout = QGridLayout()
        
        self.button_0 = QToolButton()
        self.button_0.setFixedSize(95,95)
        self.button_0.setText("0")
        
        self.button_1 = QToolButton()
        self.button_1.setFixedSize(95,95)
        self.button_1.setText("1")
        
        self.button_2 = QToolButton()
        self.button_2.setFixedSize(95,95)
        self.button_2.setText("2")
        
        self.button_3 = QToolButton()
        self.button_3.setFixedSize(95,95)
        self.button_3.setText("3")
        
        self.button_4 = QToolButton()
        self.button_4.setFixedSize(95,95)
        self.button_4.setText("4")
        
        self.button_5 = QToolButton()
        self.button_5.setFixedSize(95,95)
        self.button_5.setText("5")
        
        self.button_6 = QToolButton()
        self.button_6.setFixedSize(95,95)
        self.button_6.setText("6")
        
        self.button_7 = QToolButton()
        self.button_7.setFixedSize(95,95)
        self.button_7.setText("7")
        
        self.button_8 = QToolButton()
        self.button_8.setFixedSize(95,95)
        self.button_8.setText("8")
        
        # Connecting buttons to slots
        self.connect_button.clicked.connect(self.clicked_connect)
        self.quit_button.clicked.connect(self.clicked_quit)
        self.button_0.clicked.connect(lambda : self.clicked_button(0))
        self.button_1.clicked.connect(lambda : self.clicked_button(1))
        self.button_2.clicked.connect(lambda : self.clicked_button(2))
        self.button_3.clicked.connect(lambda : self.clicked_button(3))
        self.button_4.clicked.connect(lambda : self.clicked_button(4))
        self.button_5.clicked.connect(lambda : self.clicked_button(5))
        self.button_6.clicked.connect(lambda : self.clicked_button(6))
        self.button_7.clicked.connect(lambda : self.clicked_button(7))
        self.button_8.clicked.connect(lambda : self.clicked_button(8))
        
        # Organising QToolButtons
        playing_board_layout.addWidget(self.button_0,0,0,1,1)
        playing_board_layout.setHorizontalSpacing(0)
        playing_board_layout.addWidget(self.button_1,0,1,1,1)
        playing_board_layout.setHorizontalSpacing(0)
        playing_board_layout.addWidget(self.button_2,0,2,1,1)
        playing_board_layout.setHorizontalSpacing(0)
        playing_board_layout.addWidget(self.button_3,1,0,1,1)
        playing_board_layout.setHorizontalSpacing(0)
        playing_board_layout.addWidget(self.button_4,1,1,1,1)
        playing_board_layout.setHorizontalSpacing(0)
        playing_board_layout.addWidget(self.button_5,1,2,1,1)
        playing_board_layout.setHorizontalSpacing(0)
        playing_board_layout.addWidget(self.button_6,2,0,1,1)
        playing_board_layout.setHorizontalSpacing(0)
        playing_board_layout.addWidget(self.button_7,2,1,1,1)
        playing_board_layout.setHorizontalSpacing(0)
        playing_board_layout.addWidget(self.button_8,2,2,1,1)
                
        playing_board_widget =QWidget()
        playing_board_widget.setLayout(playing_board_layout)
        
        # Organising grid heading
        grid_heading_layout = QVBoxLayout()
        grid_heading_layout.addWidget(self.grid_heading_label)
        grid_heading_layout_widget = QWidget()
        grid_heading_layout_widget.setLayout(grid_heading_layout)
        
        # Organising grid heading and playing grid
        game_grid_layout = QVBoxLayout()
        game_grid_layout.addWidget(grid_heading_layout_widget)
        game_grid_layout.addWidget(playing_board_widget)
        game_grid_layout_widget = QWidget()
        game_grid_layout_widget.setLayout(game_grid_layout)
        
        
        # Organising shape display
        shape_display_layout = QHBoxLayout()
        shape_display_layout.addWidget(self.shape_label)
        shape_display_layout.addWidget(self.shape_button)
        shape_display_widget = QWidget()
        shape_display_widget.setLayout(shape_display_layout)
        
        # Organising shape display and server messages
        server_messages_layout = QGridLayout()
        server_messages_layout.addWidget(self.server_messages_label,2,0)
        server_messages_layout.addWidget(self.server_messages,3,0)
        server_messages_widget = QWidget()
        server_messages_widget.setLayout(server_messages_layout)
        
        # Organising shape display and server messages
        bottom_info_layout = QVBoxLayout()
        bottom_info_layout.addWidget(shape_display_widget)
        bottom_info_layout.addWidget(server_messages_widget)
        bottom_info_widget = QWidget()
        bottom_info_widget.setLayout(bottom_info_layout)
        
        # Organising server connection label, QlineEdit and button
        top_info_layout = QGridLayout()
        top_info_layout.addWidget(self.server_label,0,0)
        top_info_layout.addWidget(self.server_input,0,1)
        top_info_layout.addWidget(self.connect_button,0,2)
        top_info_widget = QWidget()
        top_info_widget.setLayout(top_info_layout)
        
        # Organising grid with shape display and server messages
        horizonal_box = QHBoxLayout()
        horizonal_box.addWidget(bottom_info_widget)
        horizonal_box.addWidget(game_grid_layout_widget)
        horizonal_box_widget = QWidget()
        horizonal_box_widget.setLayout(horizonal_box)
        
        # Inserting widgets to main window
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.heading_label)
        main_layout.addWidget(top_info_widget)
        main_layout.addWidget(horizonal_box_widget)
        main_layout.addWidget(self.quit_button)
        
        self.setLayout(main_layout)
        
    def clicked_connect(self):
        self.server_messages.appendPlainText("Server Succesfully Connected")
    
    def clicked_quit(self):
        self.close()
        
    def clicked_button(self, n):
        self.server_messages.appendPlainText('Button {0} clicked'.format(n))


# Stylesheet to help describe the style of the GUI
stylesheet = """
QWidget{
        background-color: #3a3a3a;
        color: #fff;
        selection-background-color: #b78620;
        selection-color: #000;
        }

QLabel{
        background-color: transparent;
        color: #fff;
        }

QToolBar{
        background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(69, 69, 69, 255),stop:1 rgba(58, 58, 58, 255));
        border-top: none;
        border-bottom: 1px solid #4f4f4f;
        border-left: 1px solid #4f4f4f;
        border-right: 1px solid #4f4f4f;        
        background-color: transparent;
        color: #fff;
        padding: 5px;
        padding-left: 8px;
        padding-right: 8px;
        margin-left: 1px;
        }


QToolBar::separator{
        background-color: #2e2e2e;
        width: 1px;
        }



QToolButton:hover{
        background-color: rgba(183, 134, 32, 20%);
        border: 1px solid #b78620;
        color: #fff;
        }


QToolButton:pressed{
        background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));
        border: 1px solid #b78620;
        }


QToolButton:checked{
        background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));
        border: 1px solid #222;
        }
QPushButton{
        background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));
        color: #ffffff;
        min-width: 80px;
        border-style: solid;
        border-width: 1px;
        border-radius: 3px;
        border-color: #051a39;
        padding: 5px;
        }


QPushButton::flat{
        background-color: transparent;
        border: none;
        color: #fff;
        }


QPushButton::disabled{
        background-color: #404040;
        color: #656565;
        border-color: #051a39;
        }


QPushButton::hover{
        background-color: rgba(183, 134, 32, 20%);
        border: 1px solid #b78620;
        }


QPushButton::pressed{
        background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49, 49, 49, 255));
        border: 1px solid #b78620;
        }


QPushButton::checked{
        background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49, 49, 49, 255));
        border: 1px solid #222;
        }



QLineEdit{
        background-color: #131313;
        color : #eee;
        border: 1px solid #343434;
        border-radius: 2px;
        padding: 3px;
        padding-left: 5px;
        }
        
QTextEdit
{
        background-color: #131313;
        color : #eee;
        border: 1px solid #343434;
        border-radius: 2px;
        padding: 3px;
        padding-left: 5px;

}
"""
def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    abs_widget = OXO_GUI()
    abs_widget.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()