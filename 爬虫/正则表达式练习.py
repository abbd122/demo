import re

line_list = [
    'XXX出生于2001年6月1日',
    'XXX出生于2001/6/1',
    'XXX出生于2001-6-1',
    'XXX出生于2001-06-01',
    'XXX出生于2001-06',
]

regex_str = r'.*?出生于(\d{4}[年/-]\d{1,2}([月/-]\d{1,2}\w{1}|[月/-]\d{1,2}|$))'

for line in line_list:
    match_obj = re.match(regex_str, line)
    if match_obj:
        print(match_obj.group(1))
    else:
        print('num {} no match'.format(line_list.index(line) + 1))

'''
result:
2001年6月1日
2001/6/1
2001-6-1
2001-06-01
2001-06
'''