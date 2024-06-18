"""
File: webcrawler.py
Name: Zoe
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names' + year + '.html'

        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #
        total_m = 0                                             # number of male babies in total
        total_f = 0                                             # number of female babies in total
        data = soup.tbody.text                                  # get the data
        tokens = data.split()                                   # split the data with blank space

        for i in range(len(tokens)):
            if i > 999:                                         # only the top 999 data is useful
                break
            else:
                if i % 5 == 2:                                  # the number of male babies with the specific name
                    final = int(tokens[i].replace(',', ''))
                    total_m += final                            # add the numbers to total_m

                elif i % 5 == 4:                                # the number of female babies with the specific name
                    final = int(tokens[i].replace(',', ''))
                    total_f += final                            # add the numbers to total_f

        print(f"Male Number: {total_m}")
        print(f"Female Number: {total_f}")


if __name__ == '__main__':
    main()
