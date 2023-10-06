
from typing import Dict, List

from models.typosquat import TypoSquat
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

RESULT = '0aypal.com 134.119.176.30 ✖\noaypal.com 185.107.56.204 ✖\nraypal.com 164.90.244.158 ✖\naypal.com 103.224.182.246 ✔\npaypal.com 64.4.250.37 ✔\npay6pal.com 103.224.182.246 ✔\npay0al.com 134.119.176.28 ✖\nƥaypal.com\n(xn--aypal-ipb.com)\n99.83.176.46 ✖\nqaypal.com 172.67.144.126 ✔\nƿaypal.com\n(xn--aypal-ytb.com)\n99.83.176.46 ✖\nṗaypal.com\n(xn--aypal-to1b.com)\n99.83.176.46 ✖\nmaypal.com 43.128.7.87 ✖\npaypoal.com 64.190.63.111 ✔\npayoal.com 95.211.75.16 ✖\npaylal.com 93.115.28.104 ✖\npayppal.com 3.33.139.32 ✔\npaypalm.com 3.64.163.50 ✖\npaypaɫ.com\n(xn--paypa-loc.com)\n99.83.176.46 ✖\npaypaol.com 199.59.243.225 ✖\npaypa1.com 3.33.139.32 ✔\npaypao.com 199.59.243.225 ✖\npaypak.com 103.224.182.241 ✔\npaypapl.com 199.59.243.225 ✖\npaypaly.com 3.33.139.32 ✖\npaypap.com 199.59.243.225 ✖\npaypa-l.com 160.124.19.145 ✖\npaypakl.com 185.107.56.59 ✔\npaypalx.com 3.33.139.32 ✔\npaypals.com 99.83.176.46 ✖\npaypalp.com 103.224.182.246 ✔\npaypalv.com 91.195.240.12 ✔\npaypad.com 18.160.41.33 ✖\npaypan.com 159.89.244.183 ✖\npaypał.com\n(xn--paypa-o7a.com)\n162.255.119.200 ✔\npaypah.com 3.223.247.119 ✖\npaypall.com 3.33.139.32 ✖\npaypalt.com 13.248.169.48 ✖\npaypali.com 164.90.244.158 ✖\npaypam.com 15.197.142.173 ✔\npaypalz.com 156.245.52.218 ✖\npaypalk.com 185.107.56.205 ✖\npaypale.com 103.224.182.246 ✔\npaypalf.com 15.197.142.173 ✖\npaypalq.com 3.13.126.129 ✖\npaypsl.com 64.190.63.111 ✔\npaypaal.com 3.33.139.32 ✔\npaypzl.com 93.115.28.104 ✖\npaypyal.com 99.83.176.46 ✖\npaypol.com 103.224.182.245 ✔\npaypalo.com 185.53.177.53 ✔\npaypala.com 185.53.178.50 ✔\npaypsal.com 103.224.182.246 ✔\npaypazl.com 199.59.243.225 ✖\npaypayl.com 134.119.176.23 ✖\npaypawl.com 15.197.142.173 ✖\npaypul.com 78.41.204.32 ✖\npaypqal.com 103.224.182.246 ✔\npaypȧl.com\n(xn--paypl-wcc.com)\n99.83.176.46 ✖\npaypăl.com\n(xn--paypl-uwa.com)\n99.83.176.46 ✖\npaypǎl.com\n(xn--paypl-nwb.com)\n99.83.176.46 ✖\npaypaql.com 185.107.56.203 ✖\npaypla.com 104.21.83.78 ✔\npaypạl.com\n(xn--paypl-m11b.com)\n99.83.176.46 ✖\npaypãl.com\n(xn--paypl-dra.com)\n99.83.176.46 ✖\npaypâl.com\n(xn--paypl-6qa.com)\n99.83.176.46 ✖\npaypäl.com\n(xn--paypl-jra.com)\n99.83.176.46 ✖\npaypál.com\n(xn--paypl-0qa.com)\n99.83.176.46 ✖\npaypàl.com\n(xn--paypl-uqa.com)\n99.83.176.46 ✖\npaypwl.com 162.210.199.87 ✖\npaypql.com 93.115.28.104 ✖\npayp1al.com 45.76.28.55 ✔\npaypel.com 185.107.56.204 ✖\npaypil.com 185.53.177.53 ✔\npayapl.com 185.107.56.205 ✖\npaypl.com 64.98.135.58 ✔\npayp-al.com 103.224.212.225 ✔\npayopal.com 185.107.56.204 ✖\npaypwal.com 156.237.192.92 ✖\npayp0al.com 103.224.182.246 ✔\npayṗal.com\n(xn--payal-wo1b.com)\n99.83.176.46 ✖\npayƥal.com\n(xn--payal-lpb.com)\n99.83.176.46 ✖\npayƿal.com\n(xn--payal-1tb.com)\n99.83.176.46 ✖\npaypål.com\n(xn--paypl-pra.com)\n109.235.174.20 ✖\npaymal.com 91.195.240.101 ✔\npayxal.com 3.64.163.50 ✖\npaytal.com 199.59.243.225 ✖\npayral.com 3.64.163.50 ✖\npaypcl.com 38.36.225.11 ✖\npayplal.com 103.224.182.232 ✔\npayal.com 66.81.203.11 ✖\npa6pal.com 199.59.243.225 ✖\npaypasl.com 45.33.20.235 ✖\npatpal.com 185.107.56.203 ✖\npay.pal.com 64.99.64.37 ✖\npagpal.com 13.248.169.48 ✔\npa.ypal.com 103.224.182.246 ✔\npahpal.com 99.83.176.46 ✖\npaspal.com 3.64.163.50 ✖\npaupal.com 93.115.28.104 ✖\npa6ypal.com 103.224.182.246 ✔\npay-pal.com 216.21.239.197 ✖\npaylpal.com 67.227.226.240 ✔\npatypal.com 103.224.182.246 ✔\npapyal.com 162.210.196.168 ✔\npaytpal.com 103.224.182.251 ✔\npaapal.com 5.79.79.210 ✖\npagypal.com 154.197.182.108 ✖\npayqal.com 207.148.248.143 ✖\npayhpal.com 103.224.182.252 ✔\npapal.com 198.23.51.117 ✔\npayspal.com ✖ ✔\npa7pal.com 52.33.207.7 ✖\npa-ypal.com 15.197.142.173 ✖\npaẏpal.com\n(xn--papal-hy1b.com)\n99.83.176.46 ✖\npayxpal.com 104.143.9.211 ✖\npaxypal.com 44.230.85.241 ✖\npaȳpal.com\n(xn--papal-wec.com)\n99.83.176.46 ✖\npauypal.com 91.195.240.40 ✖\npaÿpal.com\n(xn--papal-3va.com)\n99.83.176.46 ✖\npaʏpal.com\n(xn--papal-ouc.com)\n99.83.176.46 ✖\npahypal.com 77.247.182.242 ✖\npaýpal.com\n(xn--papal-rva.com)\n99.83.176.46 ✖\npa9pal.com 99.83.176.46 ✖\npaipal.com 3.33.139.32 ✔\npyapal.com 64.190.63.111 ✔\npuypal.com 199.59.243.225 ✖\npaxpal.com 185.53.177.53 ✔\npay7pal.com 44.227.76.166 ✔\np.aypal.com 103.224.182.246 ✔\npaygpal.com 45.39.143.136 ✖\npzypal.com 64.190.63.111 ✔\npwypal.com 93.115.28.104 ✖\npaaypal.com 3.33.139.32 ✔\npayupal.com 67.225.218.6 ✔\npa7ypal.com 44.227.76.166 ✔\npayapal.com 72.14.185.43 ✔\npayypal.com 3.33.139.32 ✔\npsaypal.com 3.64.163.50 ✖\npzaypal.com 185.53.178.50 ✔\npasypal.com 103.224.182.251 ✔\npwaypal.com 93.115.28.104 ✖\npąypal.com\n(xn--pypal-3wa.com)\n99.83.176.46 ✖\npȧypal.com\n(xn--pypal-tcc.com)\n99.83.176.46 ✖\npypal.com 103.224.182.238 ✔\npăypal.com\n(xn--pypal-rwa.com)\n99.83.176.46 ✖\npǎypal.com\n(xn--pypal-kwb.com)\n99.83.176.46 ✖\npaqypal.com 95.211.75.10 ✖\npɑypal.com\n(xn--pypal-0jc.com)\n99.83.176.46 ✖\npåypal.com\n(xn--pypal-mra.com)\n99.83.176.46 ✖\npoypal.com 5.22.145.121 ✖\npqaypal.com 77.247.182.244 ✖\npäypal.com\n(xn--pypal-gra.com)\n99.83.176.46 ✖\npyypal.com 68.178.132.165 ✔\npâypal.com\n(xn--pypal-3qa.com)\n99.83.176.46 ✖\npawypal.com 103.224.212.216 ✔\npàypal.com\n(xn--pypal-rqa.com)\n99.83.176.46 ✖\npáypal.com\n(xn--pypal-xqa.com)\n99.83.176.46 ✖\npqypal.com 3.64.163.50 ✖\npiypal.com 3.64.163.50 ✖\npeypal.com 93.115.28.104 ✖\nlogin-paypal.com 99.83.176.46 ✖\npaypal.info 3.33.139.32 ✔\npsypal.com 75.126.104.249 ✖\npaypal.ru 3.33.139.32 ✖\npyaypal.com 96.126.123.244 ✔\npaypal.in 64.4.250.39 ✔\npaypal.tk 3.33.139.32 ✖\nsecurity-paypal.com 91.184.0.200 ✖\npaypal.buzz 99.83.176.46 ✖\npạypal.com\n(xn--pypal-j11b.com)\n185.214.125.59 ✔\npaypal.org 3.33.139.32 ✔\npaypal.net 3.33.139.32 ✔\npaypal.uk 3.33.139.32 ✖\np-aypal.com 54.235.212.68 ✖\npaypalcom.com 199.59.243.225 ✖\nwww-paypal.com 64.190.63.111 ✔\npaypal.fit 3.33.130.190 ✖\npaypal.co 64.4.250.38 ✔\nwwpaypal.com 199.59.243.225 ✖\npaypal.de 64.4.250.38 ✔\napypal.com 93.115.28.104 ✖\nppaypal.com 3.33.139.32 ✔\nṕaypal.com\n(xn--aypal-ho1b.com)\n99.83.176.46 ✖\npaypal.wang 23.227.38.65 ✖\nauth-paypal.com 173.201.177.241 ✖\nwwwpaypal.com 95.211.219.67 ✔\npaypal.top 118.193.11.34 ✖\npaypal.cn 103.150.165.251 ✔\nlaypal.com 66.63.171.125 ✔'


class CloneFinder:

    @staticmethod
    def find_clones(dns_twist_link: str) -> List[TypoSquat]:

        # with webdriver.Chrome() as driver:
        
        #     domain_results = CloneFinder._get_domain_results(dns_twist_link, driver)
        domain_results = RESULT
        domain_results = CloneFinder._parse_result(domain_results)
        
        for domain, ip in domain_results.items():
            yield domain, ip

    @staticmethod
    def _get_domain_results(dns_twist_link, driver) -> str:
        dnstwist_results = []
        driver = webdriver.Chrome()
        driver.get(dns_twist_link)

        WebDriverWait(driver, 40).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//*[@id='progress_fill'][contains(@style,'width: 100%')]")
            )
        )

        return driver.find_elements(By.ID, 'resolved_report_target')[0].text

    def _parse_result(results: str) -> Dict[str, str]:
        result_dict = {}
        results = results.replace("✖","").replace("✔","").split("\n")

        for result in results:
            result = result.rstrip(' ').split(' ')
            
            if len(result) == 2:
                key, value = tuple(result)

                result_dict[key] = value

        return result_dict
