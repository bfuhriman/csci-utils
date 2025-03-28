import subprocess
import pymupdf
import sys
import os

# Look for a PDF file in the current directory
def find_pdf():
    for file in os.listdir():
        if file.endswith(".pdf"): return file
    sys.exit("No PDF document was found in the current directory.")

# Parse PDF text for shell commands
def get_cmds(pdf):
    text = chr(12).join(page.get_text() for page in pymupdf.open(pdf)).split("\n")
    return [line.strip() for line in text if line.startswith("./")]

# Print the command, then execute it in the bash shell
def execute(command):
    print(command)
    subprocess.run(command, shell=True, stdout=sys.stdout, stderr=sys.stderr, text=True)

# Run tests
def ctest(pdf):
    commands = get_cmds(pdf)
    if len(sys.argv) > 1:
        if 0 < int(sys.argv[1]) < len(commands):
            execute(commands[int(sys.argv[1]) - 1])
        else:
            print("Invalid command index.")
    else:
        for i, command in enumerate(commands):
            execute(command) 
            if i < len(commands) - 1: print()

ctest(find_pdf())
