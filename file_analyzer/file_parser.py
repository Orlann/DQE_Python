import logging
import logging.config

from bs4 import BeautifulSoup


class FileParser:

    @staticmethod
    def get_text_from_file(file):
        try:
            with open(file, encoding="utf8") as file:
                file_text = file.read()
                html_text = BeautifulSoup(file_text, "html.parser")
                return html_text.body
        except IOError:
            print("Error with file")

    @staticmethod
    def get_title(html_text):
        title_block = html_text.title
        title_children = [e.text for e in title_block if e.name is not None]
        title = title_children[1]
        return title

    @staticmethod
    def get_paragraphs(html_text):
        paragraphs = html_text.find_all(['p'])
        return paragraphs

    @staticmethod
    def words_in_paragraph(paragraph):
        words = paragraph.split()
        return words

    @staticmethod
    def words_in_paragraphs(array_of_paragraphs):
        words = []
        for p in array_of_paragraphs:
            words.extend(FileParser.words_in_paragraph(p.text))
        return words

    @staticmethod
    def count_characters_in_word(word):
        count_of_characters = len(word)
        return count_of_characters

    @staticmethod
    def count_characters_in_words(array_of_words):
        total_characters = 0
        for w in array_of_words:
            total_characters += FileParser.count_characters_in_word(w)
        return total_characters

    @staticmethod
    def is_word_capital(word):
        is_upper = word[0].isupper()
        return is_upper

    @staticmethod
    def count_words_with_capital_letter(array_of_words):
        capital_words_count = 0
        for w in array_of_words:
            if FileParser.is_word_capital(w):
                capital_words_count += 1
        return capital_words_count

    @staticmethod
    def get_file_statistic(file_path):
        logging.config.fileConfig(fname='logging.conf', disable_existing_loggers=False)
        logger = logging.getLogger('Parser')

        file_statistic = []
        file_text = FileParser.get_text_from_file(file_path)
        logger.debug(file_text)
        title = FileParser.get_title(file_text)
        logger.debug(f"Book title is {title}")
        file_statistic.append(title)

        paragraphs = FileParser.get_paragraphs(file_text)
        logger.debug(f"Paragraphs: {paragraphs}")

        number_of_paragraphs = len(paragraphs)
        logger.debug(f"Number of paragraphs: {number_of_paragraphs}")
        file_statistic.append(number_of_paragraphs)

        total_words_array = FileParser.words_in_paragraphs(paragraphs)
        total_words_count = len(total_words_array)
        logger.debug(f"Total words count: {total_words_count}")
        file_statistic.append(total_words_count)

        capitalized_word_count = FileParser.count_words_with_capital_letter(total_words_array)
        logger.debug(f"Total count of capitalized words: {capitalized_word_count}")
        file_statistic.append(capitalized_word_count)

        lowercase_word_count = total_words_count - capitalized_word_count
        logger.debug(f"Total count of lowercase words: {lowercase_word_count}")
        file_statistic.append(lowercase_word_count)

        characters_count = FileParser.count_characters_in_words(total_words_array)
        logger.debug(f"Total letters count: {characters_count}")
        file_statistic.append(characters_count)
        return file_statistic


