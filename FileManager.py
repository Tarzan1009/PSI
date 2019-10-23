class File_manager:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        file = open(self.file_name)
        text = file.read()
        return text

    def update_file(self, text_data):
        file = open(self.file_name)
        file.write(text_data)
        file.close()
