from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import re
import ast
import datetime
import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.worksheet.table import Table, TableStyleInfo

# import sqlite3

# import csv
# import pandas as pd
# from pandas import DataFrame

# Setting up the environment and getting the web page raddy to scrap
driver = webdriver.Chrome('C:/Users/User/AppData/Local/Programs/Python/Python38/Scripts/chromedriver.exe')
driver.maximize_window()
url = "https://www.betfair.ro/exchange/plus/ro/curse-de-cai-pariuri-7/next"
driver.get(url)

# print(driver.page_source)

# x = 0
# while x < 100:

# Get the list of events and some other tabs from the page
race_list = []
races_class = WebDriverWait(driver, 30).until(ec.presence_of_all_elements_located((By.CLASS_NAME, "node")))
for race in races_class:
    race_list.append(race.text)
#     print(race.text)
# print(race_list)

# Because the list is in the second element it had to be separated and then use re library to select each event
# the re library is to select only te time "tag", the rest of the elements don't have the hour pattern
# THINGS TO SOLVE IN HERE:
# SOMETIMES THE PAGE DOESN'T LOAD PROPERLY AND FOR THIS REASON CAN'T FIND THE SECOND ELEMENT
# THERE IS TRY AND EXCEPT BUT DOESN'T WORK PROPERLY, WHEN CAN'T FIND THE SECOND ELEMENT
# THE PROBLEM GOES DOWN TO THE NEXT STATEMENT AND GIVES AN ERROR BECAUSE IT CAN'T FIND THE EVENTS
# VARIABLE
try:
    race_list = race_list[2].split()
    scheduled_hours = [i for i in race_list if re.search(r'\d\d:\d\d', i)]
    events = scheduled_hours[:7]  # only 10 events
    # print(events)
except:
    "IndexError: list index out of range"

# Preparing each event for the scrap: obtaining the sum that it's been bet on the event, the title and the buttons
# obtaining all the links from the horse racing page
# PROBLEM TO BE DEALT WITH:
# WHEN IT LOOPS THROUGH ALL THE LINKS, IT TAKES THOSE RACES WITH THE SAME NAMES THAT ARE A DAY APART
# FOR NOW THIS ISN'T A PROBLEM BECAUSE THE RACES THAT ARE ON THE NEXT DAY DON'T MEET THE REQUIREMENT
# OF HAVING THE TOTAL SUM OF MONEY OVER 5000 LEI, BUT JUST A SMALL BUG TO HAVE IN MIND
race_title = []
race_link = []
for event in events:
    races = driver.find_elements_by_partial_link_text(event)
    for race in races:
        race_title.append(race.text)
        race_link.append(race.get_attribute('href'))


# print(race_title)
# for link in race_link:
#     print(link)

# Find the race winner
# HERE IS A DELAY IMPLEMENTED, AFTER EACH ROW CHECKED WAITS 5 SEC FOR THE JOKEY TO BE
# IDENTIFIED, SO SAY IF THE WINNER IS AT POSITION 5, IT WILL TAKE 20 TO 25 SEC GET
# THE CORRECT ANSWER
def race_finished():
    jockey_names = WebDriverWait(driver, 30).until(ec.presence_of_all_elements_located((By.CLASS_NAME, "name")))
    jockey_names_list = []
    for jockey in jockey_names:
        jokey_01 = jockey.text
        jockey_names_list.append(jokey_01)
        race_winner = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME, "runner-winner")))
        race_win01: str = '//*[@id="main-wrapper"]/div/div[2]/div/ui-view/div/div/div[1]/div[3]/div/div[' \
                          '1]/div/bf-main-market/bf-main-marketview/div/div[2]/bf-marketview-runners-list[' \
                          '2]/div/div/div/table/tbody/tr['
        race_win02: str = ']/td/div[1]/div[2]/div'
    # print(jockey_names_list)
    position_final = []

    for position in range(len(jockey_names)):
        race_w = race_win01 + str(position + 1) + race_win02
        try:
            winner = WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.XPATH, race_w)))
            if winner.text == "Câştigător":
                position_final.append(position)
            break
        except:
            "TimeoutException"

    venue_name = WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.CLASS_NAME, "venue-name")))
    venue_name_final = venue_name.text
    winner_final = jockey_names_list[int(position_final[0])]

    print(venue_name_final)
    print(winner_final)


# This function takes the races that meet the requirements
# IN HERE SHOULD BE THE "PRESSING OF THE BUTTONS ACTION"
# AFTER ALL CONDITIONS ARE CHECKED TO PLACE THE BET AND CALCULATE IF IT DOES HAVE TO
# INCREASE THE MONEY THAT HAVE TO BE PLACED ON A BET OR CO REVERSE TO THE "BASE"
# FOR NOW THIS COME SECOND ORDER OF IMPORTANCE DUE TO THE FACT THE WE WANT TO TEST
# THE HYPOTHESIS FIRST


