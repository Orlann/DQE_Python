import logging
import logging.config
from os import listdir, remove
from os.path import isfile, join
import glob
import shutil


class FolderAnalyzer:

    def __init__(self, folder, file_type):
        self.folder = folder
        self.file_type = file_type
        logging.config.fileConfig(fname='logging.conf', disable_existing_loggers=False)
        self.logger = logging.getLogger("Folder_analyzer")

    def file_browser(self):
        files = [f for f in glob.glob(f"{self.folder}/*.{self.file_type}")]
        self.logger.info("Find all files in folder")
        return files

    def full_file_name(self):
        folder_content = listdir(self.folder)
        folder_content_full_path = [join(self.folder, f) for f in folder_content]
        self.logger.info(fr"Find full path to files in folder: {folder_content_full_path}")
        return folder_content_full_path

    def move_excess_files(self, target_folder):
        all_files_full_names = self.full_file_name()
        necessary_files = self.file_browser()
        excess_objects = [f for f in all_files_full_names if f not in necessary_files]
        self.logger.info("Moving all excess file to another folder")
        for f in excess_objects:
            try:
                shutil.move(f, target_folder)
            except OSError:
                remove(f)
