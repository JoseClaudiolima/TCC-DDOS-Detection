import ctypes
import ctypes.wintypes
import getpass

LOGON32_LOGON_INTERACTIVE = 2
LOGON32_PROVIDER_DEFAULT = 0
advapi32 = ctypes.WinDLL("advapi32.dll")

def authenticate_user(domain="."):
    try:
        # Get username and password
        user = input("Enter your username: ")
        pwd = getpass.getpass("Enter your password: ")

        """Attempts to authenticate a Windows user securely"""
        handle = ctypes.wintypes.HANDLE()
        success = advapi32.LogonUserW(
            user, domain, pwd,
            LOGON32_LOGON_INTERACTIVE,
            LOGON32_PROVIDER_DEFAULT,
            ctypes.byref(handle)
        )
        # Clear password from memory immediately after use
        pwd = None

        if success:
            print("✅ Authentication successful!")
            ctypes.windll.kernel32.CloseHandle(handle)
            return True
        else:
            print("❌ Authentication failed.")
            return False
    finally:
        # Overwrite password to remove traces from memory
        del pwd
        del user
