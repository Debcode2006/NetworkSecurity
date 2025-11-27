import sys
from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self,error_message, error_details:sys):
        self.error_message = error_message
        _,_,exc_tab = error_details.exc_info()
        
        self.lineno= exc_tab.tb_lineno
        self.file_name = exc_tab.tb_frame.f_code.co_filename
        
        
    def __str__(self):
        return f"Error occurred in the file script [{self.file_name}] line number [{self.lineno}] error message [{str(self.error_message)}]"
    
    