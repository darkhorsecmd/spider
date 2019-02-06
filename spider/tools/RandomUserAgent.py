from fake_useragent import UserAgent


class RandomUserAgent():
    def __init__(self):
        self.ua = UserAgent(verify_ssl=False)

    def get_RanDomAgent(self):
       return self.ua.random



if __name__ == '__main__':
    userAgent = RandomUserAgent()
    print(type(userAgent.get_RanDomAgent()))