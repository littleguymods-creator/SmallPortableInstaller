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
        ##style sheets n other stuff first section
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
            commandfire = (
                "choco install firefox -y"
            )
            subprocess.Popen(["powershell", "-NoProfile", "-Command",  f'Start-Process powershell.exe -Verb RunAs -ArgumentList \'-Noprofile -NoExit -Command "{commandfire}"\''])
        def chrome(self):
           commandchrome = (
               "choco install chrome -y"
           )
           subprocess.Popen(["powershell", "-NoProfile", "-Command",  f'Start-Process powershell.exe -Verb RunAs -ArgumentList \'-Noprofile -NoExit -Command "{commandchrome}"\''])
        def brave(self):
            commandbrave = (
                "choco install brave -y"
            )
            subprocess.Popen(["powershell", "-NoProfile", "-Command",  f'Start-Process powershell.exe -Verb RunAs -ArgumentList \'-Noprofile -NoExit -Command "{commandbrave}"\''])
        def waterfox(self):
            commandwater = (
                "choco install waterfox -y"
            )
            subprocess.Popen(["powershell", "-NoProfile", "-Command",  f'Start-Process powershell.exe -Verb RunAs -ArgumentList \'-Noprofile -NoExit -Command "{commandwater}"\''])
        def librewolf(self):
            commandlibre = (
                "choco install librewolf -y"
            )
            subprocess.Popen(["powershell", "-NoProfile", "-Command",  f'Start-Process powershell.exe -Verb RunAs -ArgumentList \'-Noprofile -NoExit -Command "{commandlibre}"\''])
        def choco(self):
           command = (
               "Set-ExecutionPolicy Bypass -Scope Process -Force; iwr https://community.chocolatey.org/install.ps1 -UseBasicParsing | iex"
           )
           subprocess.Popen(["powershell", "-NoProfile", "-Command",  f'Start-Process powershell.exe -Verb RunAs -ArgumentList \'-Noprofile -NoExit -Command "{command}"\''])
        def vscodeide(self):
            subprocess.Popen(["powershell", "-NoProfile", "-Command", f'Start-Process powershell.exe -Verb RunAs', "choco install vscode.install -y"], creationflags=subprocess.CREATE_NEW_CONSOLE)
        def vscodiumide(self):
                commandvscodium = (
                    "choco install vscodium --version=1.104.36664 -y"
                )
                subprocess.Popen(["powershell", "-NoProfile", "-Command",  f'Start-Process powershell.exe -Verb RunAs -ArgumentList \'-Noprofile -NoExit -Command "{commandvscodium}"\''])
        def audacity(self):
            commandauda = (
                "choco install audacity -y"
            )
            subprocess.Popen(["powershell", "-NoProfile", "-Command",  f'Start-Process powershell.exe -Verb RunAs -ArgumentList \'-Noprofile -NoExit -Command "{commandauda}"\''])
        def vlc(self):
            commandvlc = (
                "choco install vlc"
            )
            subprocess.Popen(["powershell", "-NoProfile", "-Command",  f'Start-Process powershell.exe -Verb RunAs -ArgumentList \'-Noprofile -NoExit -Command "{commandvlc}"\''])
        def sevenzip(self):
            commandzip = (
                "choco install 7zip --version=26.0.0 -y"
            )
            subprocess.Popen(["powershell", "-NoProfile", "-Command",  f'Start-Process powershell.exe -Verb RunAs -ArgumentList \'-Noprofile -NoExit -Command "{commandzip}"\''])
        def keepass(self):
           commandpass = (
             "choco install keepass -y"
           )
           subprocess.Popen(["powershell", "-NoProfile", "-Command",  f'Start-Process powershell.exe -Verb RunAs -ArgumentList \'-Noprofile -NoExit -Command "{commandpass}"\''])
            
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

        ##second section

        ##drawing label
        self.drawingl = QLabel("Drawing Apps", self)
        self.drawingl.setAlignment(Qt.AlignCenter)
        self.drawingl.setGeometry(0, 0, 850, 500)
        self.drawingl.move(0,-150)

        ##bottom buttons
        self.firstsectiob = QPushButton("1", self)
        self.firstsectiob.move(300,450)
        self.secondsectiob = QPushButton("2", self)
        self.secondsectiob.move(450,450)

        ##buttons
        self.kritab = QPushButton("Krita", self)
        self.kritab.setGeometry(375,155,100,30)

        ##stlyesheet second section
        self.drawingl.setStyleSheet("""font-size:17pt;""")

        ##hide when app loaded
        self.drawingl.hide()
        self.kritab.hide()

        ##way more stuff
        def secondsection():
                    self.vscodeloabel.hide()
                    self.miscl.hide()
                    self.browsergroup.hide()
                    self.browserlabel.hide()
                    self.audael.hide()
                    self.miscgroup.hide()
                    self.browsergroup.hide()
                    self.codegroup.hide()
                    self.audacityb.hide()
                    self.kritab.show()
                    self.drawingl.show()
        def firstsection():
                    self.vscodeloabel.show()
                    self.miscl.show()
                    self.browsergroup.show()
                    self.browserlabel.show()
                    self.audael.show()
                    self.miscgroup.show()
                    self.browsergroup.show()
                    self.codegroup.show()
                    self.audacityb.show()
                    self.kritab.hide()
                    self.drawingl.hide()




        ##install stuff again
        def comkrita(self):
            commandkrita = "choco install krita --version=5.2.16"
            
            subprocess.Popen(["powershell", "-NoProfile", "-Command",  f'Start-Process powershell.exe -Verb RunAs -ArgumentList \'-Noprofile -NoExit -Command "{commandkrita}"\''])
        ##connect bottom buttons
        self.firstsectiob.clicked.connect(firstsection)
        self.secondsectiob.clicked.connect(secondsection)
        self.kritab.clicked.connect(comkrita)
        
        pass

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())