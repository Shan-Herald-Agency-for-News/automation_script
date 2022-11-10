# -*- coding: utf-8 -*-

import facebook
import json


token = {""}
graph = facebook.GraphAPI(shan_token)

posts_count = 0

def main():
    get_data(['id', 'title'])

def get_data(fields):
    id = 'shannews'
    data = graph.get_object(id, fields=fields)
    posts_count = posts_count + data['summary']['total_count']
    print(data['paging']['next'])


if __name__ == "__main__":
    main()

