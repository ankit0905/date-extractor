#!/usr/bin/python3
# -*- coding: utf-8 -*-
import datetime
import re
from nltk import ngrams
from nltk.tokenize import wordpunct_tokenize

days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "weekend"]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
words = {"today": 0, "tomorrow": 1, "yesterday": -1, "day before yesterday": -2, "day after tomorrow": 2}
prefix = {"this": 0, "coming": 0, "last": 1, "previous": 1, "next": 2}
words_s = ["today", "tomorrow", "yesterday", "day before yesterday", "day after tomorrow"]
prefix_s = ["this", "coming", "last", "previous", "next"]


class CustomDate:
	""" Custom Date class which converts a valid user input
		to DD-MM-YYYY format date.
	"""

	def __init__(self, user_input):
		self.user_input = user_input.lower().replace("weekend", "saturday")
		self.output_date = datetime.datetime.today()
		self.date = -1
		self.month = -1
		self.year = datetime.datetime.now().year
		self.errors = ""
		if not any(char.isdigit() for char in self.user_input):
			self.getDate()
		else:
			self.convert()
		self.output_date = self.output_date.strftime('%d-%m-%Y')
		# print(self.user_input, self.output_date, self.errors)

	def convert(self):
		""" Converts a given date to DD-MM-YYYY format
		"""
		date_list = re.split(r'[-. ,/|\'\\]+', self.user_input)
		date_list = [x for x in date_list if x]
		didx, midx = 0, 1
		if not date_list[0][0].isnumeric():
			didx, midx = 1, 0
		self.date = int(re.sub('[^0-9]', '', date_list[didx]))
		if len(date_list) > 1:
			if date_list[midx].isnumeric():
				self.month = int(date_list[midx])
			else:
				for it in range(len(months)):
					if months[it].lower().startswith(date_list[midx].lstrip("0").lower()):
						self.month = it + 1
						break
			try:
				self.year = int(date_list[2])
			except Exception:
				self.year = datetime.datetime.now().year
		else:
			self.month = datetime.datetime.now().month
		self.output_date = datetime.date(self.year, self.month, self.date)

	def getDate(self):
		""" Converts keywords like "next monday", "this monday", "weekend" etc. into a valid date

		"""
		if self.user_input in words:
			delta = words[self.user_input]
			self.output_date += datetime.timedelta(delta)
		else:
			inp = self.user_input.split()
			if len(inp) == 1:
				if self.user_input in days:
					self.output_date = self.next_weekday(self.output_date, days.index(self.user_input))
				else:
					self.errors = "Invalid Input"
			elif len(inp) > 2:
				self.errors = "Invalid Input"
			else:
				if prefix[inp[0]] == 0:
					self.output_date = self.next_weekday(self.output_date, days.index(inp[1]))
				elif prefix[inp[0]] == 1:
					self.output_date = self.previous_weekday(self.output_date, days.index(inp[1]))
				else:
					self.output_date = self.next_weekday(self.output_date, days.index(inp[1]))
					if days[datetime.datetime.today().weekday()] != inp[1]:
						self.output_date = self.next_weekday(self.output_date, days.index(inp[1]))

	def next_weekday(self, d, weekday):
		""" Gets the date of coming weekday

			d: initial date
			weekday: index of the weekday
		"""
		days_ahead = weekday - d.weekday()
		if days_ahead <= 0:  # Target day already happened this week
			days_ahead += 7
		return d + datetime.timedelta(days_ahead)

	def previous_weekday(self, d, weekday):
		""" Gets the date of last weekday

			d:  initial date
			weekday: index of the weekday
		"""
		days_ahead = weekday - d.weekday()
		if days_ahead >= 0:  # Target day already happened this week
			days_ahead -= 7
		return d + datetime.timedelta(days_ahead)


if __name__ == '__main__':
	user_input = input("Enter Input: ")
	user_input.replace(',', " ")
	user_input = user_input.split()
	user_input = [word for word in user_input if word != "of"]
	query = list()
	dates = list()
	if len(user_input) < 3:
		query.append(" ".join(user_input))
	else:
		tokens = wordpunct_tokenize(" ".join(user_input))
		query = [" ".join(word) for word in ngrams(tokens, 1)]
		query += [" ".join(word) for word in ngrams(tokens, 2)]
		query += [" ".join(word) for word in ngrams(tokens, 3)]
		query.sort(key=len, reverse=True)
	while len(query) > 0:
		try:
			keyword = query[0]
			d = CustomDate(keyword)
			if d.output_date not in dates and d.errors != "Invalid Input":
				temp, curr = wordpunct_tokenize(keyword), []
				if len(temp) > 1:
					curr = [" ".join(word) for word in ngrams(temp, 1)]
				if len(temp) > 2:
					curr += [" ".join(word) for word in ngrams(temp, 2)]
				for ele in curr:
					if ele in query:
						query.remove(ele)
				dates.append(d.output_date)
				print(keyword, " => ", d.output_date)
				# break
			query.remove(keyword)
		except Exception:
			query.remove(keyword)

'''
Coded by:

Saurabh Aggarwal
Ankit Anand
Hitesh Sagtani

(Interns at ValueFirst Digital Media, Gurgaon)
PRACTICE SCHOOL - 1 Project
'''