#! /usr/bin/python
# -*- coding: utf-8 -*-

import datetime
from pelican import signals
import os
import urllib.request

def load_csv(generator):

    # dirname = os.path.dirname(os.path.abspath(__file__))
    # filepath = os.path.join(dirname, 'concerts.csv')
    # with open(filepath, 'r', encoding='utf-8') as f:
    #    doc = f.read()

    data = urllib.request.urlopen("https://raw.githubusercontent.com/organic-jukebox/concert-archive/master/concerts.csv").read(50000)
    doc = data.decode("utf-8")
    csv_list = filter(None, doc.split('\n'))
    data = []

    for i, row in enumerate(csv_list):

        row_dict = dict()
        row_data = row.split(';')
        # print(row_data[1].encode('ascii', 'ignore'))
        date_ints = row_data[0].split("-")
        date = datetime.date(int(date_ints[0]), int(date_ints[1]), int(date_ints[2]))
        row_dict['date'] = date

        row_dict['country'] = row_data[1]
        row_dict['city'] = row_data[2]
        row_dict['venue'] = row_data[3]
        row_dict['band'] = row_data[4]
        row_dict['text'] = row_data[5]
        row_dict['tags'] = row_data[6].split(',')
        visible = row_data[7] != 'false'
        # print(row_dict['band'].encode('ascii', 'ignore'))

        if visible:
            data.append(row_dict)

    data = sorted(data, key=lambda concert: concert['date'])
    upcoming = [concert for concert in data if concert['date'] >= datetime.date.today()]
    archived = [concert for concert in data if concert['date'] < datetime.date.today()]
    archived.reverse()

    def filtered(data2):

        def new_filtered(*args, exclude=False):
            tags = args
            if isinstance(tags, str):
                tags = [tags]
            data3 = []
            for row in data2:
                match = False
                if tags:
                    for tag in row['tags']:
                        for intag in tags:
                            if exclude:
                                match = True
                                if tag == intag:
                                    match = False
                            else:
                                if tag == intag:
                                    match = True
                else:
                    match = True
                if match:
                    data3.append(row)
            return data3
        return new_filtered

    generator.context['concerts_upcoming'] = filtered(upcoming)
    generator.context['concerts_archive'] = filtered(archived)


def register():
    signals.generator_init.connect(load_csv)
