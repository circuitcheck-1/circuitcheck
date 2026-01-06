from rules import run_rules
from netlist_parser import extract_design_info

def analyze_netlist(file_path):
    with open(file_path, "r", errors="ignore") as f:
        netlist_text = f.read()

    design_info = extract_design_info(netlist_text)
    return run_rules(design_info)
