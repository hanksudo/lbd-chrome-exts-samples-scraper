import os
import zipfile

ZIP_PATH = "zips"
PROJECTS_PATH = "projects"


def main():
    if not os.path.exists(PROJECTS_PATH):
        os.mkdir(PROJECTS_PATH)

    for dirname, dirnames, filenames in os.walk(ZIP_PATH):
        for filename in filenames:
            zip_file_path = os.path.join(dirname, filename)
            if zipfile.is_zipfile(zip_file_path):
                zipfile.ZipFile(zip_file_path).extractall(PROJECTS_PATH)

if __name__ == "__main__":
    main()
