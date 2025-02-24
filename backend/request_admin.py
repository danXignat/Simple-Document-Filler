import ctypes
import sys

def request_admin():
    """Request administrator privileges."""
    if not ctypes.windll.shell32.IsUserAnAdmin():
        # Re-run the script with admin privileges
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, ' '.join(sys.argv), None, 1)
        sys.exit(0)