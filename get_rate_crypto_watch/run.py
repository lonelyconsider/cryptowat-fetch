from scrapy import cmdline
from zimbrasmtp import SmtpServer

try:
    cmdline.execute(['scrapy', 'crawl', 'cwSpider'])
except Exception as e:
    print(e)
    smtp = SmtpServer()
    smtp.send_mail(subject='CryptoWat-Remind', message='The data could not be get now, please check the API calls and DB setting.')
    exit()
