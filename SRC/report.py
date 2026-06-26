from datetime import datetime


def generate_report(report):

    with open("../Output/Quality_Report.txt", "w") as file:

        file.write("=" * 60 + "\n")
        file.write("DATA QUALITY REPORT\n")
        file.write("=" * 60 + "\n\n")

        file.write(f"Generated On : {datetime.now()}\n\n")

        for key, value in report.items():

            file.write(f"{key}\n")
            file.write(f"{value}\n\n")

    print("Quality Report Generated Successfully")