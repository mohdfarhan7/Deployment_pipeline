import requests
from bs4 import BeautifulSoup

def scrape_job_listings(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    job_listings = []
    # Find the HTML elements containing job information and extract the relevant data
    for listing in soup.find_all('div', class_='job-listing'):
        title = listing.find('h2').text.strip()
        company = listing.find('span', class_='company').text.strip()
        location = listing.find('span', class_='location').text.strip()
        job_listings.append({'title': title, 'company': company, 'location': location})

    return job_listings

# Example usage
job_listings = scrape_job_listings('https://example.com/jobs')  # Replace with the actual URL of the job listings page
for job in job_listings:
    print(f"Title: {job['title']}")
    print(f"Company: {job['company']}")
    print(f"Location: {job['location']}")
    print('---')
