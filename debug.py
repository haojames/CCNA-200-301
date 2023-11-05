import ctypes

# Định nghĩa hàm OutputDebugString từ thư viện Windows
kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
OutputDebugString = kernel32.OutputDebugStringW

def debug_message(message):
    message = f"[YourAppName] {message}"
    OutputDebugString(message)

# Ghi thông tin debug vào log
debug_message("This is a debug message.")