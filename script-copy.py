# Source and destination file paths
source_path = "C:\\Users\\PC\\Downloads\\emanuel_barrera_resume_july_01.pdf"
destination_path = "C:\\Users\\PC\\emanuel0918\\cv\\emanuel_barrera_resume.pdf"

# Read the binary content from the source file
with open(source_path, "rb") as source_file:
    binary_content = source_file.read()

# Write the binary content to the destination file
with open(destination_path, "wb") as destination_file:
    destination_file.write(binary_content)
