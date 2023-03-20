#!/usr/bin/python3
import sys
import os
import csv
from utils import load_linuxhw_DMI, save_linuxhw_DMI


def __dmi_fix_result(result):
    non_dict = False
    keys = []

    for i in range(len(result)):
        if not result[i][1]:
            parts = result[i][0].split(":")
            if len(parts) > 1:
                result[i] = [parts[0].strip(), ":".join(parts[1:]).strip()]
            else:
                result[i] = result[i][0]
                non_dict = True
        else:
            if result[i][0][-1] == ":":
                result[i][0] = result[i][0][:-1]
        if not non_dict:
            if result[i][0] in keys:
                non_dict = True
            else:
                keys.append(result[i][0])

    if not non_dict:
        dict_result = {}
        for row in result:
            dict_result[row[0]] = row[1]
        return dict_result
    return result


def dmi_process_line(lines, ident=0):
    result = []
    while lines:
        line = lines.pop(0)
        if not line.strip():
            continue
        elif line.startswith("\t" * (ident + 1)):
            lines.insert(0, line)
            result[-1][1] = dmi_process_line(lines, ident + 1)
        elif line.startswith("\t" * ident):
            result.append([line.strip(), []])
        else:
            lines.insert(0, line)
            return __dmi_fix_result(result)
    return __dmi_fix_result(result)


def dmi_process(content):
    dmi_data = dmi_process_line(content.split("\n"))
    board_producer = ""
    board_name = ""
    board_sensor = ""

    for record in dmi_data:
        if isinstance(record, list):
            if (
                len(record) == 2 and
                record[0] == "Base Board Information" and
                isinstance(record[1], dict)
            ):
                board_producer = record[1].get("Manufacturer")
                board_name = record[1].get("Product Name")
            elif (
                len(record) == 2 and
                record[0] == "Management Device" and
                isinstance(record[1], dict) and
                record[1].get("Address Type") == "I/O Port" and
                record[1].get("Type") == "Other"
            ):
                board_sensor = record[1].get("Description")
                for sensor_producer in ["SMsC", "SmSC", "Nuvoton", "Winbond", "ITE"]:
                    if f"{sensor_producer} " in board_sensor:
                        board_sensor = board_sensor.replace(f"{sensor_producer} ", "")

    return board_producer, board_name, board_sensor


if __name__ == "__main__":
    board_desc = load_linuxhw_DMI()

    current_dir = "."
    if len(sys.argv) > 1:
        current_dir = sys.argv[1]

    sensors = []

    for dirname, _, filenames in os.walk(current_dir):
        if "/.git" in dirname:
            continue
        # print path to all filenames.
        for filename in filenames:
            print (f"Processing: {dirname}/{filename}")

            try:
                with open(f"{dirname}/{filename}", "rb") as f:
                    content = f.read().decode("utf8")

                board_producer, board_name, board_sensor = dmi_process(content)
            except:
                print (f"Could not parse: {dirname}/{filename}")
                continue

            print (f"\tBoard: {board_name}")
            print (f"\tProduced: {board_producer}")
            print (f"\tSensor: {board_sensor}")
            if (
                not board_producer or
                not board_name
            ):
                continue

            if board_sensor:
                if board_sensor not in sensors:
                    sensors.append(board_sensor)

            for row in board_desc:
                if (
                    row[0].upper() == board_producer.upper() and
                    row[1].upper() == board_name.upper()
                ):
                    if board_sensor:
                        row[2] = board_sensor
                    if len(row) < 4:
                        row.append(filename)
                    else:
                        names = row[3].split("/")
                        if filename not in names:
                            names.append(filename)
                        row[3] = "/".join(sorted(names))
                    break
            else:
                board_desc.append([board_producer, board_name, board_sensor, filename])

    print ("Used sensors:")
    for board_sensor in sorted(sensors):
        print (f"\t{board_sensor}")
    board_desc.sort()
    save_linuxhw_DMI(board_desc)
