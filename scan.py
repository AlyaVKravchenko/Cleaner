import sys
from pathlib import Path

images = []
documents = []
audio = []
video = []
archives = []
others = list()
unknown = set()
extensions = set()
folders = list()

registered_extensions = {
    "JPEG": images,
    "PNG": images,
    "JPG": images,
    "SVG": images,
    'AVI':  video,
    'MP4': video,
    'MOV': video,
    'MKV': video,
    'DOC': documents,
    'PDF': documents, 
    'XLSX': documents, 
    'PPTX': documents,
    "TXT": documents,
    "DOCX": documents,
    'MP3': audio, 
    'OGG': audio, 
    'WAV': audio, 
    'AMR': audio,
    "ZIP": archives,
    'GZ': archives, 
    'TAR': archives
}


def get_extensions(file_name):
    return Path(file_name).suffix[1:].upper()

def scan(folder):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ("DOCUMENTS", "AUDIO", "VIDEO", "ARCHIVE", "IMAGES", "OTHER"):
                folders.append(item)
                scan(item)
            continue

        extension = get_extensions(file_name=item.name)
        new_name = folder/item.name
        if not extension:
            others.append(new_name)
        else:
            try:
                container = registered_extensions[extension]
                extensions.add(extension)
                container.append(new_name)
            except KeyError:
                unknown.add(extension)
                others.append(new_name)

if __name__ == '__main__':
    path = sys.argv[1]
    print(f"Start in {path}")

    arg = Path(path)
    scan(arg)


    
    print(f"images: {images}\n")
    print(f"documents: {documents}\n")
    print(f"audio: {audio}\n")
    print(f"video: {video}\n")

    print(f"archive: {archives}\n")
    print(f"unknown: {others}\n")
    print(f"All extensions: {extensions}\n")
    print(f"Unknown extensions: {unknown}\n")

    
