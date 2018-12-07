# -*- coding: utf-8 -*-

from workflow import Workflow3
import json
import sys
import time

reload(sys)
sys.setdefaultencoding('utf8')

ICON_DEFAULT = 'icon.png'

def save_history_data(query, title, arg):
    jsonData = '{"title": "%s", "subtitle": "%s", "arg": "%s", \
        "icon": "%s"}\n' % (query, title, arg, ICON_DEFAULT)
    with open('history.log', 'a') as file:
        file.write(jsonData)


def get_history_data():
    with open('history.log', 'r') as file:
        for line in file.readlines()[-1:-10:-1]:
            line = json.loads(line)
            wf.add_item(
                title=line['title'], subtitle=line['subtitle'],
                arg=line['arg'], valid=True, icon=line['icon'])

def main(wf):
    query = wf.args[0]
    if not isinstance(query, unicode):
        query = query.decode('utf8')

    if not query:
        wf.send_feedback()

    if query == "*":
        get_history_data()
    else:
        title = convert(query)
        subtitle = 'convert(' + query + ') result: '
        arg = [query, title, query, '', '']
        arg = '$%'.join(arg)
        save_history_data(query, title, arg)
        wf.add_item(
            title=title, subtitle=subtitle, arg=arg,
            valid=True, icon=ICON_DEFAULT)
    
    wf.send_feedback()

def convert(query):
    if query == 'now' or query == '':
        return str(int(time.time()))
    elif is_numeric(query):
        localtime = time.localtime(float(query))
        return str(time.strftime('%Y-%m-%d %H:%M:%S', localtime))
    else:
        return str(int(time.mktime(time.strptime(query, "%Y-%m-%d %H:%M:%S"))))

def is_numeric(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False


if __name__ == '__main__':
    wf = Workflow3(update_settings={
        'github_slug': 'nefeed/nefeed.workflows.timestamp',
        'frequency': 7
    })
    sys.exit(wf.run(main))