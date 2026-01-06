from flask import Flask, render_template, request
import os
from checker import analyze_netlist
from report_generator import generate_pdf_report

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("netlist")

        if not file or file.filename == "":
            return render_template("index.html")

        if not file.filename.lower().endswith((".net", ".xml")):
            return render_template("index.html")

        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        results = analyze_netlist(filepath)
        generate_pdf_report(results, "static/report.pdf")

        return render_template("result.html", results=results)

    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    print("Starting CircuitCheck v1.0")
app.run(host="0.0.0.0", port=5000)


