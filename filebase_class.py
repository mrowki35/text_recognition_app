import os

class FilesBase():
    list_of_files=[]
    def check_image_format(self,filepath):
        filename = os.path.basename(filepath)
        extension = os.path.splitext(filename)[1].lower()
        if extension == ".png":
            return True
        elif extension == ".jpeg" or extension == ".jpg":
            return True
        else:
            return False
