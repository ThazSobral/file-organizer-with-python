import os
import shutil
from datetime import datetime

class Organizer:
    extensions = ['jpg', 'jpeg', 'JPG', 'JPEG', 'png', 'PNG', 'pdf', 'mp4']

    def folder_path_from_photo_date(self, file):
        date = self.photo_shooting_date(file)
        return date.strftime('%Y') + '/' + date.strftime('%Y-%m-%d')

    def photo_shooting_date(self, file):
        date = datetime.fromtimestamp(os.path.getmtime(file))
        return date

    def move_photo(self, file):
        new_folder = self.folder_path_from_photo_date(file)
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)
        shutil.move(file, new_folder + '/' + file)

    def organize(self):
        photos = [
            filename for filename in os.listdir('.') if any(filename.endswith(ext) for ext in self.extensions)
        ]
        for filename in photos:
            self.move_photo(filename)

PO = Organizer()
PO.organize()
