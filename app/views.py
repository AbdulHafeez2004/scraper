from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import time
from django.contrib import messages
from requests.exceptions import ConnectionError

# Create your views here.

def index(request):
    if request.method == 'POST':
        url = request.POST['url']
        
        

        def find_jobs():
            html_text = requests.get(url).text

            soup  = BeautifulSoup(html_text, 'lxml')
            jobs = soup.find_all('li', class_= 'clearfix job-bx wht-shd-bx')

            for index, job in enumerate(jobs):
                published_date = job.find('span', class_ = 'sim-posted').span.text.replace(' ', '')
                if 'few' in published_date:
                    company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
                    skills = job.find('span', class_='srp-skills').text.replace(' ','').replace('"', '')
                    more_info = job.header.h2.a['href']
                    
                    Company__name = company_name.strip()
                    Required__Skill = skills.strip()
                    MoreInfo =  more_info

                    messages.success(request, f'Company name: {Company__name}' )
                    messages.success(request, f'Required Skills: {Required__Skill}' )
                    messages.success(request,f'More Information: {MoreInfo}' )
                    messages.success(request, ' ')

                        



                
                # else:
                #     find_jobs()
                #     time_wait = 10
                #     print(f'Waiting {time_wait} minutes...')
                #     time.sleep(time_wait * 60)

        try:
            find_jobs()
        except ConnectionError as e:
            messages.error(request, 'Check your connection and try again.')


    return render(request, 'index.html')