##### WORKING CODE #####

##### Product Analyst scrape #####

# Currently, this scipt:
#1. Takes a URL
#
#
#
#


# Plan is to:
# 1. given job role and location preferences, get a URL for first page and concurrent pages (seems that concurrent pages have a 'start=x' param, where x == Page number * 25.)
# 2. Doesn't seem like BS4 (or LI) can ask for more than 25 roles at once
# 3. Compare to see if location params are exposed in GET response via URL
# 4. create an object that iterates through each URL, saves the:
## a. Job ID
## b. Name of company
## c. Title of role
## d. URL tied to each job into an object

# should look like: {[1234, 'Walla Inc', 'Chief Cup Officer', 'we really want a cup balancer, dassit']}

#5. Do this for 150-200 jobs (8 pages)
#6. Save (a-c) in a new object 'jds'
#7. Iterate through each jd.URL, scrape the copy, and add them to Jd.desc"
#8. Save the jds.desc into a .txt file


from bs4 import BeautifulSoup
import requests
import re # importing for RegEx
import matplotlib.pyplot as pPlot
from wordcloud import WordCloud, STOPWORDS
import numpy as npy
from PIL import Image
import datetime


desired_title = raw_input("Desired title: ")
desired_title_filename = desired_title.replace(" ", "_")
desired_title_urlencode = desired_title.replace(" ", "%20")


page_links = []
page_responses = []
page_contents = []

# creating a variable that will hold jobs (co, title, URL, desc[empty])
jds = []
data_id = []
jd_links = []
sj_responses = []
scrape_job_text = []

dt = str(datetime.datetime.now())

ff__ = open("./LI_Scraper/WC/" + desired_title_filename + "_job_descriptions.txt","a+")

wc_filename = "./LI_Scraper/WC/"+ desired_title_filename + "_WC_" + dt + ".png"


#sets STOPWORDS (words that you want the wordcloud to omit). Please remove wine-related stopwords from tutorial
stopwords = set(STOPWORDS)
stopwords.update(["Equal Opportunity",
                  "experience",
                  "skills",
                  "will",
                  "across",
                  "Analyst",
                  "drive",
                  "ability",
                "data driven",
                 "Product Management",
                 "time",
                  "Job function",
                 "Business",
                 "San Francisco",
                 "levelAssociateEmployment",
                 "typeFull",
                 "typeFull timeJob"
                 "timeJob",
                 "sexual orientation",
                 "Opportunity Employer",
                 "Equal Opportunity",
                 "timeJob functionBusiness",
                 "timeJob",
                  "function",
                 "functionBusiness",
                 "national origin",
                 "San",
                 "Francisco",
                 "New York",
                 "Equal",
                 "Opportunity",
                 "Sexual",
                 "Orientation",
                 "Product",
                 "Management",
                 "national",
                 "origin",
                 "veteran",
                 "veteran status",
                 "Bleacher",
                  "Report",
                  "Gender",
                  "Identity",
                  "Gender Identity",
                  "Fair",
                  "Chance",
                  "Fair Chance",
                 "Bleacher Report",
                 "NPS",
                 "Prism",
                 "NPS Prism",
                 "arrest",
                 "race",
                 "color",
                 "applicants",
                 "qualified",
                 "conviction",
                 "Bachelor",
                 "litigation",
                 "law firm",
                 "levelEmployment",
                 "levelEntry",
                 "injury",
                 "levelMid",
                 "Senior",
                 "Seniority",])


# Here, we're just importing both Beautiful Soup and the Requests library
# We
for i in range(0,9):
    pl_ = 'https://www.linkedin.com/jobs/search/?keywords=' + desired_title_urlencode + '&start=' + (str(25 * i))
    page_links.append(pl_)

    # no text but good to see status of API calls. this is the url that we've already determined is safe and legal to scrape from.
    pr_ = requests.get(page_links[i], timeout=10)
    page_responses.append(pr_)

    # here, we fetch the content from the url, using the requests library
    pc_ = BeautifulSoup(page_responses[i].content, "html.parser")
    page_contents.append(pc_)

    pc_pretty =  pc_.prettify()
    pc_results = pc_.body.main.div.section.ul

    pc_roles = pc_results.find_all(class_="result-card job-result-card result-card--with-hover-state")

    pc_results.li['data-id']
    # get u'1646844476'

    pcr__ = pc_results.find_all("li", "result-card job-result-card result-card--with-hover-state")
    sj_responses = []
    role_text = []

    # this returns the list of 25 data_id values
    # Given url = "https://www.linkedin.com/jobs/view/"+data_id it will return valid job posting URL

    for i in pcr__:
        if i.has_attr("data-id"):
            d_id = i["data-id"]
            data_id.append(d_id)
            # print(d_id)

            url__ = "https://www.linkedin.com/jobs/view/"+ d_id
            jd_links.append(url__)
            # print "adding %s to URL list" %(d_id)
            # print "%s added! New url: %s" % (d_id, url__)

            sjr__ = requests.get(url__, timeout=10)
            sj_responses.append(sjr__)

            #trying to create a BS4 object for each URL
            scrape_job_role = BeautifulSoup(sjr__.content,"html.parser")

            #NOTE we only want to add the section where the job description is, in order to save space
            #NOTE and not have to go through the entire object

            for element in scrape_job_role.find_all("section", "description"):
                uni_sjt = unicode(element.text)
                ascii_sjt2 = uni_sjt.encode('ascii', 'ignore')
                scrape_job_text.append(ascii_sjt2)
                ascii_sjt2 = str(ascii_sjt2)
                #print ascii_sjt2

                ff__.write(repr(ascii_sjt2))

ff__.close()
print "text-blurb saved!"

######## PA word cloud ########

#change the .png to any b&w (not transparent bground) image you like
wc_mask = npy.array(Image.open("goose_bw.png"))


wc = WordCloud(background_color="white", max_words=250, mask=wc_mask,
               stopwords=stopwords, contour_width=3, contour_color='firebrick')

#Create dataset using JD txt file
dataset = open("./LI_Scraper/WC/" + desired_title_filename + "_job_descriptions.txt", "r").read()

# Generate a wordcloud
wc.generate(dataset)

# store to file
wc.to_file(wc_filename)

# show
pPlot.figure(figsize=[30,15])
pPlot.imshow(wc, interpolation='bilinear')
pPlot.axis("off")
pPlot.show()
