import os
import ccfatigue.modules.sn_curve_loglog as sn_curve_loglog


def test_sn_curve_loglog():
    SRC_DIR = os.path.dirname(os.path.realpath(__file__))
    DATA_DIR = os.path.join(SRC_DIR, "..", "..", "Data")
    INPUT_FILENAME = "AGG_input.csv"
    INPUT_FILE = os.path.join(DATA_DIR, INPUT_FILENAME)
    print(f"input file: {INPUT_FILE}")
    OUTPUT_JSON_FILENAME = "SNC_LogLog.json"
    OUTPUT_JSON_FILE = os.path.join(DATA_DIR, OUTPUT_JSON_FILENAME)
    OUTPUT_CSV_FILENAME = "SNC_LogLog.csv"
    OUTPUT_CSV_FILE = os.path.join(DATA_DIR, OUTPUT_CSV_FILENAME)
    sn_curve_loglog.execute(INPUT_FILE, OUTPUT_JSON_FILE, OUTPUT_CSV_FILE)
