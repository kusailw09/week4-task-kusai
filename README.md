# week4-task-kusai

1️⃣ Movie Recommendation System

Approach:

Used OMDb API to fetch movie details.

Created a Movie class (title, year, rating, genre).

Stored search history in JSON file.

Displayed Top 5 most searched movies.


How to Run:

python movie_system.py

Example Input/Output:

Input → "Inception"

Output → Title: Inception | Year: 2010 | Genre: Sci-Fi | Rating: 8.8


Challenges Faced:

Handling invalid API responses.

Avoiding duplicate entries in search history.



---

2️⃣ Expense Tracker with Analysis

Approach:

Stored income/expense data in CSV.

Used Pandas to calculate totals, highest spending category, and monthly summaries.

Visualized category-wise expenses (bar chart) and monthly trends (line chart).


How to Run:

python expense_tracker.py

Example Output:

Total Income: 50,000

Total Expense: 35,000

Balance: 15,000


Challenges Faced:

Cleaning CSV data after multiple edits.

Mapping categories correctly for visualization.



---

3️⃣ Social Media Scraper & Analyzer

Approach:

Scraped 20–30 posts/headlines using API/web scraping.

Stored results in CSV.

Performed word frequency analysis (excluding stopwords).

Identified longest headline/post.

Generated Word Cloud for visualization.


How to Run:

python scraper_analyzer.py

Example Output:

Most common words: ["India", "Economy", "Tech"]

Longest headline: "Government announces new AI policy for startups..."


Challenges Faced:

Removing stopwords properly.

Handling network/API errors.



---

4️⃣ Student Dashboard

Approach:

Added students with name, roll no, and scores (3 subjects).

Saved into CSV file.

Used Pandas to calculate averages, top performers, pass/fail.

Visualized data with histogram (scores) and bar chart (subject averages).

Code modularized into models/, utils/, and main.py.


How to Run:

python student_dashboard/main.py

Example Output:

Top Performer: Aditi (Avg: 92)

Pass: 18 | Fail: 2


Challenges Faced:

Modularizing code cleanly.

Ensuring CSV consistency after multiple runs.
