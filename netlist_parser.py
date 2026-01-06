import xml.etree.ElementTree as ET

def extract_design_info(netlist_text):
    design = {
        "components": set(),
        "nets": set()
    }

    try:
        root = ET.fromstring(netlist_text)
    except Exception:
        return design

    for comp in root.findall(".//comp"):
        ref = comp.get("ref", "").upper()
        if ref:
            design["components"].add(ref)

    for net in root.findall(".//net"):
        name = net.get("name", "").upper()
        if name:
            design["nets"].add(name)

    return design
