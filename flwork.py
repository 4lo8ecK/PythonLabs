def get_codes(path: str) -> list:
    content = []
    try:
        with open(path, 'r') as file:
            content = file.readlines()
            for i in range(len(content)):
                content[i] = str(content[i])[:-1]
    except FileNotFoundError:
        return content
    return content
# !get_codes(str) -> list

