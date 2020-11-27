from file_analyzer.folder_analyzer import FolderAnalyzer

INSPECTED_DIR = r"D:\OrlAnn\DQE_MentorProgram\Module_4_Python\Input"
DESTINATION_DIR = r"D:\OrlAnn\DQE_MentorProgram\Module_4_Python\Incorrect_input"
FILE_TYPE = "fb2"


def main():
    analyzer = FolderAnalyzer(INSPECTED_DIR, FILE_TYPE)
    analyzer.move_excess_files(DESTINATION_DIR)


if __name__ == "__main__":
    main()
