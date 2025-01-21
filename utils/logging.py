def error_log(text):
    print('\033[31;40;1mError :\033[39;49;0m ' + text)
    
def warning_log(text):
    print('\033[33;40;1mWarning :\033[39;49;0m ' + text)
    
def success_log(text):
    print('\033[32;40;1mSucces :\033[39;49;0m ' + text)

def info_log(text):
    print('\033[34;40;1mInfo :\033[39;49;0m ' + text)