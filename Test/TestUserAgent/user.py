from fake_useragent import UserAgent
ua = UserAgent(verify_ssl=False)
print(ua.random)