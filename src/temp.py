# -*- coding: utf-8 -*-

from utils import get_soup


url = 'https://caibaoshuo.com/cn_industries/309'
div = get_soup(url).find('div', {'class': 'fullscreen-body'})
tds=div.find('tbody').find_all('td', {'class': 'company-name-td'})

codes=[]
for td in tds:
    obj={
        'name': td.find('a').text,
        'code': td.find('span').text
    }
    codes.append(obj)
print(codes)