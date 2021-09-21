"""
    project organise hard exmple folder downloads
    by create folder to store files img [png,jpg,ipeg,gif]
    and create folder to store files (zip)
    and create folder to store files (pdf)
    and create folder to store files (exe)
    etc ...
"""
import os
import module_organise as org

os.chdir(r"C:\Users\useer\Downloads") # it use to change directory in this path to downloads path
arr=os.listdir(os.getcwd()) # it use to get name of files in list
domains=[] # to store jpg|png etc... in this list
files=[] # to store files by name and domain

for i in arr:
    if len(i.split('.')) > 1: # split file into array to name and domain
        domains.append(i.split('.')[1]) # to add domain files such as jpg|mp4
        files.append(i.split('.'))  # to add files in list such as ['ahmed','jpg']

domains=list(set(domains))

# orgaanise files img
img=org.Organise(arr,domains,files)

# create folders to move files in it
img.create_folders()

# organise files img
img.organise_files(['jpg','png','gif','jpeg'],'imgs')

# organise files video
img.organise_files(['mp4','webm'],'videos')

# organise files exe
img.organise_files(['exe'],'program_file')

# organise files rar
img.organise_files(['zip','rar','tar'],'zip_fil')

# organise files codes
img.organise_files(['html','htm','py','js','css','cpp','c','bash'],'codes')

# organise files ddl , ini
img.organise_files(['dll'],'files_program')

# organise files txt etc..
img.organise_files(['txt','xlsx'],'writing')