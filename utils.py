import csv
import yaml


def load_linuxhw_DMI():
    board_desc = []
    try:
        with open("docs/linuxhw_DMI.csv", newline='') as f:
            reader = csv.reader(f)
            try:
                for row in reader:
                    if (
                        not row[0] or
                        not row[1]
                    ):
                        continue
                    elif (
                        "To be filled by O.E.M." in row[0] or
                        "To be filled by O.E.M." in row[1]
                    ):
                        continue
                    board_desc.append(row)
            except csv.Error as ex:
                print (f"Could not read docs/linuxhw_DMI.csv: {ex}")
        print (f"Loaded {len(board_desc)} boards descriptions.")
    except Exception as ex:
        print (f"Could not read linuxhw_DMI.csv: {ex}")
    return board_desc


def save_linuxhw_DMI(board_desc):
    try:
        with open("docs/linuxhw_DMI.csv", 'w', newline='') as f:
            writer = csv.writer(f)
            for row in board_desc:
                writer.writerow(row)
        print (f"Saved {len(board_desc)} boards descriptions.")
    except Exception as ex:
        print (f"Could not write linuxhw_DMI.csv: {ex}")


def file_write_with_changes(name, content):
    try:
        with open(name, "rb") as f:
            if f.read().decode("utf8") == content:
                print (f"Same content {name}")
                return
    except Exception as ex:
        print (f"Could not read {name}: {ex}")
    with open(name, "wb") as f:
        f.write(content.encode("utf8"))


def load_board_flags():
    boards_flags = {}
    try:
        with open("boards.yaml", "rb") as f:
            boards_flags.update(yaml.load(f.read().decode("utf8"), yaml.Loader))
        print (f"Loaded {len(boards_flags.keys())} boards.")
    except Exception as ex:
        print (f"Could not read boards.yaml: {ex}")
    return boards_flags
