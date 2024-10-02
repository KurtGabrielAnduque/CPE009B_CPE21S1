from TextFileReaderWriter import TextFileReaderWriter


tfrw = TextFileReaderWriter()


data_to_write = "This is a simple text file.\nIt contains a few lines of text."
tfrw.write("sample.txt", data_to_write)

# Reading from the text file
tfrw.read("sample.txt")

