current_browser = 'firefox' 
print('Current Browser:', current_browser)

browsers = ['opera', 'google', 'chrome', 'edge', 'aloha', 'brave', 'vivaldi', 'duckduckgo', 'safari']

keywords_rem = ['download', 'install', 'set up']
keywords_ini = ['remove', 'uninstall', 'delete', 'erase', 'switch to']

def analyze_search(search):
     triggered = False
     search_m = search.lower().strip()
     
     # path a
     for keyword_rem in keywords_rem:
          for browser in browsers:
               if keyword_rem in search_m and browser in search_m: 
                    triggered = True
                    
     # path b
     for keyword_ini in keywords_ini:
          if keyword_ini in search_m and current_browser in search_m:
               triggered = True
       
     if triggered:
          print('Are you trying to switch browsers?\n')
     else:
          print('Nothing was triggered.\n')

print()
while True:
     search = input('Search: ')
     analyze_search(search)
