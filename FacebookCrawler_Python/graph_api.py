# -*- coding: utf-8 -*-

import facebook
import json

token = {'EAAIHErrxSpkBAIE7NWvagLgZAPNuQchaLKvPEs2LGgROZAftBFwH6eFLC3bSctraq9rXmZCWdgPUnoISHMAVl2F9WXASRB8XdEnrQgDtV4yKoB0eK3WvKmYtNNmOLZBsvh6gkONN9xo427FSUqSjLdHGXEmI4wJun88C4u0JsyxnSSe0UzHen0KZAGHFaQ7LGfOmuwb6tg3C6ZCRnOesFJGQgLPBJ7RMcZD'}
graph = facebook.GraphAPI(token)

def main():
    get_data(['id', 'title'])

def get_data(fields):
    id = 'shannews/live_videos'
    data = graph.get_object(id, fields=fields)
    print(data['paging']['next'])


if __name__ == "__main__":
    main()

