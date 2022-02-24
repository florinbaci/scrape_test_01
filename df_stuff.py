import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import re

# Setting up the environment and getting the web page raddy to scrap
driver = webdriver.Chrome('C:/Users/User/AppData/Local/Programs/Python/Python38/Scripts/chromedriver.exe')
driver.maximize_window()

df = pd.read_excel('data_df.xlsx')
# df_tail = df.tail(15)

for i, row in df.iterrows():
    url = row[7]
    driver.get(url)

    jockey_names = WebDriverWait(driver, 30).until(ec.presence_of_all_elements_located((By.CLASS_NAME, "name")))
    # print(jockey_names)

    # race_to_check = []
    # favorite = []

    #
    # def race_finished():
    jockey_names = WebDriverWait(driver, 30).until(ec.presence_of_all_elements_located((By.CLASS_NAME, "name")))
    jockey_names_list = []
    for jockey in jockey_names:
        jokey_01 = jockey.text
        jockey_names_list.append(jokey_01)
        race_winner = WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.CLASS_NAME, "runner-winner")))
        race_win01: str = '//*[@id="main-wrapper"]/div/div[2]/div/ui-view/div/div/div[1]/div[3]/div/div[' \
                          '1]/div/bf-main-market/bf-main-marketview/div/div[2]/bf-marketview-runners-list[' \
                          '2]/div/div/div/table/tbody/tr['
        race_win02: str = ']/td/div[1]/div[2]/div'

    num_of_jockeys_in_race = len(jockey_names)
    print(num_of_jockeys_in_race)

    # print(len(jockey_names_list))
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

    winner_final = jockey_names_list[int(position_final[0])]
    winner_final_01 = re.sub('\d*\.*\s', '', winner_final)
    # winner_final_02 = re.findall('[A-Z][^A-Z]*', winner_final_01)
    winner_final_02 = re.sub(r'([A-Z])', r' \1', winner_final_01).split()
    winner_final_03 = ' '.join([str(elem) for elem in winner_final_02])
    print(winner_final_03)

    print(i, row[6], row[7])
    print('\n')

    if winner_final_03[:5] in row[6]:
        # df.at[i, "Win_Lost"] = 0
        # df.at[i, "Winner_jockey"] = 'johny'
        # df.at[i, "No_of_jockeys"] = num_of_jockeys_in_race

        df.loc[i, ["Win_Lost", "Winner_jockey"]] = [0, winner_final_03]
        print('is in')
    else:
        df.loc[i, ["Win_Lost", "Winner_jockey"]] = [1, winner_final_03]
        # df.at[i, "Win_Lost"] = 1
        # df.at[i, "No_of_jockeys"] = num_of_jockeys_in_race
        # df.at[i, "Winner_jockey"] = 'boby'

        print('not in')

    df.to_excel('data_df01.xlsx')
# print(df_tail)

driver.quit()
