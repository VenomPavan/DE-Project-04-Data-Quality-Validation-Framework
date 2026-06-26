from extract import extract
from validate import validate
from report import generate_report
from logger import setup_logger


logger = setup_logger()


def main():

    logger.info("Data Quality Framework Started")

    df = extract()

    logger.info("CSV Loaded Successfully")

    report = validate(df)

    logger.info("Validation Completed")

    generate_report(report)

    logger.info("Report Generated Successfully")

    print(report)

    logger.info("Project Completed")


if __name__ == "__main__":
    main()