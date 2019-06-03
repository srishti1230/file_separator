import os, shutil
dict_extension={
"image_extension":('.jpeg','.png','.JPG'),
"audio_extension" :('.mp3','.mda','.wav','.flac'),
"video_extension" :('.mp4','.mkv','.MKV',',flv','.mpeg'),
"document_extension" :('.doc','.pdf','.txt')
}

folderpath= input("enter the folder path:")

def  file_finder(folder_path, file_extensions):
    files=[]
    for file in os.listdir(folder_path):
        for extension in file_extensions:
            if file.endswith(extension):
                files.append(file)
    return files
    # return[file for file in os.listdir(folder_path) for extension in file_extensions if file.endswith(extension)]

# file_finder(folderpath,document_extension)
for extension_type,extension_tuple in dict_extension.items():
    # print("calling file finder")
    # print(file_finder(folderpath,extension_tuple))
    folder_name=extension_type.split('_')[0] + 'files'
    folder_path=os.path.join(folderpath,folder_name)
    os.mkdir(folder_path)
    for item in file_finder(folderpath,extension_tuple):
        item_path=os.path.join(folderpath,item)
        item_new_path=os.path.join(folder_path,item)
        shutil.move(item_path,folder_path)
