import sys
from logger import logging

def error_message_detail(error, error_detail):
    _, _, exc_tb = error_detail
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in Python script: {}, line number: {}. Error message: {}".format(
        file_name, exc_tb.tb_lineno, str(error))
    return error_message

class CustomException(Exception):
    def __init__(self, message="An error occurred"):
        self.message = message
        super().__init__(self.message)

if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Divide by Zero")
        error_detail = sys.exc_info()
        error_msg = error_message_detail(e, error_detail)
        raise CustomException(error_msg)
