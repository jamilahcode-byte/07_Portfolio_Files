Project: Batch Report Compiler
from pathlib import Path 

#step get folder path & make final report
source = Path("Reports")
output = Path("final_report.txt")

with output.path("w", encoding="utf-8") as out:
    for file in source.glob(".txt"):
        out.write("\n-------{file.name} ---------\n")
        out.write(file.read_text(encoding="utf-8")))
