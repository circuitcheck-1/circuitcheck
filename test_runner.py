import os
from checker import analyze_netlist

TEST_DIR = "tests"

def run_tests():
    print("Running automated PCB rule tests...\n")

    for category in ["good", "bad"]:
        folder = os.path.join(TEST_DIR, category)
        for file in os.listdir(folder):
            path = os.path.join(folder, file)
            results = analyze_netlist(path)

            if category == "good" and results:
                print(f"❌ FAIL (should be clean): {file}")
            elif category == "bad" and not results:
                print(f"❌ FAIL (should have issues): {file}")
            else:
                print(f"✅ PASS: {file}")

if __name__ == "__main__":
    run_tests()
