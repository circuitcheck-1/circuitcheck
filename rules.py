def run_rules(design):
    issues = []

    components = design["components"]
    nets = design["nets"]

    has_r = any(c.startswith("R") for c in components)
    has_c = any(c.startswith("C") for c in components)
    has_d = any(c.startswith("D") for c in components)
    has_u = any(c.startswith("U") for c in components)

    if "RESET" in nets and has_u and not has_r:
        issues.append({
            "level": "ERROR",
            "title": "Floating RESET pin",
            "description": "RESET net exists but no pull-up resistor detected.",
            "fix": "Add a 10kΩ pull-up resistor from RESET to VCC."
        })

    if "SCL" in nets and "SDA" in nets and not has_r:
        issues.append({
            "level": "ERROR",
            "title": "Missing I2C pull-up resistors",
            "description": "I2C bus requires pull-up resistors on SDA and SCL lines.",
            "fix": "Add 4.7kΩ–10kΩ pull-up resistors to VCC."
        })

    if "VCC" in nets and has_u and not has_c:
        issues.append({
            "level": "WARNING",
            "title": "Missing decoupling capacitor",
            "description": "No decoupling capacitor detected near MCU power pins.",
            "fix": "Add a 0.1µF ceramic capacitor close to each VCC pin."
        })

    if "POWER_IN" in nets and not has_d:
        issues.append({
            "level": "WARNING",
            "title": "No reverse polarity protection",
            "description": "Board may be damaged if power is connected incorrectly.",
            "fix": "Add a diode or MOSFET-based reverse polarity protection."
        })

    return issues
