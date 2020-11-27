from file_analyzer.file_parser import FileParser
import logging
import logging.config

from file_analyzer.folder_analyzer import FolderAnalyzer
from file_analyzer.sql_worker import SQLWorker

FOLDER_PATH = r"D:\OrlAnn\DQE_MentorProgram\Module_4_Python\Input"
TARGET_FOLDER_PATH = r"D:\OrlAnn\DQE_MentorProgram\Module_4_Python\Incorrect_input"
INPUT_FILE_PATH = r"D:\OrlAnn\DQE_MentorProgram\Module_4_Python\Input\Example_1.fb2"
DATABASE_PATH = r"D:\OrlAnn\DQE_MentorProgram\Module_4_Python\dqe_database.db"


def main():
    # Logging declaring
    logging.config.fileConfig(fname='logging.conf', disable_existing_loggers=False)
    logger = logging.getLogger('Main_program')
    logger.debug('Start of main program')

    # Getting list of files for parsing
    folder_analyzer = FolderAnalyzer(FOLDER_PATH, "fb2")
    folder_analyzer.move_excess_files(TARGET_FOLDER_PATH)
    files_for_parsing = folder_analyzer.full_file_name()
    logger.info(f"Files for parsing: {files_for_parsing}")

    # Parsing file and getting file statistic
    file_statistic = []
    for f in files_for_parsing:
        file_statistic.append(FileParser.get_file_statistic(f))
        logger.info(f"Statistic for file is: {file_statistic}")

    # Adding file statistic to database
    sql_worker = SQLWorker(DATABASE_PATH)
    sql_worker.execute_sql("""CREATE TABLE IF NOT EXISTS books
                (title text, paragraphs_count integer, words_count integer, letters_count integer,
                capital_words_count integer, lower_words_count integer)""")
    for f in file_statistic:
        sql_worker.insert_sql("books", f)
    # sql_worker.execute_sql('DELETE FROM books')


if __name__ == "__main__":
    main()
