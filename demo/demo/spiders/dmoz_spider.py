#encoding=utf-8
'''
Created on Dec 11, 2015

@author: sainty
'''
import logging
import scrapy
from demo.items import DemoItem
import sys  
import codecs
from scrapy.spiders import CrawlSpider,Rule
from scrapy.selector import Selector
#class DmozSpider(CrawlSpider):
class NUPTSpider(scrapy.Spider):
    reload(sys)  
    sys.setdefaultencoding('utf8')
    '''add XXX.log
    logger = logging.getLogger('mylogger')
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler('/home/mtbf3/NUPT.log')
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s-%(name)s-%(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)'''
    name = "intern_nupt"
    allowed_domains = ["njupt.91job.gov.cn"]
    start_urls = ["http://njupt.91job.gov.cn/job/search/d_category%5B0%5D/0/d_category%5B1%5D/101/d_category%5B2%5D/102"
,"http://njupt.91job.gov.cn/job/search?d_category[0]=0&d_category[1]=101&d_category[2]=102&page=2"]
    def parse(self,response):
	uls = response.xpath("//ul[@class='infoList']")
	page_num = 31
	for ul in uls:
		item = DemoItem() 
		item['intern_info'] = ''.join(ul.xpath(".//li[@class='span1']/a[@href]/text()").extract())
		item['intern_url'] = 'njupt.91job.gov.cn'+''.join(ul.xpath(".//li[@class='span1']/a/@href").extract())
		item['intern_company'] = ''.join(ul.xpath(".//li[@class='span2']/a/text()").extract())
		item['intern_location']= ''.join(ul.xpath(".//li[@class='span3']/text()").extract())
		item['intern_date'] = ''.join(ul.xpath(".//li[@class='span4']/text()").extract())
		yield item 
	for i in range(3,page_num):		
		next_page_url = "http://njupt.91job.gov.cn/job/search?d_category[0]=0&d_category[1]=101&d_category[2]=102&page="+str(i)
		yield scrapy.Request(next_page_url,callback = self.parse_info)

    def parse_info(self,response):
	uls = response.xpath("//ul[@class='infoList']")
	for ul in uls:
		item = DemoItem() 
		item['intern_info'] = ''.join(ul.xpath(".//li[@class='span1']/a[@href]/text()").extract())
		item['intern_url'] = 'njupt.91job.gov.cn'+''.join(ul.xpath(".//li[@class='span1']/a/@href").extract())
		item['intern_company'] = ''.join(ul.xpath(".//li[@class='span2']/a/text()").extract())
		item['intern_location']= ''.join(ul.xpath(".//li[@class='span3']/text()").extract())
		item['intern_date']= ''.join(ul.xpath(".//li[@class='span4']/text()").extract())
		yield item 

class NJUSpider(scrapy.Spider):
    reload(sys)  
    sys.setdefaultencoding('utf8')
    name = "intern_nju"
    allowed_domains = ["bbs.nju.edu.cn"]
    start_urls = ["http://bbs.nju.edu.cn/bbsdoc?board=JobExpress&start=11985&type=doc"]
    def parse(self,response):
	month_dict = {'Dec':'12','Nov':'11','Oct':'10','Sep':'9'}
    	page_num = 5
    	for i in range(1,20):
		item = DemoItem()
                intern_date = ''.join(Selector(response).xpath("//table[@width=670]/tr[2]/td[5]//nobr/text()")[i].extract())
		if intern_date.find('Dec') != -1 or intern_date.find('Nov') != -1:
#			print '--------------------------',intern_date
			month_list = []
			month_list = intern_date.split()
#			print '---------------------',month_list[0]
			Month = month_dict[month_list[0]]
			final_date = '2015-'+Month+'-'+month_list[1]
			item['intern_date'] = str(final_date)
		else:
			item['intern_date'] = intern_date	
		item['intern_info'] = ''.join(Selector(response).xpath("//table[@width=670]/tr[2]/td[5]/nobr//a[contains(@href,'bbscon')]/text()")[i].extract())
		item['intern_url'] = 'http://bbs.nju.edu.cn/'+''.join(Selector(response).xpath("//table[@width=670]/tr[2]/td[5]/nobr//a[contains(@href,'bbscon')]/@href")[i].extract())
		yield item
    	for i in range(1,page_num):
			num = 11985 - i*20		
			next_page_url = "http://bbs.nju.edu.cn/bbsdoc?board=JobExpress&start="+str(num)+"&type=doc"
#			print next_page_url 
			yield scrapy.Request(next_page_url,callback = self.parse_info)

    def parse_info(self,response):
	month_dict = {'Dec':'12','Nov':'11','Oct':'10','Sep':'9'}
    	for i in range(1,20):
		item = DemoItem()
        	intern_date = ''.join(Selector(response).xpath("//table[@width=670]/tr[2]/td[5]//nobr/text()")[i].extract())
		if intern_date.find('Dec') != -1 or intern_date.find('Nov') != -1 or intern_data.find('Sep') != -1 :
#			print '--------------------------',intern_date
			month_list = []
			month_list = intern_date.split()
#			print '---------------------',month_list[0]
			Month = month_dict[month_list[0]]
			if int(month_list[1]) < 10:
				final_date = '2015-'+Month+'-0'+month_list[1]				
			else:
				final_date = '2015-'+Month+'-'+month_list[1]
			item['intern_date'] = str(final_date)
		else:
			item['intern_date'] = intern_date
		item['intern_info'] = ''.join(Selector(response).xpath("//table[@width=670]/tr[2]/td[5]/nobr//a[contains(@href,'bbscon')]/text()")[i].extract())
		item['intern_url'] = 'http://bbs.nju.edu.cn/'+''.join(Selector(response).xpath("//table[@width=670]/tr[2]/td[5]/nobr//a[contains(@href,'bbscon')]/@href")[i].extract())
		yield item
		

















