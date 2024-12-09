import os
from utils.summary_generator import summary
from utils.data_extractor import Report


async def get_summary(file):
    # Extract data from the report
    report = Report(file)
    report_text = report.get_report()
    try:
        title, summary_text = await summary(report_text)
        return title, summary_text
    except Exception as e:
        return "Error", str(e)
