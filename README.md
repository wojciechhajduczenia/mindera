# mindera
desafio1

Fill in variable pointing to chrome webdriver location: path = ''

OS used for dev: CentOS Linux release 7.5.1804 (Core) 

Additional packages packages installed:
  - chromium
  - chromedriver
  - python
  - Xvfb 
  - libXfont 
  - Xorg
  - selenium standalone server
 
 XVFB configuration:  
 
 su username -c /usr/bin/Xvfb :99 -ac -screen 0 1280x1024x24 -nolisten tcp &gt
 
 Selenium standalone server configuration: 
 

 su $user -c /usr/bin/java -jar selenium_server_locstion -host 127.0.0.1 &gt
 
 To run:
 - download packages from this repository and place them in your folder
 - be sure to have sufficient permissions to start browser (chrome in this case) from command line ie.:/usr/bin/chromium-browser
 - to run the tests, type: python mindera_code_test.py
 
 Expected result:
 
 Amount of elements in the list:6
Item 5
Item 4
Item 3
Item 1
Item 2
Item 0
['Item 5', 'Item 4', 'Item 3', 'Item 1', 'Item 2', 'Item 0']
['Item 0', 'Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5']
element to drag:Item 0
source...................
<selenium.webdriver.remote.webelement.WebElement (session="774461b0a222dd550fb3a522a7ec864a", element="0.7343893415416458-6")>
destination........................... 
<selenium.webdriver.remote.webelement.WebElement (session="774461b0a222dd550fb3a522a7ec864a", element="0.7343893415416458-6")>
element to drag:Item 1
source...................
<selenium.webdriver.remote.webelement.WebElement (session="774461b0a222dd550fb3a522a7ec864a", element="0.7343893415416458-4")>
destination........................... 
<selenium.webdriver.remote.webelement.WebElement (session="774461b0a222dd550fb3a522a7ec864a", element="0.7343893415416458-6")>
element to drag:Item 2
source...................
<selenium.webdriver.remote.webelement.WebElement (session="774461b0a222dd550fb3a522a7ec864a", element="0.7343893415416458-4")>
destination........................... 
<selenium.webdriver.remote.webelement.WebElement (session="774461b0a222dd550fb3a522a7ec864a", element="0.7343893415416458-6")>
element to drag:Item 3
source...................
<selenium.webdriver.remote.webelement.WebElement (session="774461b0a222dd550fb3a522a7ec864a", element="0.7343893415416458-3")>
destination........................... 
<selenium.webdriver.remote.webelement.WebElement (session="774461b0a222dd550fb3a522a7ec864a", element="0.7343893415416458-6")>
element to drag:Item 4
source...................
<selenium.webdriver.remote.webelement.WebElement (session="774461b0a222dd550fb3a522a7ec864a", element="0.7343893415416458-2")>
destination........................... 
<selenium.webdriver.remote.webelement.WebElement (session="774461b0a222dd550fb3a522a7ec864a", element="0.7343893415416458-6")>
element to drag:Item 5
source...................
<selenium.webdriver.remote.webelement.WebElement (session="774461b0a222dd550fb3a522a7ec864a", element="0.7343893415416458-1")>
destination........................... 
<selenium.webdriver.remote.webelement.WebElement (session="774461b0a222dd550fb3a522a7ec864a", element="0.7343893415416458-6")>

 
 
