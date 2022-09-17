import os
import shutil
from zipfile import ZipFile
import zipfile



def create_archive():
    archive = zipfile.ZipFile(os.path.abspath('archive.zip'), 'w')
    archive.write('./resources/Grades.xlsx')
    archive.write('./resources/Employees.csv')
    archive.write('./resources/ISTQB.pdf')
    archive.close()

def move_archive():
    source = os.path.abspath('archive.zip')
    move_to = os.path.abspath('./resources')
    shutil.move(source, move_to)