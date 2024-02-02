from pathlib import Path


def get_cats_info(path: str) -> list:
    """Conversion of data into a dictionary"""
    cats_info = []
    path = Path(path)

    if not path.exists():
        print(f"The file does not exist: {path}")
        exit()

    try:
        with open(path, mode="r", encoding="utf-8") as file:
            lines = [el.strip() for el in file.readlines() if el.strip()]
    except Exception as e:
        print(f"The file does not exist: {e}")
        exit()

    for line in lines:
        items_line = line.split(",")
        cats_info.append(
            {"id": items_line[0], "name": items_line[1], "age": items_line[2]}
        )
    return cats_info


cats_info = get_cats_info("cats_file.txt")
print(cats_info)
