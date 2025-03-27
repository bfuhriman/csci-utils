import subprocess
import pymupdf
import sys
import os

# Look for a PDF file in the current directory
def find_pdf():
    for file in os.listdir():
        if file.endswith(".pdf"): return file
    sys.exit("No PDF document was found in the current directory.")

# Extract text from the PDF document
def text(pdf):
    try:
        return chr(12).join(page.get_text() for page in pymupdf.open(pdf)).split("\n")
    except pymupdf.FileNotFoundError:
        sys.exit(f"Could not find \"{pdf}\" in the current directory.")

# Run the commands from the examples section
def run_tests(pdf):
    commands = [line.strip() for line in text(pdf) if line.startswith("./")]
    for i, command in enumerate(commands):
        print(command)
        subprocess.run(command, shell=True, stdout=sys.stdout, stderr=sys.stderr, text=True)
        if i < len(commands) - 1: print()

pdf = find_pdf()
run_tests(pdf)
