import os
from summary_generator import summary
from data_extractor import Report


async def main():
    file_name = "Contoso_Annual_Financial_Report_2022.xlsx"
    file_path = os.path.join("data", file_name)

    if not os.path.exists(file_path):
        return f"File not found: {file_path}"
    
    # Extract data from the report
    report = Report(file_path)
    report_text = report.get_report()

    title, summary_text = await summary(report_text)
    print("Title:", title)
    print(summary_text)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())