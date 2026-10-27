# Task 7 — First Chart Story: Turning Numbers into a Narrative

**Track:** Data Analytics  
**Level:** 1 | **Day:** 7  
**Tools:** Excel, CSV, Python (Matplotlib)

## Project overview
This mini-project demonstrates how to choose a chart based on the question being answered. It uses three clearly labeled charts and a short narrative to turn a small sales dataset into understandable insights.

> **Data note:** The sales figures in this project are synthetic/illustrative, created for practice. They are not real company results and are not sourced from the Iris Dataset or World Happiness Report.

## Business questions and chart choices
1. **How do monthly sales compare?** — Bar chart.
2. **How do sales change over time?** — Line chart.
3. **How is sales distributed across product categories?** — Pie chart (three categories only).

## Key findings
- June has the highest monthly sales at ₹24,000; January is the lowest at ₹12,000.
- Sales rise overall from ₹12,000 in January to ₹24,000 in June, a 100% increase, although there is a dip in March.
- Category totals are Electronics ₹42,000 (40.6%), Clothing ₹36,000 (34.8%), and Home & Kitchen ₹25,500 (24.6%).
- The category chart uses three slices, which keeps the comparison readable.

## Narrative
The illustrative sales data shows overall growth during the first six months, with sales doubling from January to June despite a small decline in March. June records the highest monthly sales, suggesting stronger performance toward the end of the period. Across the three product categories, Electronics contributes the largest share of total category sales, followed by Clothing and Home & Kitchen. Together, the charts show both the time-based trend and the category mix, while also demonstrating why chart selection should follow the question: bars compare values, lines show change over time, and a pie chart summarizes a small number of parts of a whole.

## Files
- `First_Chart_Story_Sales_Analysis.xlsx` — workbook with monthly and category data plus native Excel charts.
- `monthly_sales_data.csv` — six-month illustrative dataset.
- `category_sales_data.csv` — category totals for the pie chart.
- `charts/` — exported PNG chart images.
- `report/Task_7_First_Chart_Story_Report.pdf` — formatted report.
- `report/Task_7_First_Chart_Story_Report.docx` — editable report.
- `python_chart_story.py` — script that rebuilds the charts from the CSV files.
- `interview_answers.md` — short answers to the task's interview questions.

## Reproduce charts (optional)
Install dependencies:
```bash
pip install pandas matplotlib
```
Run:
```bash
python python_chart_story.py
```
The Excel workbook already contains the data and charts, so Python is optional for reviewing the result.
