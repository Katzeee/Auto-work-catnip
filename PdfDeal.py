from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import pdfplumber
from Logger import Root_logger
import numpy as np
from utils import *
import os


class PDFDeal:
    exculde_names_ = ["Technical", "Techinical"] # these words are the difference between pdf files need to be processed and need not. One file whose name contains these words will not be processed
    def __init__(self, folder_path):
        self.folder_path_ = folder_path
        self.browser = webdriver.Edge()
        self.browser.minimize_window()
        self.browser.get('https://fanyi.baidu.com')
        self.input = self.browser.find_element(By.ID, "baidu_translate_input")
        self.file_paths_ = []
        self.problem_overviews_ = []
        self.problem_overviews_translate_ = []
        self.project_numbers_ = []
        self.part_numbers_ = []
        self.group_numbers_ = []
        self.GetAllFiles()
        self.ParseAll()

    def __del__(self):
        self.browser.close()

    def GetAllFiles(self):
        for i in os.listdir(self.folder_path_):
            current_folder = self.folder_path_ + "\\" + i
            if os.path.isdir(current_folder):
                for j in os.listdir(current_folder):
                    if "pdf" in j and not IsContain(self.exculde_names_, j):
                        self.file_paths_.append(current_folder + "\\" + j) 
        Root_logger.Log_GREEN("All PDF files in the folder: " + str([file.split('\\')[-1].split('.')[0] for file in self.file_paths_]), True)

    def ParseAll(self):
        for file in self.file_paths_:
            Root_logger.Log_GREEN("==============processing " + file.split('\\')[-1].split('.')[0] + "==============", True)
            pdf = pdfplumber.open(file)
            self.ParseProblemOverview(pdf)
            self.ParseProjectNumber(pdf)
            self.ParsePartNumber(pdf)
            self.ParseGroupNumber(pdf)

    def ParseProblemOverview(self, pdf:pdfplumber.pdf.PDF):
        content = pdf.pages[0].extract_tables()[0][8][0]
        if content is None:
            Root_logger.Log_RED("==============     Failed      ==============", True)
        else:
            Root_logger.Log_GREEN("==============     Succeed      ==============", True)
        content = content.replace('\n', ' ')
        self.problem_overviews_.append(content)
        content_translate = self.Translate(content)
        self.problem_overviews_translate_.append(content_translate)

    def ParseProjectNumber(self, pdf:pdfplumber.pdf.PDF):
        self.project_numbers_.append(pdf.pages[0].extract_tables()[0][0][1].split('\n')[-1])

    def ParsePartNumber(self, pdf:pdfplumber.pdf.PDF):
        self.part_numbers_.append(pdf.pages[0].extract_tables()[0][0][4].split(':  ')[-1])
    
    def ParseGroupNumber(self, pdf:pdfplumber.pdf.PDF):
        self.group_numbers_.append(pdf.pages[0].extract_tables()[0][4][0].split(': ')[1].split('\n')[0])


    def Translate(self, content:str) -> str:
        self.input.clear()
        self.input.send_keys(content)
        sleep(2)
        output = self.browser.find_element(By.CLASS_NAME, "output-bd")
        return output.text


        

    def AA(self):
        empty = np.array(["" for i in range(len(self.file_paths_))])
        a = np.array([[file.split('\\')[-1].split('.')[0] for file in self.file_paths_], self.problem_overviews_, self.problem_overviews_translate_, empty, self.project_numbers_, self.part_numbers_, self.group_numbers_])
        return a.transpose()
            
    