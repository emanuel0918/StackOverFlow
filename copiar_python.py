# Open the PNG file for reading in binary mode
with open('C:\\Users\\Emanuel\\Documents\\input.txt', 'rb') as reader:
    # Read the content of the PNG file as bytes
    content = reader.read()
with open ('C:\\Users\\Emanuel\\Downloads\\output.txt', 'wb') as writer:
    writer.write(content)
# Display the number of bytes read
print(f"Number of bytes read: {len(content)}")

