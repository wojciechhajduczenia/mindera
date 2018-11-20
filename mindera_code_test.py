'''
Created on Nov 17, 2018

@author: wojtekhaj
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

#path = '/home/wojtekhaj/mindera/qa-sortable-challenge/solution/chromedriver'
path = ''
driver=webdriver.Chrome(path)
driver.get("http:localhost:3000/")
assert "Mindera QA Challenge" in driver.title
driver.save_screenshot("before.png")
menuItems= driver.find_elements_by_xpath("//*[@id='app']/ul/li")
count=len(menuItems)

text="Amount of elements in the list:"
print(text + str(count))

button_list=[]
for element_number in range(count):
    print(menuItems[element_number].text)
    button_list.insert(element_number,str(menuItems[element_number].text))   
print(button_list)
button_list.sort()
print(button_list)

for element_number in range(count):
    element_to_drag_name=button_list[element_number]
    print("element to drag:" + element_to_drag_name)
    
    source=driver.find_element_by_xpath("//li[text()='"+ element_to_drag_name +"']")
    print("source...................")
    print(source)
 
    destination=driver.find_element_by_xpath("//li[6]")
    print("destination........................... ")
    print(destination)
    
    ActionChains(driver).move_to_element(source).click_and_hold().move_to_element_with_offset(destination, 0, 60).release().perform()

    
driver.save_screenshot("after.png")  
#driver.quit()