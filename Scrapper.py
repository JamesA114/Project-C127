from bs4 import BeautifulSoup
import pandas as pd
import  time
from selenium import webdriver
from selenium.webdriver.common.by import By

scrapped_data = []

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("C:/Users/jimmy/Desktop/CodingClasses/C127/chromedriver.exe")
browser.get(START_URL)
# Webdriver

def scrap():
    soup = BeautifulSoup(browser.page_source, "html.parser")
    bright_star_table = soup.find("table", attrs={"class", "wikitable"})

    table_body = bright_star_table.find('tbody')
    table_rows = table_body.find('tr')
    for row in table_rows:
        table_cols = row.find_all('td')
        print(table_cols)
        temp_list = []
        for col_data in table_cols:
            data = col_data.strip()
            temp_list.append(data)
        scrapped_data.append(temp_list)
scrap()

stars_data = []

for i in range(0, len, (scrapped_data)):
    Star_Names = scrapped_data[i][1]
    Distance = scrapped_data[i][3]
    Mass = scrapped_data[i][5]
    Radius = scrapped_data[i][6]
    Lum = scrapped_data[i][7]

    required_data = [Star_Names, Distance, Mass, Radius, Lum]
    stars_data.append(required_data)
    Headers = ["Star_Names", "Distance", "Mass", "Radius", "Lum"]
    star_df_1 = pd.DataFrame(stars_data, columns = Headers)
    star_df_1.to_csv('scrapped_data.csv', index=True, index_label="id")