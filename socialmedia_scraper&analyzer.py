import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

URL = "https://www.bbc.com/news"   # Example site
FILE = "headlines.csv"

# Scrape headlines
res = requests.get(URL)
soup = BeautifulSoup(res.text, "html.parser")
headlines = [h.get_text().strip() for h in soup.find_all("h3")][:30]

# Save to CSV
df = pd.DataFrame(headlines, columns=["Headline"])
df.to_csv(FILE, index=False)

# Text analysis
text = " ".join(headlines).lower()
words = re.findall(r"\b[a-z]{3,}\b", text)  # only words of length >=3
stopwords = {"the","and","for","with","that","from","this","have","not","was","are"}
filtered = [w for w in words if w not in stopwords]

# Most common words
common = Counter(filtered).most_common(5)
print("Most Common Words:", common)

# Longest headline
longest = max(headlines, key=len)
print("Longest Headline:", longest)

# Word Cloud (Bonus)
wc = WordCloud(width=800, height=400, background_color="white").generate(" ".join(filtered))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()