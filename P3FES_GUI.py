from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
import sys
from Data.Party_Unmodded import *
from Data.Levels_Unmodded import *

yukSkills = []
junSkills = []
akiSkills = []
mitSkills = []
aigSkills = []
koroSkills = []
kenSkills = []
shinSkills = []
metSkills = []

# app class
class P3SkillEditor(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        
        self.setWindowIcon(QIcon("icon.png"))
        
        self.instructions()
        self.configureWindows()
        self.centerWindow()
        self.configureTitleFrame()
        self.configureSelectionGameFrame()
        
        self.stackedWidgetFrame()
        self.partyWidget()
        self.calendarWidget()
        self.pnachBtn()
        
        self.game_flag = 0
    
    def instructions(self):
        QMessageBox.information(self, "Instructions", "        1 - This GUI is for The Journey game mode only!\n\
        2 - Enter date (days & months)\n\
        3 - Enter levels of your party members (if you wanna skip, enter 0)\n\
        4 - Click the 'Create .PNACH file' button to create the cheat code\n\
        5 - The .pnach file will be created within this folder.")
    
    def configureWindows(self):
        self.setWindowTitle("P3 Skill Editor")
        self.setGeometry(0, 0, 800, 600)
        self.setMinimumSize(self.width(), self.height())
        self.setMaximumSize(self.width(), self.height())
        self.setStyleSheet("QMainWindow {background-color: #A9CCE3}")
    
    def centerWindow(self):
        geometryFrame = self.frameGeometry()
        centerPoint = QGuiApplication.primaryScreen().availableGeometry().center()
        geometryFrame.moveCenter(centerPoint)
        self.move(geometryFrame.topLeft())
        
    def configureTitleFrame(self):
        topBarFrame = QFrame(self)
        topBarFrame.setStyleSheet("QFrame {background-color: #D4E6F1; border: 2px solid #1A5276; border-radius: 5px; padding: 5px}\
            QLabel {color: black; background-color: #7FB3D5; border: none; padding-top: 15}")
        topBarFrame.setGeometry(5, 5, 300, 90)
        
        title = QLabel(topBarFrame, text="P3 Skill Editor", font=QFont("p5hatty", 40))
        title.setGeometry(5, 5, 0, 0)
        title.adjustSize()
        
        topBarLayout = QHBoxLayout(topBarFrame)
        topBarLayout.addWidget(title)
        topBarLayout.setAlignment(Qt.AlignLeft)
        topBarLayout.setContentsMargins(0, 0, 0, 0)
    
    def configureSelectionGameFrame(self):
        selectionFrame = QFrame(self)
        selectionFrame.setGeometry(310, 5, 485, 90)
        selectionFrame.setStyleSheet("QFrame {background-color: #D4E6F1; border: 2px solid #1A5276; border-radius: 5px; padding: 5px}\
            QLabel {border: none}")
        
        self.selectionBox = QComboBox(selectionFrame, font=QFont("p5hatty", 22))
        self.selectionBox.setGeometry(5, 5, 475, 30)
        self.selectionBox.setStyleSheet("QComboBox {color: black; background-color: #7FB3D5; border: 2px solid #1A5276; border-radius: 5px; padding-top: 3}\
            QComboBox:hover {color: black; border: 2px solid #2471A3; background-color: #EAF2F8; padding-top: 4}\
                QComboBox::drop-down {border: none}\
                    ")
        gameList = ["The Journey"]
        self.selectionBox.addItems(gameList)
        
        selectButton = QPushButton(selectionFrame, text="Select game", font=QFont("p5hatty", 20), clicked=self.selectionEvent)
        selectButton.setStyleSheet("QPushButton {color: black; background-color: #7FB3D5; border: 2px solid #1A5276; border-radius: 5px; padding-top: 3}\
            QPushButton:hover:!pressed {background-color: #EAF2F8; border: 2px solid #2471A3}")
        
        selectionLayout = QVBoxLayout(selectionFrame)
        selectionLayout.addWidget(self.selectionBox)
        selectionLayout.addWidget(selectButton)
    
    def stackedWidgetFrame(self):
        stackedWidgetFrame = QFrame(self)
        stackedWidgetFrame.setGeometry(5, 100, 790, 450)
        stackedWidgetFrame.setStyleSheet("QFrame {background-color: #D4E6F1; border: 2px solid #1A5276; border-radius: 5px; padding: 5px}")
        
        self.mainPageWidget = QWidget()
        
        self.sWidget = QStackedWidget(stackedWidgetFrame)
        self.sWidget.setStyleSheet("border: none;")
        self.sWidget.setGeometry(5, 5, 780, 480)
        self.sWidget.addWidget(self.mainPageWidget)
        
        self.sWidget.setCurrentIndex(0)
        
        sWidgetLayout = QVBoxLayout(stackedWidgetFrame)
        sWidgetLayout.addWidget(self.sWidget)
    
    def partyWidget(self):
        frame = QFrame(self.mainPageWidget)
        frame.setMinimumSize(300, 405)
        frame.setStyleSheet("QFrame {background-color: transparent; border-radius: 10px}\
            QLineEdit {background-color: #D4E6F1; border: 2px solid #1A5276; border-radius: 5px;}\
                QLabel {background-color: #D4E6F1; border: 2px solid #2980B9; border-radius: 5px; padding-top: 10}\
                    QLineEdit:hover {color: black; border: 2px solid #2471A3; background-color: #EAF2F8; padding-top: 3}")
        frame.adjustSize()
        
        pLabel = QLabel(frame, text="Set Party Levels", font=QFont("p5hatty", 24))
        pLabel.setGeometry(5, 5, 300, 45)
        pLabel.setAlignment(Qt.AlignCenter)
        
        lineEdit_height = 55
        
        self.yukariEdit = QLineEdit(frame, text="Yukari", font=QFont("p5hatty", 24))
        self.yukariEdit.setGeometry(6, lineEdit_height, 300, 37)
        
        self.junpeiEdit = QLineEdit(frame, text="Junpei", font=QFont("p5hatty", 24))
        self.junpeiEdit.setGeometry(6, lineEdit_height * 1.7, 300, 37)
        
        self.akihikoEdit = QLineEdit(frame, text="Akihiko", font=QFont("p5hatty", 24))
        self.akihikoEdit.setGeometry(6, lineEdit_height * 2.4, 300, 37)
        
        self.mitsuruEdit = QLineEdit(frame, text="Mitsuru", font=QFont("p5hatty", 24))
        self.mitsuruEdit.setGeometry(6, lineEdit_height * 3.1, 300, 37)
        
        self.aigisEdit = QLineEdit(frame, text="Aigis", font=QFont("p5hatty", 24))
        self.aigisEdit.setGeometry(6, lineEdit_height * 3.8, 300, 37)
        
        self.koromaruEdit = QLineEdit(frame, text="Koromaru", font=QFont("p5hatty", 24))
        self.koromaruEdit.setGeometry(6, lineEdit_height * 4.5, 300, 37)
        
        self.kenEdit = QLineEdit(frame, text="Ken", font=QFont("p5hatty", 24))
        self.kenEdit.setGeometry(6, lineEdit_height * 5.2, 300, 37)
        
        self.shinjiEdit = QLineEdit(frame, text="Shinji", font=QFont("p5hatty", 24))
        self.shinjiEdit.setGeometry(6, lineEdit_height * 5.9, 300, 37)
        
        self.metisEdit = QLineEdit(frame, text="Metis", font=QFont("p5hatty", 24))
        self.metisEdit.setGeometry(6, lineEdit_height * 6.6, 300, 37)
        self.metisEdit.hide()
        
    def calendarWidget(self):
        self.calFrame = QFrame(self.mainPageWidget)
        self.calFrame.setMinimumSize(420, 405)
        self.calFrame.setGeometry(320, 0, 0, 0)
        self.calFrame.setFont(QFont("p5hatty", 24))
        
        self.calFrame.setStyleSheet("QFrame {background-color: transparent}\
            QLineEdit {background-color: #D4E6F1; border: 2px solid #1A5276; border-radius: 5px;}\
                QLabel {background-color: #D4E6F1; border: 2px solid #2980B9; border-radius: 5px; padding-top: 10}\
                    QLineEdit:hover {color: black; border: 2px solid #2471A3; background-color: #EAF2F8; padding-top: 3}")
        self.calFrame.adjustSize()
        
        calTitle = QLabel(self.calFrame, text="Set Calendar Date", font=QFont("p5hatty", 24))

        calTitle.setGeometry(5, 5, 410, 45)
        calTitle.setAlignment(Qt.AlignCenter)
        
        self.daysEdit = QLineEdit(self.calFrame, text="Days", font=QFont("p5hatty", 24))
        self.daysEdit.setGeometry(6, 55, 410, 37)
        
        self.monthsEdit = QLineEdit(self.calFrame, text="Months", font=QFont("p5hatty", 24))
        self.monthsEdit.setGeometry(6, 55 * 1.7, 410, 37)
    
    def selectionEvent(self):
        if self.selectionBox.currentIndex() == 0:
            self.metisEdit.hide()
            self.calFrame.show()
            self.game_flag = 0
            
            self.flagChecker()
            
        elif self.selectionBox.currentIndex() == 1:
            self.metisEdit.show()
            self.game_flag = 1
            self.calFrame.hide()
            
            self.flagChecker()
        
    def flagChecker(self):
        if self.game_flag == 1:
            print("The Answer, selected.")
            QMessageBox.information(self, "Game Selection", "You selected The Answer.")
        else:
            print("The Journey, selected.")
            QMessageBox.information(self, "Game Selection", "You selected The Journey.")
        print(self.game_flag)
        
    def pnachBtn(self):
        pnachBtn = QPushButton(self, text="Create .PNACH", font=QFont("p5hatty", 24), clicked=self.valueChecker)
        pnachBtn.setGeometry(5, 555, 790, 40)
        pnachBtn.setStyleSheet("QPushButton {background-color: #D4E6F1; border: 2px solid #1A5276; border-radius: 5px; padding-top: 4}\
            QPushButton:hover:!pressed {color: black; border: 2px solid #2471A3; background-color: #EAF2F8; padding-top: 3}")

    def valueChecker(self):
        if self.game_flag == 0:
            self.getCalendar()
            self.journeyCreator()
            self.showInformationBox()
        
    def getCalendar(self):
        self.dateFlag = 0
        month = int(self.monthsEdit.text())
        day = int(self.daysEdit.text())
        
        if month > 10 or month == 1 or month == 10 and day > 4:
            akihiko = akihikoEv
            ken = kenEv
        if month > 11 or month == 1 or month == 11 and day > 7:
            yukari = yukariEv
        if month > 11 or month == 1 or month == 11 and day > 17:
            mitsuru = mitsuruEv
        if month > 11 or month == 1 or month == 11 and day > 22:
            junpei = junpeiEv
        if month > 12 or month == 1 or month == 12 and day > 29:
            aigis = aigisEv
        
        if month in [0, 2, 3] or month > 12:
            self.dateFlag = 1
            QMessageBox.information(self, "Unevolved Party Members", "It seems you entered an invalid date, thus assuming that your members is unevolved.")
        elif day == 0 or day > 31:
            self.dateFlag = 1
            QMessageBox.information(self, "Unevolved Party Members", "It seems you entered an invalid date, thus assuming that your members is unevolved.")     
    
    def journeyCreator(self):
        print(" - Journey Creator - ")
        yukariLvl = int(self.yukariEdit.text())
        junpeiLvl = int(self.junpeiEdit.text())
        akihikoLvl = int(self.akihikoEdit.text())
        mitsuruLvl = int(self.mitsuruEdit.text())
        aigisLvl = int(self.aigisEdit.text())
        koroLvl = int(self.koromaruEdit.text())
        kenLvll = int(self.kenEdit.text())
        shinjiLvl = int(self.shinjiEdit.text())
        
        for (minLv, maxLv, skill) in yukari:    
            if minLv <= yukariLvl < maxLv:
                yukSkills.append(skill)
        print(f"Yukari - {yukSkills}")

        for (minLv, maxLv, skill) in junpei:
            if minLv <= junpeiLvl < maxLv:
                junSkills.append(skill)
        print(f"Junpei - {junSkills}")

        for (minLv, maxLv, skill) in akihiko:
            if minLv <= akihikoLvl < maxLv:
                akiSkills.append(skill)
        print(f"Akihiko - {akiSkills}")

        for (minLv, maxLv, skill) in mitsuru:
            if minLv <= mitsuruLvl < maxLv:
                mitSkills.append(skill)
        print(f"Mitsuru - {mitSkills}")

        for (minLv, maxLv, skill) in aigis:
            if minLv <= aigisLvl < maxLv:
                aigSkills.append(skill)
        print(f"Aigis - {aigSkills}")

        for (minLv, maxLv, skill) in koromaru:
            if minLv <= koroLvl < maxLv:
                koroSkills.append(skill)
        print(f"Koromaru - {koroSkills}")

        for (minLv, maxLv, skill) in ken:
            if minLv <= kenLvll < maxLv:
                kenSkills.append(skill)
        print(f"Ken - {kenSkills}")

        for (minLv, maxLv, skill) in shinjiro:
            if minLv <= shinjiLvl < maxLv:
                shinSkills.append(skill)
        print(f"Shinji - {shinSkills}")


        # CREATE A PNACH FILE!
        with open("94A82AAA.pnach", "w") as pnach_file:
            pnach_file.write("//Persona 3 FES Party Skills Modifier, The Journey")
        
        # pnach files CODE print
        with open("94A82AAA.pnach", "a") as pnach:
            # Yukari
            count = 0
            while count < len(yukSkills):
                if count == 0:
                    pnach.write(f"\n\n//Yukari Skills (Level {yukariLvl})")
                pnach.write(f"\n//Persona Skill {(str(count + 1))}\npatch=1,EE,00"
                            f"{format(8601848 + (count * 2), 'x').upper()},short,0{yukSkills[count]}")
                count += 1
            # fills in the remaining skill slots with blank entries to overwrite potential duplicates/ unwanted skills
            if count != 0:
                while count < 8:
                    pnach.write(f"\n//Persona Skill {(str(count + 1))}\npatch=1,EE,00"
                                f"{format(8601848 + (count * 2), 'x').upper()},short,0000")
                    count += 1

            # Takes in Stats data and outputs level cheat codes
            if yukariLvl != 0:
                Strength = 0
                Magic = 0
                Endurance = 0
                Agility = 0
                Luck = 0
                for(Level, Str, Mag, End, Agi, Luc) in yukari_Stats:
                    if yukariLvl >= Level:
                        Strength += Str
                        Magic += Mag
                        Endurance += End
                        Agility += Agi
                        Luck += Luc

                pnach.write(f"\n\n//Yukari Stats\n//Strength: {str(Strength)}\t\tMagic: {str(Magic)}\t\tEndurance: "
                            f"{str(Endurance)}\t\tAgility: {str(Agility)}\t\tLuck: {str(Luck)}\npatch=1,EE,20834108,"
                            f"extended,{format(Agility, 'x').upper()}{format(Endurance, 'x').upper()}"
                            f"{format(Magic, 'x').upper()}{format(Strength, 'x').upper()}\npatch=1,EE,0083410C,"
                            f"extended,000000{format(Luck, 'x').upper()}")
            # Junpei
            count = 0
            while count < len(junSkills):
                if count == 0:
                    pnach.write(f"\n\n//Junpei skills (Level {junpeiLvl})")
                pnach.write(f"\n//Persona Skill {str(count + 1)}\npatch=1,EE,00"
                            f"{format(8604452 + (count * 2), 'x').upper()},short,0{junSkills[count]}")
                count += 1
            if count != 0:
                while count < 8:
                    pnach.write(f"\n//Persona Skill {str(count + 1)}\npatch=1,EE,00"
                                f"{format(8604452 + (count * 2), 'x').upper()},short,0000")
                    count += 1

            if junpeiLvl != 0:
                Strength = 0
                Magic = 0
                Endurance = 0
                Agility = 0
                Luck = 0
                for (Level, Str, Mag, End, Agi, Luc) in junpei_Stats:
                    if Level <= junpeiLvl:
                        Strength += Str
                        Magic += Mag
                        Endurance += End
                        Agility += Agi
                        Luck += Luc

                pnach.write(f"\n\n//Junpei Stats\n//Strength: {str(Strength)}\t\tMagic: {str(Magic)}\t\tEndurance: "
                            f"{str(Endurance)}\t\tAgility: {str(Agility)}\t\tLuck: {str(Luck)}\npatch=1,EE,20834B34,"
                            f"extended,{format(Agility, 'x').upper()}{format(Endurance, 'x').upper()}"
                            f"{format(Magic, 'x').upper()}{format(Strength, 'x').upper()}\npatch=1,EE,00834B38,"
                            f"extended,000000{format(Luck, 'x').upper()}")

            # Akihiko
            count = 0
            while count < len(akiSkills):
                if count == 0:
                    pnach.write("\n\n//Akihiko skills")
                pnach.write(f"\n//Persona Skill {str(count + 1)} \npatch=1,EE,00"
                            f"{format(8606188 + (count * 2), 'x').upper()},short,0{akiSkills[count]}")
                count += 1
            if count != 0:
                while count < 8:
                    pnach.write(f"\n//Persona Skill {str(count + 1)}\npatch=1,EE,00"
                                f"{format(8606188 + (count * 2), 'x').upper()},short,0000")
                    count += 1

            if akihikoLvl != 0:
                Strength = 0
                Magic = 0
                Endurance = 0
                Agility = 0
                Luck = 0
                for (Level, Str, Mag, End, Agi, Luc) in akihiko_Stats:
                    if Level <= akihikoLvl:
                        Strength += Str
                        Magic += Mag
                        Endurance += End
                        Agility += Agi
                        Luck += Luc

                pnach.write(f"\n\n//Akihiko Stats\n//Strength: {str(Strength)}\t\tMagic: {str(Magic)}\t\tEndurance: "
                            f"{str(Endurance)}\t\tAgility: {str(Agility)}\t\tLuck: {str(Luck)}\npatch=1,EE,208351FC,"
                            f"extended,{format(Agility, 'x').upper()}{format(Endurance, 'x').upper()}"
                            f"{format(Magic, 'x').upper()}{format(Strength, 'x').upper()}\npatch=1,EE,00835200,"
                            f"extended,000000{format(Luck, 'x').upper()}")

            # Mitsuru
            count = 0
            while count < len(mitSkills):
                if count == 0:
                    pnach.write("\n\n//Mitsuru skills")
                pnach.write(f"\n//Persona Skill {str(count + 1)}\npatch=1,EE,00"
                            f"{format(8603584 + (count * 2), 'x').upper()},short,0{mitSkills[count]}")
                count += 1
            if count != 0:
                while count < 8:
                    pnach.write(f"\n//Persona Skill {str(count + 1)}\npatch=1,EE,00"
                                f"{format(8603584 + (count * 2), 'x').upper()},short,0000")
                    count += 1

            if mitsuruLvl != 0:
                Strength = 0
                Magic = 0
                Endurance = 0
                Agility = 0
                Luck = 0
                for (Level, Str, Mag, End, Agi, Luc) in mitsuru_Stats:
                    if Level <= mitsuruLvl:
                        Strength += Str
                        Magic += Mag
                        Endurance += End
                        Agility += Agi
                        Luck += Luc

                pnach.write(f"\n\n//Mitsuru Stats\n//Strength: {str(Strength)}\t\tMagic: {str(Magic)}\t\tEndurance: "
                            f"{str(Endurance)}\t\tAgility: {str(Agility)}\t\tLuck: {str(Luck)}\npatch=1,EE,208347D0,"
                            f"extended,{format(Agility, 'x').upper()}{format(Endurance, 'x').upper()}"
                            f"{format(Magic, 'x').upper()}{format(Strength, 'x').upper()}\npatch=1,EE,008347D4,"
                            f"extended,000000{format(Luck, 'x').upper()}")

            # Aigis
                count = 0
                while count < len(aigSkills):
                    if count == 0:
                        pnach.write("\n\n//Aigis skills")
                    pnach.write(f"\n//Persona Skill {str(count + 1)}\npatch=1,EE,00"
                                f"{format(8602716 + (count * 2), 'x').upper()},short,0{aigSkills[count]}")
                    count += 1
                if count != 0:
                    while count < 8:
                        pnach.write(f"\n//Persona Skill {str(count + 1)}\npatch=1,EE,00"
                                    f"{format(8602716 + (count * 2), 'x').upper()},short,0000")
                        count += 1

                if aigisLvl != 0:
                    Strength = 0
                    Magic = 0
                    Endurance = 0
                    Agility = 0
                    Luck = 0
                    for (Level, Str, Mag, End, Agi, Luc) in aigis_Stats:
                        if Level <= aigisLvl:
                            Strength += Str
                            Magic += Mag
                            Endurance += End
                            Agility += Agi
                            Luck += Luc

                    pnach.write(f"\n\n//Aigis Stats\n//Strength: {str(Strength)}\t\tMagic: {str(Magic)}\t\tEndurance: "
                                f"{str(Endurance)}\t\tAgility: {str(Agility)}\t\tLuck: {str(Luck)}\npatch=1,EE,2083446C,"
                                f"extended,{format(Agility, 'x').upper()}{format(Endurance, 'x').upper()}"
                                f"{format(Magic, 'x').upper()}{format(Strength, 'x').upper()}\npatch=1,EE,00834470,"
                                f"extended,000000{format(Luck, 'x').upper()}")

            # Koromaru
            count = 0
            while count < len(koroSkills):
                if count == 0:
                    pnach.write("\n\n//Koromaru skills")
                pnach.write(f"\n//Persona Skill {str(count + 1)}\npatch=1,EE,00"
                            f"{format(8608792 + (count * 2), 'x').upper()},short,0{koroSkills[count]}")
                count += 1
            if count != 0:
                while count < 8:
                    pnach.write(f"\n//Persona Skill {str(count + 1)}\npatch=1,EE,00"
                                f"{format(8608792 + (count * 2), 'x').upper()},short,0000")
                    count += 1

            if koroLvl != 0:
                Strength = 0
                Magic = 0
                Endurance = 0
                Agility = 0
                Luck = 0
                for (Level, Str, Mag, End, Agi, Luc) in koromaru_Stats:
                    if Level <= koroLvl:
                        Strength += Str
                        Magic += Mag
                        Endurance += End
                        Agility += Agi
                        Luck += Luc

                pnach.write(f"\n//Koromaru Stats\n//Strength: {str(Strength)}\t\tMagic: {str(Magic)}\t\tEndurance: "
                            f"{str(Endurance)}\t\tAgility: {str(Agility)}\t\tLuck: {str(Luck)}\npatch=1,EE,20835C28,"
                            f"extended,{format(Agility, 'x').upper()}{format(Endurance, 'x').upper()}"
                            f"{format(Magic, 'x').upper()}{format(Strength, 'x').upper()}\npatch=1,EE,008345C2C,"
                            f"extended,000000{format(Luck, 'x').upper()}")

            # Ken
            count = 0
            while count < len(kenSkills):
                if count == 0:
                    pnach.write("\n\n//Ken skills")
                pnach.write(f"\n//Persona Skill {str(count + 1)}\npatch=1,EE,00"
                            f"{format(8607056 + (count * 2), 'x').upper()},short,0{kenSkills[count]}")
                count += 1
            if count != 0:
                while count < 8:
                    pnach.write(f"\n//Persona Skill {str(count + 1)}\npatch=1,EE,00"
                                f"{format(8607056 + (count * 2), 'x').upper()},short,0000")
                    count += 1

            if kenLvll != 0:
                Strength = 0
                Magic = 0
                Endurance = 0
                Agility = 0
                Luck = 0
                for (Level, Str, Mag, End, Agi, Luc) in ken_Stats:
                    if Level <= kenLvll:
                        Strength += Str
                        Magic += Mag
                        Endurance += End
                        Agility += Agi
                        Luck += Luc

                pnach.write(f"\n\n//Ken Stats\n//Strength: {str(Strength)}\t\tMagic: {str(Magic)}\t\tEndurance: "
                            f"{str(Endurance)}\t\tAgility: {str(Agility)}\t\tLuck: {str(Luck)}\npatch=1,EE,20835560,"
                            f"extended,{format(Agility, 'x').upper()}{format(Endurance, 'x').upper()}"
                            f"{format(Magic, 'x').upper()}{format(Strength, 'x').upper()}\npatch=1,EE,008345564,"
                            f"extended,000000{format(Luck, 'x').upper()}")
            
            # Shinjiro
            count = 0
            while count < len(shinSkills):
                if count == 0:
                    pnach.write("\n\n//Shinjiro skills")
                pnach.write(f"\n//Persona Skill {str(count + 1)}\npatch=1,EE,00"
                            f"{format(8607924 + (count * 2), 'x').upper()},short,0{shinSkills[count]}")
                count += 1
            if count != 0:
                while count < 8:
                    pnach.write(f"\n//Persona Skill {str(count + 1)}\npatch=1,EE,00"
                                    f"{format(8607924 + (count * 2), 'x').upper()},short,0000")
                    count += 1

            if shinjiLvl != 0:
                Strength = 0
                Magic = 0
                Endurance = 0
                Agility = 0
                Luck = 0
                for (Level, Str, Mag, End, Agi, Luc) in shinjiro_Stats:
                    if Level <= shinjiLvl:
                            Strength += Str
                            Magic += Mag
                            Endurance += End
                            Agility += Agi
                            Luck += Luc

                pnach.write(f"\n\n//Shinjiro Stats\n//Strength: {str(Strength)}\t\tMagic: {str(Magic)}\t\tEndurance: "
                            f"{str(Endurance)}\t\tAgility: {str(Agility)}\t\tLuck: {str(Luck)}\npatch=1,EE,208358C4,"
                            f"extended,{format(Agility, 'x').upper()}{format(Endurance, 'x').upper()}"
                            f"{format(Magic, 'x').upper()}{format(Strength, 'x').upper()}\npatch=1,EE,0083458C8,"
                            f"extended,000000{format(Luck, 'x').upper()}")
    
    def showInformationBox(self):
        if self.dateFlag == 1:
            QMessageBox.information(self, "Code created!", f"\tYukari : {self.yukariEdit.text()}\n\
        Junpei : {self.junpeiEdit.text()}\n\
        Akihiko : {self.akihikoEdit.text()}\n\
        Mitsuru : {self.mitsuruEdit.text()}\n\
        Aigis : {self.aigisEdit.text()}\n\
        Koromaru : {self.koromaruEdit.text()}\n\
        Ken : {self.kenEdit.text()}\n\
        Shinji : {self.shinjiEdit.text()}\n")
        else:
            QMessageBox.information(self, "Code created!", f"\tYukari : {self.yukariEdit.text()}\n\
        Junpei : {self.junpeiEdit.text()}\n\
        Akihiko : {self.akihikoEdit.text()}\n\
        Mitsuru : {self.mitsuruEdit.text()}\n\
        Aigis : {self.aigisEdit.text()}\n\
        Koromaru : {self.koromaruEdit.text()}\n\
        Ken : {self.kenEdit.text()}\n\
        Shinji : {self.shinjiEdit.text()}\n\n\
        Date entered : {self.monthsEdit.text()}/{self.daysEdit.text()}")

        
def runApp():
    app = QApplication(sys.argv)
    win = P3SkillEditor()
    win.show()
    app.exec()
    

if __name__ == "__main__":
    try:
        runApp()
    except:
        print(f"Error : {sys.exc_info()[1]}")