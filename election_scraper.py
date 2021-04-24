import csv
import sys

import requests
from bs4 import BeautifulSoup
import re




def check_args():
    if len(sys.argv) == 3:  #Checking for the right number of arguments
        return True
    else:
        print('Wrong number of arguments!')
        return False

def check_url(url):
    split_url = str(url).split('/')
    if split_url[0] == 'https:' and split_url[2] == 'volby.cz' and split_url[3] == 'pls' and split_url[4] == 'ps2017nss':
        return True
    else:
        print('Unexpected url!')
        return False

def get_response(url):
    r = requests.get(url)
    if r.status_code != 200:
        print(f'Error {r.status_code}')
        return None

    with requests.Session() as s:
        return s.get(url)

def extract_data(response):
    return BeautifulSoup(response.text, "html.parser")

def find_tables(soup):
    return soup.find_all('table')

def extract_dis_data(tables):
    dis_data = []  #district data
    print('Extracting data...')

    for table in tables:
        rows = table.find_all("tr")[2:]

        for row in rows:
            if row.find("td").text == "-":
                continue

            mun_data = {"code": "", "name": "", "registered": 0, "envelopes": 0, "valid": 0}  #municipality data
            mun_poli_data = {}

            mun_data["code"] = row.find("a").text
            mun_data["name"] = row.a.findNext("td").text
            dis_data.append(mun_data)

            mun_url = f"https://volby.cz/pls/ps2017nss/{row.find('a')['href']}"

            mun_response = get_response(mun_url)
            mun_soup = extract_data(mun_response)

            mun_data["registered"] = mun_soup.find('td', headers='sa2').text.replace('\u00a0', '')  #remove unbreakable spaces
            mun_data["envelopes"] = mun_soup.find('td', headers='sa3').text.replace('\u00a0', '')
            mun_data["valid"] = mun_soup.find('td', headers='sa6').text.replace('\u00a0', '')

            poli_names = mun_soup.find_all('td', headers=re.compile(r'^t\w+sb2$'))  #attribute whose value begins with 't' and ends with 'sb2'
            poli_votes = mun_soup.find_all('td', headers=re.compile(r'^t\w+sb3$'))
            for i in range(len(poli_names)):
                if poli_names[i].text != '-':
                    mun_poli_data[poli_names[i].text] = poli_votes[i].text.replace('\u00a0', '')

            mun_data["political parties"] = mun_poli_data

    return dis_data


def create_csv(data, file_name):
    print('Creating a CSV file...')

    poli_names = []
    for mun in data:
        for party in mun["political parties"].keys():
            if party not in poli_names:
                poli_names.append(party)

    with open(str(file_name) + '.csv', 'a+', newline='', encoding='utf-8-sig') as file:  #utf bom
        header = ['CODE', 'NAME', 'REGISTERED', 'ENVELOPES', 'VALID'] + poli_names
        writer = csv.writer(file, dialect='excel')
        writer.writerow(header)

        for mun_info in data:
            line = [mun_info["code"], mun_info["name"], mun_info["registered"], mun_info["envelopes"], mun_info["valid"]]
            for party in poli_names:
                pol_vote = mun_info["political parties"].get(party)
                if pol_vote is None:
                    line.append('-')
                else:
                    line.append(pol_vote)

            writer.writerow(line)

    file.close()


def el_scraper():
    print('2017 Election Results Scraper')

    if not check_args():
        print('Exiting...')
        exit()

    url = sys.argv[1]
    file_name = sys.argv[2]

    if not check_url(url):
        print('Exiting...')
        exit()

    response = get_response(url)

    if response is None:
        print('Exiting...')
        exit()

    soup = extract_data(response)
    tables = find_tables(soup)
    data = extract_dis_data(tables)

    if len(data) == 0:
        print('No data extracted. Have you input the correct link?')
        print('Exiting...')
        exit()

    create_csv(data, file_name)

    print(f'Results have been successfully saved to {file_name}.csv')

if __name__ == '__main__':
    el_scraper()

