import sys
import os

if __name__ == "__main__":
    current_dir = "."
    table = []

    if len(sys.argv) > 1:
        current_dir = sys.argv[1]

    for dirname, _, filenames in os.walk(current_dir):
        # print path to all filenames.
        for filename in filenames:
            if filename.endswith('.dsl'):
                file_parts = filename.split(".")
                if len(file_parts) != 3:
                    print (f"Can't parse filename: '{dirname}/{filename}'")
                board_group = file_parts[0].split("-")
                board_hash = file_parts[1]
                board_version = ""
                # check bios version
                if board_group[-1].isdigit():
                    board_version = int(board_group[-1])
                    board_group = board_group[:-1]
                # check board producer
                board_producer = ""
                if board_group[-1].upper() in ("ASUS"):
                    board_producer = board_group[-1].upper()
                    board_group = board_group[:-1]
                if board_group[0] == "ROG" and board_group[1] == "STRIX":
                    # fix WIFI name
                    if board_group[-1].upper() == "WIFI":
                        board_group[-1] = "(WI-FI)"
                    # create name
                    board_name = f"{board_group[0]} {board_group[1]} "
                    board_name += f"{board_group[2]}-{board_group[3]} "
                    board_name += " ".join(board_group[4:])
                elif board_group[0] == "ROG" and board_group[1] in ("CROSSHAIR", "MAXIMUS"):
                    # fix WIFI name
                    if board_group[-1].upper() == "WIFI":
                        board_group[-1] = "(WI-FI)"
                    # create name
                    board_name = f"{board_group[0]} {board_group[1]} "
                    board_name += " ".join(board_group[2:])
                elif board_group[0] == "TUF" and board_group[1] == "GAMING":
                    # fix WIFI name
                    if board_group[-1].upper() == "WIFI":
                        board_group[-1] = "(WI-FI)"
                    if len(board_group[3]) == 1:
                        board_group = [
                            board_group[0], board_group[1],
                            f"{board_group[2]}-{board_group[3]}"
                        ] + board_group[4:]
                    # create name
                    board_name = f"{board_group[0]} {board_group[1]} "
                    board_name += " ".join(board_group[2:])
                elif board_group[0].upper() in ("PRO", "PRIME"):
                    # create name
                    board_name = f"{board_group[0]} "
                    board_name += "-".join(board_group[1:])
                else:
                    board_name = "-".join(board_group)
                board_name = board_name.replace("_", " ")
                print (f"Board: {board_name}, Version: {board_version} Revision: {board_hash}")
                table.append(
                    f"| {board_name} {' ' * (32 - len(board_name))} "
                    f"| N {' ' * 3} "
                    f"| N {' ' * 3} "
                    f"| N {' ' * 3} "
                    f"| {board_hash} "
                    f"| {board_producer}{' ' * (4 - len(board_producer))} |"
                )

    print ("\n".join(sorted(table)))
