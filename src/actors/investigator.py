
from models.typosquat import TypoSquat


import asyncio
import aiohttp


WHOIS_API_KEY = '7D807D27979F8C89B64882FC63FE9915'
VT_API_KEY = "f71dfc8ebb8d6b5c0694be4d1cbdefe0153f34727033ba181e64c30b672ecc64"

class Investigator:

    def __init__(self, culprit: TypoSquat):
        self.culprit = culprit

    def investigate(self):
        asyncio.run(self.run_api_calls())

    async def run_api_calls(self):
        whois_result = await self.whois_details()
        vt_result = await self.vt_data()  
        return whois_result, vt_result

    async def whois_details(self):
        
        geolocation_url = f"https://api.ip2location.io/?key={WHOIS_API_KEY}&ip={self.culprit.ip}&format=json"
        whois_url = f"https://api.ip2whois.com/v2?key={WHOIS_API_KEY}&domain={self.culprit.name}"
        
        async with aiohttp.ClientSession() as session:
            async with session.get(whois_url) as whois_response:
                whois_data = await whois_response.json()
            async with session.get(geolocation_url) as geo_response:
                location_data = await geo_response.json()
        
        if whois_response.status == 200:
            self.culprit.creation_date = whois_data['create_date']
            self.culprit.nameservers = whois_data['nameservers']
            self.culprit.registrar = whois_data['registrar']
        else:
            print(f"no whois data for {self.culprit.name}")

        if geo_response.status == 200:
            self.culprit.country = location_data['country_name']
            self.culprit.city = location_data['city_name']
            self.culprit.asn = location_data['asn']
        else:
            print(f"no geo data for {self.culprit.name}")    
        return
    
    async def vt_data(self):
        url = f"https://www.virustotal.com/api/v3/ip_addresses/{self.culprit.ip}"
        headers = {
            "accept": "application/json",
            "x-apikey": VT_API_KEY
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as vt_response:
                vt_results = await vt_response.json()
                
        if vt_response.status == 200:
            analysis_results = vt_results['data']['attributes']['last_analysis_stats']
            reputation =  vt_results['data']['attributes']['reputation']
        
            if analysis_results['malicious'] > 0:
                self.culprit.ip_is_flagged = True
            elif reputation < 0:
                self.culprit.ip_is_flagged = True
            else: 
                self.culprit.ip_is_flagged = False
        else:
            return
