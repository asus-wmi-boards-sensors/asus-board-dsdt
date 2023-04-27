#!/usr/bin/python3
import sys
import os
import yaml
import hashlib
from utils import load_linuxhw_DMI, file_write_with_changes, load_board_flags


if __name__ == "__main__":
    boards_flags = load_board_flags()
    board_desc = load_linuxhw_DMI()
    hash_to_name = {}
    for row in board_desc:
        if len(row) >= 4 and row[3]:
            for hash_value in row[3].split("/"):
                hash_to_name[hash_value] = row[1]

    current_dir = "."
    if len(sys.argv) > 1:
        current_dir = sys.argv[1]

    for dirname, _, filenames in os.walk(current_dir):
        if "/.git" in dirname:
            continue
        # print path to all filenames.
        for filename in filenames:
            name_parts = filename.split(".")
            if len(name_parts) != 2:
                print (f"Skip {filename}")
                continue

            if name_parts[1].lower() != 'bin':
                print (f"Skip incorrect extension {filename}")
                continue

            board_name = hash_to_name.get(name_parts[0])
            if not board_name:
                print (f"Unknown original name {filename}")
                continue

            # produced
            board_producer = ""
            system_name = ""
            for desc in board_desc:
                if len(desc) >= 3:
                    if desc[1] == board_name:
                        board_producer = desc[0]
                        if len(desc) > 4:
                            system_name = desc[4]
                        break

            print (f"Processing {board_name} from {dirname}/{filename}")

            # create flags struct
            if board_name not in boards_flags:
                boards_flags[board_name] = {
                    "board_producer": board_producer,
                }
            board_flags = boards_flags[board_name]
            if not board_flags.get("aliases"):
                board_flags["aliases"] = []

            with open(f"{dirname}/{filename}", "rb") as f:
                content = f.read().decode("utf8")

            parsed_content = []
            lines = content.split("\n")
            for line in lines:
                if not line.strip():
                    continue
                if line.startswith("Firmware Warning (ACPI):"):
                    continue
                line = line.replace("\t", " " * 2)
                if (
                    # could be any amount spaces before real dump
                    line.startswith(" ") and
                    parsed_content and
                    ":" in line
                ):
                    # skip addr
                    line = line.split(":")[1].strip()
                    # get only bynary addr
                    line = line[:16 * 3]
                    # add hex values
                    parsed_content[-1][1] += line.strip().split(" ")
                else:
                    parsed_content.append([line.strip(), []])

            for row in parsed_content:
                if (
                    row[0].startswith("DSDT") or
                    row[0].startswith("SSDT")
                ):
                    if not len(row[1]):
                        print (f"{row[0]} has empty data")
                        continue
                    data = bytes([int(val, 16) for val in row[1]])
                    hash_value = hashlib.md5(data).hexdigest()
                    # board final name
                    produced_by = board_producer
                    board_dump_name = board_name
                    if system_name and produced_by == "Hewlett-Packard":
                        board_dump_name = system_name
                    for ch in "{}()/\\[].":
                        board_dump_name = board_dump_name.replace(ch, " ")
                    # produced
                    if produced_by in ("ASUSTeK COMPUTER INC.", "ASUSTeK Computer INC."):
                        produced_by = "ASUS"
                    elif produced_by == "Gigabyte Technology Co., Ltd.":
                        produced_by = "GIGABYTE"
                    elif produced_by == "Hewlett-Packard":
                        produced_by = "HP"
                    board_dump_name += f" {produced_by}"
                    board_dump_name += " 0000"
                    board_dump_name = board_dump_name.strip().replace(" ", "-")
                    board_dump_fullname = f"dumps/{board_dump_name}.{hash_value}.aml"
                    print (f"Dump file name: {board_dump_fullname}")
                    with open(board_dump_fullname, "wb") as f:
                        f.write(data)
                    # save to aliases
                    if board_dump_name not in board_flags["aliases"]:
                        board_flags["aliases"].append(board_dump_name)

    # save current state
    file_write_with_changes("boards.yaml", yaml.dump(boards_flags))
