import os
import shutil
from datetime import datetime

class Organizer:
    def organize(self, extensions):
        files = [
            filename for filename in os.listdir('.') if any(filename.endswith(ext) for ext in extensions)
        ]
        for filename in files:
            self.move_file(filename)
    
    def move_file(self, file):
        new_folder = self.folder_path_from_file_date(file)
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)
        shutil.move(file, new_folder + '/' + file)

    def folder_path_from_file_date(self, file):
        date = self.file_shooting_date(file)
        return date.strftime('%Y') + '/' + date.strftime('%Y-%m-%d')

    def file_shooting_date(self, file):
        date = datetime.fromtimestamp(os.path.getmtime(file))
        return date

class Manager:
    extensions = []
    def __init__(self):
        self.intro()
        self.extensions = self.extension_to_be_sought()

    def intro(self):
        print('\
        ooooo  ooooo  ooooo  ooooo  o    o  o  ooooo  ooooo  ooooo\n\
        o   o  o   o  o      o   o  o o  o  o     o   o      o   o\n\
        o   o  ooooo  o ooo  o   o  o  o o  o    o    ooooo  ooooo\n\
        o   o  o  o   o   o  ooooo  o   oo  o   o     o      o  o \n\
        ooooo  o   o  ooooo  o   o  o    o  o  ooooo  ooooo  o   o\n\
        \nOrganize seus arquivos do seu jeito.\n\
        ')

    def extension_to_be_sought(self):
        extensions = input('Com quais extensões deseja trabalhar? \n(ex: jpg, pdf, ...)\n')
        return extensions.replace(" ", "").split(',')

config = Manager()
organizer = Organizer()
organizer.organize(config.extensions)