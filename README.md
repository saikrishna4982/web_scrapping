# Web Scrapping
This Project Developed to Give an Overview about Web Scrapping, In this Project We Will be Using The following Website to Scrap/Get Data : https://www.timesjobs.com/
<br>Basically, This website is a Job Portal Where Jobs From Different Comapanies are posted, So In this Project By Using this Website We are going to get the latest Jobs avaialbe Based on the Skils Entered by the User.
### Technical Requirements
1. Django 4.0
<br>Install Using : `pip install django`
2. BeautifulSoap4
<br>Install Using : `pip install beautifulsoap4`
3. lxml
<br>Install Using : `pip install lxml`
4. pandas
<br>Install Using : `pip install pandas`
5. openpyxl
<br>Install Using : `pip install openpyxl`
6. python -  Download and follow instalation guide from https://www.python.org/downloads/
### How to Run this App:
1. Git Clone or Download the Repository into your local Machine
2. Open Your Command Prompt and Direct it towards the local Repository
3. After Being insde the Local Repository Type `python main.py` 
<br> As soon as you hit enter you will be prompted to enter the Skills for which you are looking Job's Enter the skills and press Enter
4. You Will see a Message On The Screen Saying **posted**
5. After That open your Local Repository You Will notice that a new file called **posts.xlsx** is created open the file to see the available jobs based on your skills
<br> **posts.xlsx** file contain columns like *Comapny Name,Experience,Skills Required,Location,More Information*

So, In this way you can get Information from AnyWebsite and Store it Anywhere you want.
