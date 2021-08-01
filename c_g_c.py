import regex
import requests
import pyfiglet
from bs4 import BeautifulSoup

print('#'*71)
print(pyfiglet.figlet_format('Currency gold coin prices', font='slant'))
print('Made by Ali Hosseinverdi')
print('#'*71)

def results():
        user = input('\nWhat currency(or coin or gold) do you want to know the price ?(write "table" for show the table) :\n')
    
        site = requests.get("https://api.sunnyweb.ir/arz")
        text = site.text

        bs = BeautifulSoup(text, 'html.parser')

        table = bs.findAll('table', {'class':'table table-striped'})
        table = str(table)

        table_2 = regex.findall('>\d+,?\.?\d*,?\.?\d*,?\.?\d+<', table)

        arz_dic = {
        'bitcoin' : table_2[0],
        'tala_24' : table_2[1],
        'eterium' : table_2[2],
        'tala_18' : table_2[3],
        'sekke_emami' : table_2[4],
        'pond_england' : table_2[5],
        'sekke_bahar' : table_2[6],
        'euro' : table_2[7],
        'sekke_nim' : table_2[8],
        'dollar_amrican' : table_2[9],
        'sekke_rob' : table_2[10],
        'dollar_canada' : table_2[11],
        'sekke_gerami' : table_2[12],
        'dollar_australia' : table_2[13],
        'sekke_mesghali' : table_2[14],
        'dollar_newziland' : table_2[15],
        'dollar_sangapour' : table_2[16],
        'dollar_hongkong' : table_2[17],
        'derham_emarat' : table_2[18],
        'lir_turkey' : table_2[19],
        'lir_sourya' : table_2[20],
        'yoan_chin' : table_2[21],
        'yen_japan' : table_2[22],
        'frank_sooeis' : table_2[23],
        'cron_sooed' : table_2[24],
        'cron_danmark' : table_2[25],
        'cron_norweg' : table_2[26],
        'dinar_aragh' : table_2[27],
        'dinar_bahrain' : table_2[28],
        'dinar_kowait' : table_2[29],
        'dinar_bahrain' : table_2[30],
        'rial_arabestan' : table_2[31],
        'rial_qatar' : table_2[32],
        'rial_omman' : table_2[33],
        'roopie_india' : table_2[34],
        'roopie_pakestan' : table_2[35],
        'afghani_afghanestan' : table_2[36],
        'ringet_malesya' : table_2[37],
        'bat_tahiland' : table_2[38],
        'dram_armenia' : table_2[39],
        'lary_gorjya' : table_2[40]
        }

        b = 0

        if user == 'table':
            for i in arz_dic.keys():
                print(i)


        for i in arz_dic.keys():
            if user == i:
                print(arz_dic.get(i))
                b = 1


        if b == 0:
            if user != 'table':
                print('The currency was not found !!!')

        again = input('\nDo you want to use again ?[y/n]: \n')

        if again == 'y' or again == 'Y':
            results()
        else:
            print('\n###Good Bye###')

results()
