import os
import platform
import subprocess

def get_system_uptime():
    """
    Returns the system uptime as a string.
    Works on Linux, macOS, and Windows.
    """
    if platform.system() == "Windows":
        # Windows doesn't have a simple uptime command, so use 'net stats srv'
        try:
            output = subprocess.check_output("net stats srv", shell=True, text=True)
            for line in output.splitlines():
                if "Statistics since" in line:
                    return f"System uptime (Windows): {line}"
        except Exception as e:
            return f"Error getting uptime on Windows: {e}"
    elif platform.system() == "Linux":
        try:
            output = subprocess.check_output("uptime -p", shell=True, text=True)
            return f"System uptime (Linux): {output.strip()}"
        except Exception as e:
            return f"Error getting uptime on Linux: {e}"
    elif platform.system() == "Darwin":
        try:
            output = subprocess.check_output("uptime", shell=True, text=True)
            return f"System uptime (macOS): {output.strip()}"
        except Exception as e:
            return f"Error getting uptime on macOS: {e}"
    else:
        return "Unsupported OS for uptime retrieval"

if __name__ == "__main__":
    print(get_system_uptime())
