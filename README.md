# CircuitCheck 

CircuitCheck is a schematic-level PCB design analysis web application that
detects common hardware design mistakes **before fabrication**.

It helps reduce first-board failures by automatically analyzing schematic
netlists and reporting potential design risks with clear recommendations.

---

##  Features

- Upload KiCad schematic netlists (`.net` / `.xml`)
- Automated rule-based schematic checks
- Clear **ERROR** and **WARNING** reports
- Downloadable PDF analysis report
- Clean, mobile-friendly web interface
- No login required (v1.0)

---

##  Checks Implemented (v1.0)

- Floating RESET pin detection
- Missing I²C pull-up resistors
- Missing decoupling capacitors
- Missing reverse polarity protection on power input

---

##  Supported Input

- **KiCad schematic netlist**
  - `.net`
  - `.xml`
- Schematic-level analysis (PCB layout not required)

---

## ▶ Run Locally

```bash
pip install flask reportlab
python app.py
