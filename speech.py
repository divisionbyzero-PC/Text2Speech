# by ['Percival']
#
# me.dividesbyzero@gmail.com

from gtts import gTTS
from playsound import playsound
from PyQt5 import QtWidgets, QtGui, uic
from PyQt5.QtWidgets import QFileDialog
import sys, os
from random import randint

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()        
        uic.loadUi('window.ui', self) 
        self.show()                        
        self.setWindowIcon(QtGui.QIcon('monkey.png'))        
        
        self.eng1.clicked.connect(self.english)
        self.sp1.clicked.connect(self.spanish) 
        self.pt1.clicked.connect(self.portuguese) 
        self.it1.clicked.connect(self.italian) 
        self.fr1.clicked.connect(self.french)

        self.save.clicked.connect(self.save_mp3)

        global randfile        

        r1 = randint(1,10000000)
        r2 = randint(1,10000000)

        randfile = str(r2)+"randomtext"+str(r1) +".mp3"

    
    def english(self):
        language = 'en'
        mytext = str(self.input.toPlainText()).strip()
        global myobj
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save(randfile)
        playsound(randfile)
        os.remove(randfile)       
        return myobj

    def spanish(self):
        language = 'es'
        mytext = str(self.input.toPlainText()).strip()
        global myobj
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save(randfile)
        playsound(randfile)
        os.remove(randfile)       
        return myobj
        
    def portuguese(self):
        language = 'pt'
        mytext = str(self.input.toPlainText()).strip()
        global myobj
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save(randfile)
        playsound(randfile)
        os.remove(randfile)       
        return myobj              

    def italian(self):
        language = 'it'
        mytext = str(self.input.toPlainText()).strip()
        global myobj
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save(randfile)
        playsound(randfile)
        os.remove(randfile)       
        return myobj

    def french(self):
        language = 'fr'
        mytext = str(self.input.toPlainText()).strip()
        global myobj
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save(randfile)
        playsound(randfile)
        os.remove(randfile)       
        return myobj        

    def save_mp3(self):
        file = str(QFileDialog.getExistingDirectory(self, "Choose where to save log"))
        myobj.save(f'{file}/speech.mp3')

        

app = QtWidgets.QApplication(sys.argv)     
window = Ui()                              
app.exec_()                                
