import ctypes
import ctypes.wintypes
import getpass

LOGON32_LOGON_INTERACTIVE = 2
LOGON32_PROVIDER_DEFAULT = 0
advapi32 = ctypes.WinDLL("advapi32.dll")

def authenticate_user(user_name, password, domain="."):
    try:
        """Attempts to authenticate a Windows user securely"""
        handle = ctypes.wintypes.HANDLE()
        success = advapi32.LogonUserW(
            user_name, domain, password,
            LOGON32_LOGON_INTERACTIVE,
            LOGON32_PROVIDER_DEFAULT,
            ctypes.byref(handle)
        )
        # Clear password from memory immediately after use
        password = None

        if success:
            ctypes.windll.kernel32.CloseHandle(handle)
            return True
        else:
            print("❌ Authentication failed.")
            return False
    finally:
        # Overwrite password to remove traces from memory
        del password
        del user_name
