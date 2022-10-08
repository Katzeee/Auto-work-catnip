from enum import Enum
import datetime
import os

from utils import GetCurrentTime

class Logger:
    def __init__(self, log_file:str = ""):
        self.log_file_ = log_file

    class Color(Enum):
        RED = "\033[31m"
        GREEN = "\033[32m"
        RESET = "\033[0m"
    
    def Log(self, log_content:str, is_to_stdout:bool, color:Color):
        current_log_time_str = datetime.datetime.now().strftime("%H:%M:%S")
        log_content = "[{}] ".format(current_log_time_str) + log_content
        log_str = color.value + log_content + self.Color.RESET.value
        if is_to_stdout == True:
            print(log_str)
        if self.log_file_ != "":
            with open(self.log_file_, 'a', encoding='utf-8') as f:
                f.write(log_content + '\n')

    def Log_RED(self, log_content, is_to_stdout):
        self.Log(log_content, is_to_stdout, self.Color.RED)

    def Log_GREEN(self, log_content, is_to_stdout):
        self.Log(log_content, is_to_stdout, self.Color.GREEN)

folder_path = os.getcwd()
if not os.path.exists(folder_path + "\\Log"):
    os.mkdir(folder_path + "\\Log")
log_path = folder_path + "\\Log\\Log." + GetCurrentTime() + ".txt"
print(log_path)
Root_logger = Logger()
    

