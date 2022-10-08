import xlwings as xw
import numpy as np
from Logger import Root_logger
from utils import *

class ExcelFill():
    def __init__(self, excel_name:str) -> None:
        self.app = xw.App(visible=True, add_book=False)
        self.app.display_alerts = False
        self.app.screen_updating = False
        self.wb = self.app.books.open(excel_name)

    def __del__(self):
        self.wb.close()
        self.app.quit()
    
    def FillTaskList(self, content:np.array):
        sheet = self.wb.sheets('Ramp-up')
        copy_name = "Ramp-up C" + GetCurrentTime()
        sheet.copy(name=copy_name)

        aeko_number_done = sheet.range('C8').expand('down').value
        parse_names = content.transpose()[0]
        wait_fill_name = set(parse_names) - set(aeko_number_done)

        if wait_fill_name == set():
            Root_logger.Log_GREEN("Everything is up to date! Nothing need modifying!", True)
            return
        
        Root_logger.Log_GREEN("Already done in xlsx: " + str(set(parse_names) - wait_fill_name), True)
        Root_logger.Log_GREEN("Havn't been filled in xlsx: " + str(wait_fill_name), True)

        box_wait_to_fill = sheet.range('C8').offset(row_offset=len(aeko_number_done))

        if (box_wait_to_fill.value is not None):
            Root_logger.Log_RED("There is data in box C{}, process break!".format(8+len(aeko_number_done)), True)
            return
        
        final_results = []
        for result in content:
            if result[0] in wait_fill_name:
                final_results.append(list(result))

        Root_logger.Log_GREEN("Filling box start at C{}".format(8+len(aeko_number_done)), True)
        Root_logger.Log_GREEN("Following data will be filled into boxs: " + str(final_results), True)


        box_wait_to_fill.value = final_results
        self.wb.save()

