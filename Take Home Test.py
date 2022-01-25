from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

path = "/Users/manhlam/Desktop/cdriver"

search_list = []                                    #Array fuer die Sucheineigaben
search_input = input("Enter your search list: ")    #Eingabefeld; mehrere Eingaben mit Komma trennen
search_split = search_input.split(", ")              #Eingaben werden fuer die Liste gesplittet
browser = webdriver.Chrome(path)                    #oeffnet Chrome und die Website "Google.com" auf
elements = browser.get("https://www.google.com/")       
consent_button = browser.find_element(By.ID, "L2AGLb")  #sucht im HTML nach dem Element mit der ID "L2AGLb"
consent_button.click()                                  #klickt den o.g. Button an
for i in range(len(search_list)):                       #fuer jedes Element im Array wird folgendes ausgefuehrt
    search_bar = browser.find_element(By.NAME, 'q')     #sucht das Element mit dem Namen 'q' 
    search_bar.send_keys(search_list[i])                #gibt das i-te Element im Array in Suchbar ein
    search_bar.send_keys(Keys.RETURN)                   #betaetigt Eingabe Taste
    results = browser.find_element(By.CLASS_NAME, 'g')  
    link = results.find_element(By.TAG_NAME, 'a')       
    href = link.get_attribute('href')
    title = link.find_element(By.XPATH, '//h3[@class="LC20lb MBeuO DKV0Md"]') #sucht im HTML Code das h3 Element mit der Klasse "LC20lb MBeuO DKV0Md"; Element h3 beinhaltet erstes Ergbnis der Suchanfrage 
    print("Title: " + title.text)       #gibt Titel und Link der Suchanfrage raus
    print("Link: " + href)  
    browser.find_element(By.NAME, 'q').clear() #loescht Eintrag in der Suchbar
    
browser.quit()

       

