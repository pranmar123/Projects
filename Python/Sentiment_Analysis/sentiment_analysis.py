#Sentiment Analysis using Google search results.

#BS4 and requests are used to scrape the web. 
from bs4 import BeautifulSoup
import requests

#Textblob is a sentiment analysis module
from textblob import TextBlob


class Analysis:
    def __init__(self,term):
        #search term
        self._term = term

        self._subjectivity = 0
        self._sentiment = 0
        
        #the self._url will take your 
        self._url = 'https://www.google.com/search?q={0}&source=lnms&tbm=nws'.format(self._term)
    #creating a function that will run the analysis
    def run(self):
        #will go the url that we have set, this will basically take the RAW HTML text
        #on the website which is the NEWS section of whatever our search time is. 
        response = requests.get(self._url)

        #using soup
        #BeautifulSoup will parser the HTML from the value that response holds.
        soup = BeautifulSoup(response.text, 'html.parser')
        #Now we will take the a tag in HTML to get all the text.
        #All the headlines in the google news have a class ST so we are grabbing the
        #headlines
        headline_results = soup.find_all('div',class_= 'st')

        for headline in headline_results:
            #This will grab the text from the headlines (because it still contains
            #some html tags like div etc.
            blob = TextBlob(headline.get_text())
            '''The blob will be analyzed using polairty which is an int between 1 to -1
            and will see if it is positive headlines or negative headlines
            We divide the answer by the number of headlines to get an
            mean (average) sentiment result'''
            self._sentiment += blob.sentiment.polarity / len(headline_results)

            '''now we will be checking the subjectivity of the text.
            subjectivity is how much the article is based on personal
            feelings and opinions'''
            self._subjectivity += blob.sentiment.subjectivity / len(headline_results)
    def print_sentiment(self):
        print("Scaled from -1 to 1: \n The sentiment of the article is: ",self._sentiment)

    def print_subjectivity(self):
        print("Scaled from -1 to 1: \n The subjectivity of the article is: ",self._subjectivity)
    

if __name__ == '__main__':
    news = str(input("Enter the news that you want to analyze: "))

    #Making an instance of the class that will analyze the term India
    term = Analysis(news)
    #running the analysis.
    term.run()

    term.print_sentiment()
    term.print_subjectivity()
        
