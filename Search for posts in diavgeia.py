# 21.3 Tελική εργασία: Ανάκτηση δεδομένων από τη diavgeia.gov.gr
# Πρότυπο λύσης

import re
import urllib.request
import urllib.error
import csv

arxes = {}


def rss_feed(url):  # 3 μονάδες *
    '''
    Άνοιγμα του rss feed,
    :param url: η διεύθυνση του rss feed.
    Αυτή η συνάρτηση δημιουργεί ένα αρχείο
    με τα περιεχόμενα του rss_feed με όνομα
    την διεύθυνση του rss feed.
    Καλεί την συνάρτηση process_feed
    η οποία επιλέγει και τυπώνει περιεχόμενο
    Προσπαθήστε να κάνετε try/except τα exceptions
    HTTPError και URLError.
    '''
    # σύμφωνα με την ανακοίνωση της διαύγειας τα rss feeds είναι στο ίδιο url/rss
    url += r"/rss"
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read().decode()

        filename = "myRssFile.rss"
        with open(filename, "w", encoding="utf-8") as p:
            p.write(html)
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.readline())
        return 0
    except urllib.error.URLError as e:
        print(e)
        if hasattr(e, 'reason'):  # χωρίς σύνδεση ιντερνετ
            print('Αποτυχία σύνδεσης στον server')
            print('Αιτία: ', e.reason)
        return 0
    else:
        if (process_feed(filename)):
            return 1
        else:
            return 0


def process_date(date):  # 2 μονάδες
    '''
    η συνάρτηση διαμορφώνει την ελληνική ημερομηνία του rss feed:
    Στο rss αρχείο η ημερομηνία είναι της μορφής: Wed, 14 Jun 2017 17:21:16 GMT
    Θα πρέπει να διαμορφώνεται σε ελληνική ημερομηνία, πχ: Τετ, 14 Ιουν 2017
    :param date:
    :return: η ελληνική ημερομηνία
    '''
    months = {"Jan": "Ιαν", "Feb": "Φεβ", "Mar": "Μαρ", "Apr": "Απρ",
              "May": "Μαι", "Jun": "Ιουν", "Jul": "Ιουλ", "Aug": "Αυγ",
              "Sep": "Σεπ", "Oct": "Οκτ", "Nov": "Νοε", "Dec": "Δεκ"}
    days = {"Mon": "Δευ",
            "Tue": "Τρι",
            "Wed": "Τετ",
            "Thu": "Πεμ",
            "Fri": "Παρ",
            "Sat": "Σαβ",
            "Sun": "Κυρ"}

    stringDate = str(date[0])
    day = stringDate.split()[0].replace(',','')
    dayNumber = stringDate.split()[1]
    month = stringDate.split()[2]
    year = stringDate.split()[3]
    result = days[day] + ', ' + dayNumber + ' ' + months[month] + ' ' + year
    return result


def process_feed(filename):  # 3 μονάδες *
    '''
    συνάρτηση που ανοίγει το αρχείο με το rss feed και
    τυπώνει την ημερομηνία και τους τίτλους των αναρτήσεων που περιέχει.
    Xρησιμοποιήστε regular expressions
    '''

    with open(filename, 'r', encoding='utf-8') as f:
        rss = f.read().replace("\n", " ")
        feeds = []
        items = re.findall(r"<title>(.*?)</title>", rss, re.MULTILINE | re.IGNORECASE)
        date = re.findall(r"<lastBuildDate>(.*?)</lastBuildDate>", rss, re.MULTILINE | re.IGNORECASE)
        convertedDate = process_date(date)
        print(convertedDate, '\n')
        for index, item in enumerate(items):
            if index == 0:
                print('+++', item, '+++')
            else:
                print(index, ' ', item)


def search_arxes(arxh):  # 2 μονάδες
    '''
    Αναζήτηση ονόματος Αρχής που ταιριάζει στα κριτήρια του χρήστη
    '''
    results = []
    for key in arxes:
        if str(key).find(arxh.upper()) != -1:
            results.append(key)
    return results


def load_arxes():  # 2 μονάδες
    '''
    φορτώνει τις αρχές στο λεξικό arxes{}
    '''
    with open('500_arxes.csv', mode='r', encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        for index, row in enumerate(csv_reader):
            separator = ','
            currentString = separator.join(row)
            splittedRow = currentString.split(';')
            arxes[splittedRow[0]] = splittedRow[1]


######### main ###############
'''
το κυρίως πρόγραμμα διαχειρίζεται την αλληλεπίδραση με τον χρήστη
'''
load_arxes()
while True:
    arxh = input(50 * "^" + "\nΟΝΟΜΑ ΑΡΧΗΣ:(τουλάχιστον 3 χαρακτήρες), ? για λίστα:")
    if arxh == '':
        break
    elif arxh == "?":  # παρουσιάζει τα ονόματα των αρχών
        for k, v in arxes.items():
            print(k, v)
    elif len(arxh) >= 3:
        # αναζητάει όνομα αρχής που ταιριάζει στα κριτήρια του χρήστη
        result = search_arxes(arxh)
        for r in result:
            print(result.index(r) + 1, r, arxes[r])
        while result:
            epilogh = input("ΕΠΙΛΟΓΗ....")
            if epilogh == "":
                break
            elif epilogh.isdigit() and 0 < int(epilogh) < len(result) + 1:
                epilogh = int(epilogh)
                url = arxes[result[epilogh - 1]]
                print(url)
                # καλεί τη συνάρτηση που φορτώνει το αρχείο rss:
                rss_feed(url)
            else:
                continue
    else:
        continue
