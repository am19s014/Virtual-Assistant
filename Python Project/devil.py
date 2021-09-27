# from _typeshed import Self
from sys import _current_frames
import sys
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import pyaudio
import time
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from devilGui import Ui_MainWindow

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    elif hour >= 18 and hour < 8:
        speak("Good Evening!")

    else:
        speak("Good Night")

    speak("I am Devil. Please tell me how may I help you")



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sdfkfbjbckjz@gmail.com', 'password')
    server.sendmail('vdnknlkssnn19@gmail.com', to, content)
    server.close()



class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    
    def run (self):
        self.taskExecution()

    
    def takeCommand(self):
    # It takes microphone input from the user and returns string output
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            r.energy_threshold = 100  # minimum audio energy to consider for recording
            r.dynamic_energy_threshold = True
            r.dynamic_energy_adjustment_damping = 0.15
            r.dynamic_energy_ratio = 1.5
            r.pause_threshold = 0.8  # seconds of non-speaking audio before a phrase is considered complete
            r.operation_timeout = 3  # seconds after an internal operation (e.g., an API request) starts before it times out, or ``None`` for no timeout

            r.phrase_threshold = 0.3  # minimum seconds of speaking audio before we consider the speaking audio a phrase - values below this are ignored (for filtering out clicks and pops)
            r.non_speaking_duration = 0.5  # seconds of non-speaking audio to keep on both sides of the recording

            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)
            print("Say that again please...")
            return "None"
        return query

    def taskExecution(self):
        wishMe()
    # speak("What should I say?")
    # content = input()
    # to = "nevilsakhreliya2580@gmail.com"
    # sendEmail(to, content)
    # speak("Email has been sent!")
        while True:
            # if 1:
            self.query = self.takeCommand().lower()

            # Logic for executing tasks based on query
            if 'wikipedia' in self.query:
                speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in self.query:
                webbrowser.open("youtube.com")

            elif 'open google' in self.query or 'google' in self.query:
                webbrowser.open("google.com")

            elif 'open stackoverflow' in self.query:
                webbrowser.open("stackoverflow.com")


            elif 'play music' in self.query:
                music_dir = 'N:\\New folder (2)'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[7]))

            elif 'time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif 'open code' in self.query:
                codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
            elif 'email to me' in self.query:
                try:
                    speak("What should I say?")
                    content = self.takeCommand()
                    to = "dfklffk@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry Bro But, I am not able to send this email")
            else:
                print("There is something wrong with system ,Try Again Later!")


startExecution = MainThread()
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        # self.ui.pushButton_2.clicked.connect(self.close())
    
    def startTask(self):
        self.ui.movie = QtGui.QMovie("pics/jarvisImage.jpg")
        self.ui.label.setmovie(self.ui.movie)
        self.ui.movie.start()

        # self.ui.movie = QtGui.QMovie("pics/jarvisImage.jpg")
        # self.ui.label_2.setmovie(self.ui.movie)
        # self.ui.movie.start()
    #     timer = QTimer(self)
    #     timer.timeout.connect(self.showtime)
    #     timer.start(1000)
    #     startExecution.start()
    
    # def showtime(self):
    #     current_time = QTime.currentTime()
    #     current_date = QDate.currentDate()
    #     label_time = current_time.toString('hh:mm:ss')
    #     label_date = current_date.toString(Qt.ISODate)
    #     self.ui.textBrowser.setText(label_date)
    #     self.ui.textBrowser_2.setText(label_time)

        
app = QApplication(sys.argv)
devilobj = Main()                      # class object 
devilobj.show()                    # class object
exit(app.exec_())

# import sys

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     ex = Ui_MainWindow()
#     w = QtWidgets.QMainWindow()
#     ex.setupUi(w)
#     w.show()
#     sys.exit(app.exec_())