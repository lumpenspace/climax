import os
import subprocess
import sys
import platform

def copy_to_clipboard(files, climax_clipboard=None):
    system_platform = platform.system()
    climax_clipboard = climax_clipboard or os.getenv('CLIMAX_CLIPBOARD')

    abs_path = os.path.abspath(__file__)
    dir_name = os.path.dirname(abs_path)
    
    if system_platform == 'Darwin' or climax_clipboard == 'applescript':
        try:
            subprocess.run(['which', 'osascript'], check=True)
        except subprocess.CalledProcessError:
            print("osascript is not installed. Please install it to use this feature.")
            sys.exit(1)
        try:
            script_path = os.path.join(dir_name, 'copy-macos.applescript')
            subprocess.run(['osascript', script_path] + list(files), check=True)
        except subprocess.CalledProcessError as e:
            print("Failed to copy to the MacOS clipboard.", e.output)
            sys.exit(1)
    elif (system_platform == 'Linux' or climax_clipboard == 'xclip'):
        try:
            subprocess.run(['which', 'xclip'], check=True)
            script_path = os.path.join(dir_name, 'copy-linux-xclip.sh')
            subprocess.run([script_path] + list(files), check=True)
        except subprocess.CalledProcessError:
            raise Exception("install xclip to copy the file to clipboard")
    elif (system_platform == 'Windows' or climax_clipboard == 'powershell'):
        try:
            script_path = os.path.join(dir_name, 'copy-windows.ps1')
            # PowerShell execution policy might prevent the script from running, hence the bypass
            subprocess.run(['powershell', '-ExecutionPolicy', 'Bypass', '-File', script_path] + list(files), check=True)
        except subprocess.CalledProcessError as e:
            print("Failed to copy files to clipboard on Windows, please install PowerShell to use this feature.")

            sys.exit(1)
    else:
        print(f"Unsupported operating system: {system_platform}")
        sys.exit(1)
