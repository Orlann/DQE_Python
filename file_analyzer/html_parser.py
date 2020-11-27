import logging
import logging.config

from bs4 import BeautifulSoup

INPUT_FILE_PATH = r"D:\OrlAnn\DQE_MentorProgram\Module_4_Python\Input\Example_4.fb2"


def get_text_from_file(file_name):
    try:
        with open(file_name, encoding="utf8") as file:
            file_text = file.read()
            html_text = BeautifulSoup(file_text, "html.parser")
            return html_text.body
    except IOError:
        print("Error with file")


def get_title(html_text):
    title_block = html_text.title
    title_children = [e.text for e in title_block if e.name is not None]
    title = title_children[1]
    return title


def get_paragraphs(html_text):
    paragraphs = html_text.find_all(['p'])
    return paragraphs


def words_in_paragraph(paragraph):
    words = paragraph.split()
    return words


def words_in_paragraphs(array_of_paragraphs):
    words = []
    for p in array_of_paragraphs:
        words.extend(words_in_paragraph(p.text))
    return words


def count_characters_in_word(word):
    count_of_characters = len(word)
    return count_of_characters


def count_characters_in_words(array_of_words):
    total_characters = 0
    for w in array_of_words:
        total_characters += count_characters_in_word(w)
    return total_characters


def is_word_capital(word):
    is_upper = word[0].isupper()
    return is_upper


def count_words_with_capital_letter(array_of_words):
    capital_words_count = 0
    for w in array_of_words:
        if is_word_capital(w):
            capital_words_count += 1
    return capital_words_count


def main():
    logging.config.fileConfig(fname='logging.conf', disable_existing_loggers=False)
    logger = logging.getLogger('Parser')

    file_text = get_text_from_file(INPUT_FILE_PATH)
    logger.debug(file_text)
    title = get_title(file_text)
    logger.info(f"Book title is {title}")

    paragraphs = get_paragraphs(file_text)
    logger.info(f"Paragraphs: {paragraphs}")

    number_of_paragraphs = len(paragraphs)
    logger.info(f"Number of paragraphs: {number_of_paragraphs}")

    total_words_array = words_in_paragraphs(paragraphs)
    total_words_count = len(total_words_array)
    logger.info(f"Total words count: {total_words_count}")

    capitalized_word_count = count_words_with_capital_letter(total_words_array)
    logger.info(f"Total count of capitalized words: {capitalized_word_count}")

    lowercase_word_count = total_words_count - capitalized_word_count
    logger.info(f"Total count of lowercase words: {lowercase_word_count}")

    characters_count = count_characters_in_words(total_words_array)
    logger.info(f"Total letters count: {characters_count}")


if __name__ == "__main__":
    main()
