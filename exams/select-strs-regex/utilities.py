def get_file_content(file_name):
    with open(file_name, "r", encoding="utf8") as f:
        return f.read()
