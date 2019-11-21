'''
	REF:	https://docs.microsoft.com/en-us/azure/cognitive-services/bing-web-search/web-sdk-python-quickstart
'''

# Import required modules.
from azure.cognitiveservices.search.websearch import WebSearchAPI
from azure.cognitiveservices.search.websearch.models import SafeSearch
from msrest.authentication import CognitiveServicesCredentials

# Replace with your subscription key.
subscription_key = "05acd6c70fe449d98cfdf8b5866fe055"

# Instantiate the client and replace with your endpoint.
client = WebSearchAPI(CognitiveServicesCredentials(subscription_key), base_url = "https://api.cognitive.microsoft.com/bing/v7.0")

# Make a request. Replace Yosemite if you'd like.
#web_data = client.web.search(query="Yosemite")
web_data = client.web.search(query="RBC Royal Bank")
#print("\r\nSearched for Query# \" Yosemite \"")
print("\r\nSearched for Query# \" RBC Royal Bank \"")

'''
Web pages
If the search response contains web pages, the first result's name and url
are printed.
'''
if hasattr(web_data.web_pages, 'value'):

    print("\r\nWebpage Results#{}".format(len(web_data.web_pages.value)))

    first_web_page = web_data.web_pages.value[0]
    print("First web page name: {} ".format(first_web_page.name))
    print("First web page URL: {} ".format(first_web_page.url))

else:
    print("Didn't find any web pages...")

'''
Images
If the search response contains images, the first result's name and url
are printed.
'''
if hasattr(web_data.images, 'value'):

    print("\r\nImage Results#{}".format(len(web_data.images.value)))

    first_image = web_data.images.value[0]
    print("First Image name: {} ".format(first_image.name))
    print("First Image URL: {} ".format(first_image.url))

else:
    print("Didn't find any images...")

'''
News
If the search response contains news, the first result's name and url
are printed.
'''
if hasattr(web_data.news, 'value'):

    print("\r\nNews Results#{}".format(len(web_data.news.value)))

    first_news = web_data.news.value[0]
    print("First News name: {} ".format(first_news.name))
    print("First News URL: {} ".format(first_news.url))

else:
    print("Didn't find any news...")

'''
If the search response contains videos, the first result's name and url
are printed.
'''
if hasattr(web_data.videos, 'value'):

    print("\r\nVideos Results#{}".format(len(web_data.videos.value)))

    first_video = web_data.videos.value[0]
    print("First Videos name: {} ".format(first_video.name))
    print("First Videos URL: {} ".format(first_video.url))

else:
    print("Didn't find any videos...")

#####################################################################################################################

# Declare the function.
def web_results_with_count_and_offset(subscription_key):
	client = WebSearchAPI(CognitiveServicesCredentials(subscription_key))

	try:
    	'''
        Set the query, offset, and count using the SDK's search method. See:
        https://docs.microsoft.com/python/api/azure-cognitiveservices-search-websearch/azure.cognitiveservices.search.websearch.operations.weboperations?view=azure-python.
        '''
        web_data = client.web.search(query="Best restaurants in Seattle", offset=10, count=20)
        print("\r\nSearching for \"Best restaurants in Seattle\"")

        if web_data.web_pages.value:
            '''
            If web pages are available, print the # of responses, and the first and second
            web pages returned.
            '''
            print("Webpage Results#{}".format(len(web_data.web_pages.value)))

            first_web_page = web_data.web_pages.value[0]
            print("First web page name: {} ".format(first_web_page.name))
            print("First web page URL: {} ".format(first_web_page.url))

        else:
            print("Didn't find any web pages...")

	except Exception as err:
    	print("Encountered exception. {}".format(err))

#####################################################################################################################

# Declare the function.
def web_search_with_response_filter(subscription_key):
    client = WebSearchAPI(CognitiveServicesCredentials(subscription_key))
    try:
        '''
        Set the query, response_filter, and freshness using the SDK's search method. See:
        https://docs.microsoft.com/python/api/azure-cognitiveservices-search-websearch/azure.cognitiveservices.search.websearch.operations.weboperations?view=azure-python.
        '''
        web_data = client.web.search(query="xbox",
            response_filter=["News"],
            freshness="Day")
        print("\r\nSearching for \"xbox\" with the response filter set to \"News\" and freshness filter set to \"Day\".")

        '''
        If news articles are available, print the # of responses, and the first and second
        articles returned.
        '''
        if web_data.news.value:

            print("# of news results: {}".format(len(web_data.news.value)))

            first_web_page = web_data.news.value[0]
            print("First article name: {} ".format(first_web_page.name))
            print("First article URL: {} ".format(first_web_page.url))

            print("")

            second_web_page = web_data.news.value[1]
            print("\nSecond article name: {} ".format(second_web_page.name))
            print("Second article URL: {} ".format(second_web_page.url))

        else:
            print("Didn't find any news articles...")

    except Exception as err:
        print("Encountered exception. {}".format(err))

# Call the function.
web_search_with_response_filter(subscription_key)

#####################################################################################################################

# Declare the function.
def web_search_with_answer_count_promote_and_safe_search(subscription_key):

    client = WebSearchAPI(CognitiveServicesCredentials(subscription_key))

    try:
        '''
        Set the query, answer_count, promote, and safe_search parameters using the SDK's search method. See:
        https://docs.microsoft.com/python/api/azure-cognitiveservices-search-websearch/azure.cognitiveservices.search.websearch.operations.weboperations?view=azure-python.
        '''
        web_data = client.web.search(
            query="Niagara Falls",
            answer_count=2,
            promote=["videos"],
            safe_search=SafeSearch.strict  # or directly "Strict"
        )
        print("\r\nSearching for \"Niagara Falls\"")

        '''
        If results are available, print the # of responses, and the first result returned.
        '''
        if web_data.web_pages.value:

            print("Webpage Results#{}".format(len(web_data.web_pages.value)))

            first_web_page = web_data.web_pages.value[0]
            print("First web page name: {} ".format(first_web_page.name))
            print("First web page URL: {} ".format(first_web_page.url))

        else:
            print("Didn't see any Web data..")

    except Exception as err:
        print("Encountered exception. {}".format(err))
