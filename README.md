### Dependencies

*  Python >= 3.8
*  Sqlite3

### Setup

Run these commands in a shell:

```bash

    # Setuping python-side
    python3 -m venv env 
    source env/bin/activate
    pip3 install -r requirements.txt

    # Setuping db
    sqlite3 sql_app.db ".read dataset.sql"

    # ... And FINALLY
    # Running the project in the default 8000 port
    hypercorn sql_app.main:app
```

### API cases that should be written here explicitly:

1. Show the number of impressions and clicks that occurred before the 1st of June 2017, broken down by channel and country, sorted by clicks in descending order.
    http://localhost:8000/api/?date_to=2017-06-01&group_by=channel&group_by=country&order_by=clicks.desc

2. Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order.
    http://localhost:8000/api/?date_to=2017-05-01&date_to=2017-05-31&group_by=date&order_by=date.asc&filter_by=os:iOS

3. Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order.
    http://localhost:8000/api/?date_to=2017-06-01&date_to=2017-06-01&filter_by=country:%20US&group_by=os&order_by=revenue.desc

4. Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order. Please think carefully which is an appropriate aggregate function for CPI.
    http://localhost:8000/api/?filter_by=country:%20CA&group_by=channel&order_by=cpi.desc
