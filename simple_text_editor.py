import os
from termcolor import cprint

def read_file (filename):
    with open (filename, 'r') as file:
        return file.read()
        
def write_file (filename, content):
    with open (filename, 'w') as file:
        file.write (content)

def clear_file(filename):
    cprint('\n⚠️  Type CLEAR to delete everything in the file, or press Enter to skip:', 'red')
    choice = input('> ').strip().lower()
    if choice == 'clear':
        write_file(filename, '')
        cprint(f'🧹 {filename} has been cleared!', 'yellow')
    else:
        return

def get_user_input (filename):
    cprint('\n✏️  Enter your text (type SAVE on a new line to save and exit):', 'cyan')

    lines = []
    while True:
        line = input ()
        command = line.strip().lower()

        if command == 'save':
            break
        elif command == 'undo':
            if lines: 
                removed = lines.pop()
                cprint (f'↩️ Removed last line {removed} successfully', 'yellow')
            else:
                cprint ('⚠️ No lines to undo.', 'red')
        else:
            lines.append (line)

    return '\n'.join(lines)

def main():
    filename = input('Enter the filename to open or create: ').strip()
    try:
        if os.path.exists(filename):
            cprint(f"\n📂 Opening existing file: {filename}\n", 'green')
            print (read_file(filename))
        else:
            cprint(f"\n🆕 Creating new file: {filename}\n", 'yellow')
            write_file(filename, '')
    
        clear_file(filename)

        content = get_user_input(filename)
        write_file (filename, content)
        cprint(f"\n✅ {filename} saved successfully!", 'green')
    except OSError:
        cprint(f"\n❌ Error: {filename} could not be opened or written.", 'red')


if __name__ == '__main__':
    main()