from python_drivers.common.ewa_instrument import EwaInstrument
import ewa_test_stations
import configparser
import socket
import os
import time
from datetime import datetime
import csv
import json

''' Reads the options from the instruments connected to the bench

Args:
    instrument_list: The list of instruments connected to the bench

Returns:
    option_dict: A dict with the instruments and their corresponding options
        '''
def read_options(instrument_list):
    option_dict = {}

    for key in instrument_list:
        try: 
            ins = EwaInstrument(key).instrument
            ls = ins.read("*IDN?").split(",")
            ls.extend(ins.read("*OPT?").split(","))
            option_dict[key] = ls
        except Exception as error:
            print(f"! {key} not connected !")
            print(error)
    return option_dict


''' Writes the serial number, firmware and options of each instrument to instruments.json

Args:
    read_path: The path to where instruments.json is located
        '''
def write_to_json(read_path):
    instrument_list = []
    json_path = os.path.join(read_path, "instruments.json")
    content = json.loads(open(json_path).read())

    for inst in content:
        instrument_list.append(inst["id"])

    option_dict = read_options(instrument_list)

    for inst in content:
        if option_dict.get(inst["id"]) is not None:
            inst["serial"] = option_dict[inst["id"]][2]
            inst["firmware"] = option_dict[inst["id"]][3]

            for i in range(4,len(option_dict[inst["id"]])):
                inst[f"option{i - 3}"] = option_dict[inst["id"]][i]
            
    json.dump(content, open(json_path, mode="w"), indent="")

''' Writes instrument brand, model, serial number, framework and options to a .csv 

Args:
    read_path: The path to where station.ini is located
        '''
def write_to_csv(read_path):
    instrument_list = []
    parser = configparser.ConfigParser()
    parser.optionxform=str
    parser.read(os.path.join(read_path, "station.ini"))
    instrument_list = parser["Instruments"].keys()

    option_dict = read_options(instrument_list)       

    timestr = time.strftime("%Y%m%d_%H%M%S")

    # Results format and directories
    csv_dir = f"\\\\sessisgroup01001.ss.sw.ericsson.se\\rf\\RF_ASIC_LD\\Lab\\Instruments\\Instrument_Options\\{computer_name}"

    # getting the current date and time
    current_datetime = datetime.now()

    # getting the date and time from the current date and time in the given format
    foldername = current_datetime.strftime("%Y%m%d_%H%M%S")

    csv_path = os.path.join(csv_dir, foldername)

    os.makedirs(csv_path)

    csv_filename = os.path.join(csv_path, 'ins_options.csv')
    fields = ['Instrument', 'Brand', 'Model', 'Serial', 'FW', 'Options']

    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(fields)
        for ins in option_dict:
            row = [ins]
            row.extend(option_dict[ins])
            writer.writerow(row)


computer_name = socket.gethostname()
read_path = f"{os.path.dirname(ewa_test_stations.__file__)}\\{computer_name}\\"

# If instruments.json exists, write to json. else read from station.ini and write to csv.
if os.path.exists(os.path.join(read_path, "instruments.json")):
    write_to_json(read_path)
else:
    write_to_csv(read_path)

