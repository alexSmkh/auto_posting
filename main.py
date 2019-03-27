from dotenv import load_dotenv
from os.path import join
from os import getcwd
from os import getenv
from post_to_vk import create_post_on_vk
from post_to_telegram import create_post_on_telegtam
from post_to_facebook import create_post_on_fb


def main():
    load_dotenv(join(getcwd(), '.env'))
    path_to_picture_for_posting = getenv('PATH_TO_FILE')
    message_for_posting = getenv('MESSAGE')
    create_post_on_vk(path_to_picture_for_posting, message_for_posting)
    create_post_on_telegtam(path_to_picture_for_posting, message_for_posting)
    create_post_on_fb(path_to_picture_for_posting, message_for_posting)


if __name__ == '__main__':
    main()
