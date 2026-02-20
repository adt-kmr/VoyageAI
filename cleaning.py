import os
import re

# Folder containing your code files
folder_path = r"C:\Users\vansh\Downloads\FOLDER\THAPAR\4TH SEMESTER\AIPROJECT"

# Regex patterns
decorative_pattern = re.compile(r"^\s*#\s*[\-\=~•─*]+\s*$")  # decorative lines
step_pattern = re.compile(r"(Step\s*\d+|\d+\.)")             # step numbers
emoji_symbol_pattern = re.compile(r"[^\w\s#,:.-]")           # emojis & extra symbols except basic code chars

for filename in os.listdir(folder_path):
    if filename.endswith(".py"):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        cleaned_lines = []
        for line in lines:
            # Remove decorative lines
            if decorative_pattern.match(line):
                continue
            # Remove step numbers
            line = step_pattern.sub("", line)
            # Remove emojissymbols in comments
            if line.strip().startswith("#"):
                line = emoji_symbol_pattern.sub("", line)
            cleaned_lines.append(line.rstrip() + "\n")

        # Overwrite the original file with cleaned content
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(cleaned_lines)

print("All code files cleaned successfully!")
