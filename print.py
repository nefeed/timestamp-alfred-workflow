# -*- coding: utf-8 -*-
import sys
import os
from workflow import Workflow3

reload(sys)
sys.setdefaultencoding('utf8')


def getargs(wf):
    query = sys.argv[1]
    query = query.split('$%')
    part = int(sys.argv[2])
    if part == 0:
        # 原始数据
        sys.stdout.write(query[0].replace("\\","").strip())
    elif part == 1:
        # convert后的数据
        sys.stdout.write(query[1].replace("\\","").strip())


if __name__ == '__main__':
    wf = Workflow3()
    sys.exit(wf.run(getargs))
