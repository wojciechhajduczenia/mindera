#Dockerfile to build an image which supports testing according to challenge.
FROM centos
# Essential tools and xvfb
RUN yum install -y unzip curl xvfb chromium chromedriver python libXfont Xorg wget

# Chrome Driver
RUN mkdir -p /tmp/project/ 

RUN wget --no-verbose -P /tmp/project/ https://chromedriver.storage.googleapis.com/2.42/chromedriver_linux64.zip 
RUN unzip /tmp/project/*.zip && rm -rf chromedriver_linux64.zip
RUN ln -fs /tmp/project/chromedriver /usr/local/bin/chromedriver;
RUN wget --no-verbose -P /tmp/project/  http://selenium-release.storage.googleapis.com/2.40/selenium-server-standalone-2.40.0.jar 
RUN killall Xvfb && /usr/bin/Xvfb :99 -ac -screen 0 1280x1024x24 -nolisten tcp & 
RUN killall selenium-server && /usr/bin/java -jar /tmp/project/selenium-server* -host 127.0.0.1 &
COPY mindera_code_test.py /tmp/project/mindera_code_test.py
EXPOSE 3000
EXPOSE 99
EXPOSE 8080

