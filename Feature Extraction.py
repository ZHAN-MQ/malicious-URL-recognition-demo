import re
import csv
import string
from collections import namedtuple

def url_extract(u):
	if (re.match(r'^https.', u)) == None:
		u = u[7:]
	else:
		u = u[8:]
	return u

def lenth(u):
	return len(u)

def dots_count(u):
	return u.count('.')

def url_split(u):
	return re.split(r'[/.]', u)

def lenth_of_primary_domain(u):
	u = u.split('/')
	l = len(u[0])
	return l

def contain_IP(u):
	if (re.match(r'^\d{1,3}', u)) == None:
		return 0
	else:
		return 1

def avg_word_lenth(u):
	e = re.split(r'[/.]', u)
	i = len(e)
	t = 0
	sum = 0
	avg = 0
	while t < i :
		l = len(e[t])
		sum += l
		t += 1
	avg = sum/i
	return avg

def longest_word_lenth(u):
	e = re.split(r'[/.]', u)
	i = len(e)
	t = 0
	longest = 0
	while t < i:
		l = len(e[t])
		if l > longest:
			longest = l
		t += 1
	return longest

def special_character_count(u):
	count = 0
	for c in u:
		if c in string.ascii_letters:
			continue
		elif c.isdigit():
			continue
		else:
			count += 1
	count = count - u.count('.') - u.count('/')
	return count


with open('traindata-2.csv') as f:
	with open('result.txt', 'w') as w:
		w.writelines('lenth_of_url' + ',' + 'lenth_of_primary_domain' + ',' +
			   'number_of_dots' + ',' + 'contain_IP' + ',' + 'avg_word_lenth' + ',' +
			   'longest_word_length' + ',' + 'special_character_count' + ',' + 'result' + '\n')
		f_csv = csv.reader(f)
		headers = next(f_csv)
		Row = namedtuple('Row', headers)
		for r in f_csv:
			row = Row(*r)
			u = url_extract(row.url)

			l_url = lenth(u)
			l_domain = lenth_of_primary_domain(u)
			dots = dots_count(u)
			IP = contain_IP(u)
			avg = avg_word_lenth(u)
			longest = longest_word_lenth(u)
			special_character = special_character_count(u)

			w.writelines(str(l_url) + ',' + str(l_domain) + ',' + 
				str(dots) + ',' +str(IP) + ',' + 
				str(avg) + ',' + str(longest) + ',' + str(special_character) + ',' + str(row.result) + '\n')