countries.py
from pygal.i18n import COUNTRIES

for country_code in sorted(COUNTRIES.key()):
    print(country_code, COUNTRIES[country_code])
    
    
    
    
    

country_codes.py
from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """根据制定的国家，返回pygal使用的两个字母的国别码"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    #如果没有找到指定的国家，就返回none
    return None
    
   
