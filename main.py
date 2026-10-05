import sys
import subprocess

from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Small Portable Installer")
        self.setFixedSize(QSize(850,500))
        ##the label when the app starts
        self.titlelabel = QLabel("Welcome to the Small Portable Installer", self)
        self.titlelabel.move(195,10)
        ##credits label
        self.creditslabel = QLabel("Powered by PySide6 and Chocolatey", self)
        self.creditslabel.move(0,483)
        ##browser label
        self.browserlabel = QLabel("Browsers", self)
        self.browserlabel.move(375,80)
        ##MISC label
        self.miscl = QLabel("MISC", self)
        self.miscl.move(400,350)
        ##ide's label
        self.vscodeloabel = QLabel("IDE (Code Editors)", self)
        self.vscodeloabel.move(335,165)
        ##audio editor label
        self.audael = QLabel("Audio Editors", self)
        self.audael.move(355,255)
        ##buttongroup
        self.browsergroup = QWidget(self)
        self.browsergroup.setGeometry(0,0,850,250)
        self.browsergroup.move(-15,0)

        self.codegroup = QWidget(self)
        self.codegroup.setGeometry(0,0,850,250)
        self.codegroup.move(210,0)

        self.miscgroup = QWidget(self)
        self.miscgroup.setGeometry(0,0,850,500)
        self.miscgroup.move(29,0)

        self.firebtn = QPushButton("Firefox",self.browsergroup)
        self.firebtn.move(100,125)
        self.chromebtn = QPushButton("Chrome", self.browsergroup)
        self.chromebtn.move(250,125)
        self.bravebtn = QPushButton("Brave", self.browsergroup)
        self.bravebtn.move(395,125)
        self.waterbtn = QPushButton("Waterfox", self.browsergroup)
        self.waterbtn.move(545,125)
        self.librebtn = QPushButton("Librewolf", self.browsergroup)
        self.librebtn.move(695,125)
        self.chocobtn = QPushButton("Install Chocolatey", self)
        self.chocobtn.move(0,450)
        self.vscode = QPushButton("Vscode", self.codegroup)
        self.vscode.move(100,210)
        self.vscodium = QPushButton("Vscodium", self.codegroup)
        self.vscodium.move(250,210)
        self.audacityb = QPushButton("Audacity", self)
        self.audacityb.move(375,305)
        self.vlcb = QPushButton("VLC", self.miscgroup)
        self.vlcb.move(250,405)
        self.sevenzipb = QPushButton("7zip", self.miscgroup)
        self.sevenzipb.move(360,405)
        self.keepassb = QPushButton("Keepass", self.miscgroup)
        self.keepassb.move(470,405)
        ##style sheets n other stuff
        self.titlelabel.setStyleSheet("""font-size:20pt;""")
        self.browserlabel.setStyleSheet("""font-size:17pt;""")
        self.vscodeloabel.setStyleSheet("""font-size:17pt;""")
        self.audael.setStyleSheet("""font-size:17pt;""")
        self.miscl.setStyleSheet("""font-size:17pt;""")
        self.creditslabel.setStyleSheet("""font-size:10pt;""")
        self.chocobtn.setStyleSheet("""font-size:7pt;""")
        self.titlelabel.adjustSize()
        self.creditslabel.adjustSize()
        self.browserlabel.adjustSize()
        self.vscodeloabel.adjustSize()
        self.audael.adjustSize()
        ##button pressed stuff
        def firefox(self):
            subprocess.Popen(["powershell", "-NoProfile", "-Command" ,"choco install firefox -y"], creationflags=subprocess.CREATE_NEW_CONSOLE)
        def chrome(self):
            subprocess.Popen(["powershell", "-NoProfile", "-Command" ,"choco install chrome -y"], creationflags=subprocess.CREATE_NEW_CONSOLE)
        def brave(self):
            subprocess.Popen(["powershell",  "-NoProfile", "-Command", "choco install brave -y"], creationflags=subprocess.CREATE_NEW_CONSOLE)
        def waterfox(self):
            subprocess.Popen(["powershell",  "-NoProfile", "-Command", "choco install waterfox -y"], creationflags=subprocess.CREATE_NEW_CONSOLE)
        def librewolf(self):
            subprocess.Popen(["powershell",  "-NoProfile", "-Command", "choco install librewolf -y"], creationflags=subprocess.CREATE_NEW_CONSOLE)
        def choco(self):
           command = (
               "Set-ExecutionPolicy Bypass -Scope Process -Force; iwr https://community.chocolatey.org/install.ps1 -UseBasicParsing | iex"
           )
           subprocess.Popen(["powershell", "-NoProfile", "-Command",  f'Start-Process powershell.exe -Verb RunAs -ArgumentList \'-Noprofile -NoExit -Command "{command}"\''])
        def vscodeide(self):
            subprocess.Popen(["powershell", "-NoProfile", "-Command", "choco install vscode.install -y"], creationflags=subprocess.CREATE_NEW_CONSOLE)
        def vscodiumide(self):
                subprocess.Popen(["powershell", "-NoProfile", "-Command", "choco install vscodium --version=1.104.36664 -y"], creationflags=subprocess.CREATE_NEW_CONSOLE)
        def audacity(self):
            subprocess.Popen(["powershell", "-NoProfile", "-Command", "choco install audacity -y"], creationflags=subprocess.CREATE_NEW_CONSOLE)
        def vlc(self):
            subprocess.Popen(["powershell", "-NoProfile", "-Command", "choco install vlc -y"], creationflags=subprocess.CREATE_NEW_CONSOLE)
        def sevenzip(self):
            subprocess.Popen(["powershell", "-NoProfile", "-Command", "choco install 7zip --version=26.0.0 -y"], creationflags=subprocess.CREATE_NEW_CONSOLE)
        def keepass(self):
            subprocess.Popen(["powershell", "-NoProfile", "-Command", "choco install keepass -y"], creationflags=subprocess.CREATE_NEW_CONSOLE)
        ##button press idk now
        self.firebtn.clicked.connect(firefox)
        self.chromebtn.clicked.connect(chrome)
        self.bravebtn.clicked.connect(brave)
        self.waterbtn.clicked.connect(waterfox)
        self.librebtn.clicked.connect(librewolf)
        self.chocobtn.clicked.connect(choco)
        self.vscode.clicked.connect(vscodeide)
        self.vscodium.clicked.connect(vscodiumide)
        self.audacityb.clicked.connect(audacity)
        self.sevenzipb.clicked.connect(sevenzip)
        self.keepassb.clicked.connect(keepass)
        pass

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())