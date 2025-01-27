def error(text):
    print(f"\033[91mERROR: \033[97m{text}\033[0m")  # Red for critical errors

def warning(text):
    print(f"\033[93mWARNING: \033[97m{text}\033[0m")  # Yellow for non-critical issues

def info(text):
    print(f"\033[94mINFO: \033[97m{text}\033[0m")  # Blue for general information

def success(text):
    print(f"\033[92mSUCCESS: \033[97m{text}\033[0m")  # Green for successful operations

def debug(text):
    print(f"\033[95mDEBUG: \033[97m{text}\033[0m")  # Magenta for debugging output

def critical(text):
    print(f"\033[41mCRITICAL: \033[30m{text}\033[0m")  # Red background for very critical errors

def verbose(text):
    print(f"\033[90mVERBOSE: \033[97m{text}\033[0m")  # Gray for detailed logs


