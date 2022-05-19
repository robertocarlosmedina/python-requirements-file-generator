import os

# Getting a list off al the packages
os.system("mkdir .modules")
os.system("pip list >> .modules/modules.txt")

file_reader = open(".modules/modules.txt", "r")
file_writer = open("requirements.txt", "w")

# List of packages to make the requirements file
packages = [
    "textblob","torch","torchtext","nltk","jiwer",
    "flask-restful","flask" ,"flask-cors","pygame","spacy"
]

lines = file_reader.readlines()

os.system("rm .modules/packages.txt")
os.system("rm -r .modules")

for package in packages:
    for line in lines:
        line = line.split(" ")
        name, verssion = line[0].strip(), line[-1].strip()
        if(package == name.lower()):
            print(f"pip install {name}=={verssion}")
            file_writer.write(f"pip install {name}=={verssion}\n")
