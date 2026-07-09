import pandas as pd
from fpdf import FPDF

# CSV file read karo
df = pd.read_csv("students.csv")

# Average calculate karo
df["Average"] = (df["Math"] + df["Science"] + df["English"]) / 3

# PDF banao
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)

pdf.cell(200, 10, "Student Report", ln=True, align="C")
pdf.ln(10)

pdf.set_font("Arial", size=12)

for index, row in df.iterrows():
    pdf.cell(200, 10, f"{row['Name']} - Average: {row['Average']:.2f}", ln=True)

pdf.output("Student_Report.pdf")

print("Report Successfully Generated!")