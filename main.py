from bs4 import BeautifulSoup
import requests,time
import pandas as pd
import openpyxl
def find_jobs(skils_to_check):
    html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup=BeautifulSoup(html_text,'lxml')
    jobs=soup.find_all("li",class_='clearfix job-bx wht-shd-bx')
    d={}
    for index,job in enumerate(jobs):
        published_date=job.find('span',class_="sim-posted").span.text
        if published_date=='Posted few days ago':
            company_name=job.find('h3','joblist-comp-name').text.strip()
            skills=job.find('span',class_="srp-skills").text.replace(" ","").strip()
            more_info=job.header.h2.a['href']
            details=job.find('ul',class_='top-jd-dtl clearfix')
            experience=details.li.text[11:]
            location=details.span.text
            for skill in skils_to_check:
                if skill in skills:
                    d[index]={"Comapny Name":company_name,'Experience': experience,'Skills Required':skills,'Location':location,'More Information': more_info}
    df=pd.DataFrame(d)
    df=df.transpose()
    df.to_excel('posts.xlsx',index=False)
    print("posted")

if __name__=='__main__':
    skils_to_check=input("Enter your skills seperated By Comma ")
    skils_to_check=skils_to_check.split(",")
    while True:
        find_jobs(skils_to_check)
        time_wait=10
        print(f'Waiting {time_wait} Seconds')
        time.sleep(time_wait)
