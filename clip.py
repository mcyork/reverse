import pyperclip
import re
import socket
import keyboard

def extract_ips(text):
    # Regular expression to extract IP addresses
    ip_pattern = r'(?:\d{1,3}\.){3}\d{1,3}'
    return re.findall(ip_pattern, text)

def reverse_dns_lookup(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return None

def process_clipboard():
    clipboard_content = pyperclip.paste()
    ips = extract_ips(clipboard_content)
    for ip in ips:
        resolved_name = reverse_dns_lookup(ip)
        print(f'{ip}: {resolved_name or "No reverse DNS record"}')

def main():
    print("Press CTRL-Q to process the clipboard. Press CTRL-C to exit.")
    while True:
        if keyboard.is_pressed('ctrl+q'):
            process_clipboard()
            print("\nPress CTRL-Q to process again. Press CTRL-C to exit.")
        # Sleep to prevent high CPU usage
        keyboard.sleep(1)

if __name__ == "__main__":
    main()
