import os
class Organise:
    def __init__(self,arr,domains,files):
        self.arr=arr
        self.domains=domains
        self.files=files
    def create_folders(self):
        if 'imgs' not in self.arr:
            # create folder img to store ['jpg', 'png', 'gif', 'jpeg']
            os.system("mkdir imgs")

        if 'videos' not in self.arr:
            # create folder videos to store videos
            os.system(f'mkdir videos')

        if 'pdf_files' not in self.arr:
            # create folder pdf_files to store pdf files
            os.system('mkdir pdf_files')

        if 'codes' not in self.arr:
            # create folder codes to store code files
            os.system('mkdir codes')

        if 'program_file' not in self.arr:
            # create folder program_file to store exe files
            os.system('mkdir program_file')

        if 'zip_fil' not in self.arr:
            # create folder zip_file to store rar or zip files
            os.system('mkdir zip_fil')

        if 'files_program' not in self.arr:
            # create folder files_program to store files of program like dll ,dil , ini
            os.system('mkdir files_program')

        if 'writing' not in self.arr:
            # create folder wiriter
            os.system('mkdir writing')

    def organise_files(self,kind,place):
        for i in self.files:
            if i[1] in kind:
                os.system(f'move "{i[0] + "." + i[1]}" {place}')
        print(f'move to {place} Done....')