# Sales-analytics-dashboard
We will use SQl to clean data, Python to manipulate and plot, Power BI to visualize the data

# 📊 Sales Analytics Dashboard (SQL + Python + Power BI)

This project is an end-to-end **Sales Analytics** solution using:
- **SQL** for data cleaning and KPI extraction
- **Python (Pandas, Matplotlib)** for EDA
- **Power BI** for dashboard visualization

The goal is to demonstrate skills in:
✔ Data cleaning  
✔ ETL workflow  
✔ SQL querying  
✔ KPI creation  
✔ Dashboard building  
✔ Business insights  

---

## 🔧 Tools Used
- Python (Pandas, NumPy, Matplotlib)
- SQL (PostgreSQL / MySQL)
- Power BI / Tableau
- GitHub

---

## 📁 Project Structure
- `data/` → raw + cleaned datasets  
- `sql/` → table creation, cleaning, and KPI queries  
- `notebooks/` → Python EDA notebook  
- `dashboard/` → Power BI dashboard  
- `README.md` → documentation  

---

## 📈 KPIs Included
- Total Revenue  
- Year-over-Year Growth  
- Customer Lifetime Value  
- Top 10 Products  
- Monthly Sales Trend  
- Region-wise Performance  
- Revenue Forecast (optional)

---

## 🔍 SQL Examples

### Table Creation
```sql
CREATE TABLE sales (
    order_id INT PRIMARY KEY,
    order_date DATE,
    customer_id INT,
    product VARCHAR(255),
    category VARCHAR(50),
    quantity INT,
    price NUMERIC(10,2),
    region VARCHAR(50)
);
