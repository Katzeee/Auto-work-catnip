import datetime
# determine whether one of the word in words_list is in text_str
def IsContain(words_list, text_str) -> bool:
    for word in words_list:
        if word in text_str:
            return True
    return False

def GetCurrentTime():
    return datetime.datetime.now().strftime("%Y-%m-%d %H_%M_%S")