def race_to_start():
    jockey_names = WebDriverWait(driver, 30).until(ec.presence_of_all_elements_located((By.CLASS_NAME, "name")))
    jockey_names_list = []
    for jockey in jockey_names:
        jokey_01 = jockey.text
        jockey_names_list.append(jokey_01)

    combined = WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.CLASS_NAME, "total-matched")))
    event_money = combined.text
    event_money_int = int(event_money.split()[1].replace(',', ''))

    if event_money_int > 5000:
        venue_name = WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.CLASS_NAME, "venue-name")))
        venue_name_final = venue_name.text

        venue_date = WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.CLASS_NAME, "event-date")))
        venue_date_final = venue_date.text
        venue_date_final01 = venue_date_final[3:]
        # print(venue_date_final01)

        venue_time = venue_name_final.split()[0]
        venue_time_final = datetime.datetime.strptime(venue_time, '%H:%M').time()
        # print(venue_time_final)

        # print(type(venue_time))

        venue_name_final01 = str(venue_name_final.split()[1:-1])
        venue_name_final02 = (' '.join(ast.literal_eval(venue_name_final01)))
        # print(venue_name_final02)
        # print(type(venue_name_final01))

        venue_country = str(venue_name_final.split()[-1]).strip("()")
        # print(venue_country)

        venue_total_sum = event_money_int
        # print(venue_total_sum)

        jockey_names = WebDriverWait(driver, 30).until(ec.presence_of_all_elements_located((By.CLASS_NAME, "name")))

        # pro_quote01 = '//*[@id="main-wrapper"]/div/div[2]/div/ui-view/div/div/div[1]/div[3]/div/div[1]/div/bf-main-market/bf-main-marketview/div/div[
        # '2]/bf-marketview-runners-list[' \ '2]/div/div/div/table/tbody/tr[' pro_quote02 = ']/td[4]/button/div/span[1]'

        against_quote01 = '//*[@id="main-wrapper"]/div/div[2]/div/ui-view/div/div/div[1]/div[3]/div/div[1]/div/bf-main-market/bf-main-marketview/div/div[' \
                          '2]/bf-marketview-runners-list[' \
                          '2]/div/div/div/table/tbody/tr['
        against_quote02 = ']/td[5]/button/div/span[1]'

        quotes_final_against = []

        try:
            for jockey_place in range(len(jockey_names)):
                jokey = jockey_names[jockey_place]

                # pro_q = pro_quote01 + str(jockey_place + 1) + pro_quote02
                against_q = against_quote01 + str(jockey_place + 1) + against_quote02

                # quotes = WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.XPATH, pro_q)))
                quotes01 = WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.XPATH, against_q)))

                # print(jokey.text)
                # print(quotes.text)
                quotes_final_against.append(float(quotes01.text))
                # print(quotes01.text)

        except:
            'TimeoutException'

        # print(quotes_final_against)
        favorite_index = min(quotes_final_against)
        # print(favorite_index)

        favorite_jokey_name = jockey_names_list[quotes_final_against.index(favorite_index)]
        # print(favorite_jokey_name)

        # Calling the Test function to write the event in Excel
        test(venue_date_final01, venue_time_final, venue_name_final02, venue_country,
             venue_total_sum, favorite_index, favorite_jokey_name)

    else:
        pass


# The function that verifies if the race is writen in Excel, if it isn't it writes it in
# Also here Should be the Betting button
def test(venue_date_final01, venue_time_final, venue_name_final02, venue_country,
         venue_total_sum, favorite_index, favorite_jokey_name):
    # print(venue_date_final01, venue_time_final, venue_name_final02, venue_country,
    #       venue_total_sum, favorite_index, favorite_jokey_name)

    # Load the Excel file and make it active
    workbook_name = 'data.xlsx'
    wb = load_workbook(workbook_name)
    ws = wb.active

    # Because openpyxl doesn't have a module that let you select last n rows
    # I have to get the length of the C column for which I subtract the rows
    # that have to be checked, in this case I got the last 7 rows
    col_c = ws['c']
    len_table = int(len(col_c))
    # print print(len_table - 5)
    fifth_row = int(len_table - 7)

    # I bring the values form the race_to_start function in a list so we can write them in Excel
    race_final_data = [venue_date_final01, venue_time_final, venue_name_final02, venue_country,
                       venue_total_sum, favorite_index, favorite_jokey_name]

    # Select the columns and rows to be checked
    row = ws.iter_rows(min_row=fifth_row, max_row=len_table, min_col=2, max_col=3)

    # Create an empty list of the last rows from Excel to be able to compare the item
    excel_last_rows = []

    for a, b in row:
        excel_last_rows.append([a.value, b.value])

    # The button that will place the bet will be in this condition as well
    if [venue_time_final, venue_name_final02] not in excel_last_rows:
        # print(venue_time_final, venue_name_final02)
        ws.append(race_final_data)

    wb.save(filename=workbook_name)


# while True:
try:
    for race in race_link:
        driver.get(race)
        race_status = WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.CLASS_NAME, "market-status-label")))
        if race_status.text == "Intră în desfăşurare":
            race_to_start()
            # csv_write()
        elif race_status.text == 'Închis':
            race_finished()
        elif race_status.text == "În desfăşurare":
            pass

except:
    'TimeoutException'

    # x += 1
driver.quit()
