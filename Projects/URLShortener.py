import pyshorteners
import Constants
class URLShortener:
    print("Which platform would you like to use: ")
    print("""
             1: Tiny-URL,
             2: Bitly,
             3: Chilp.it,
             """)
    choice=input("Enter your choice: ")
    
    if choice=='1':
        long_url = input("Enter the URL to shorten: ")
        type_tiny = pyshorteners.Shortener()
        short_url = type_tiny.tinyurl.short(long_url)
        print("The Shortened URL is: " + short_url)
    if choice=='2':
        long_url = input("Enter the URL to shorten: ")
        type_bitly = pyshorteners.Shortener(api_key=Constants.BITLY_API_KEY_SERVICE)
        short_url = type_bitly.bitly.short(long_url)
        print("The Shortened URL is: " + short_url)
    if choice=='3':
        long_url = input("Enter the URL to shorten: ")
        short_url = pyshorteners.Shortener().chilpit.short(long_url)
        print("The Shortened URL is: " + short_url)
    print("Would you like to expand your short URL?")
    answer=input("1.Yes or 2.No : ")
    if (answer=='Yes'and choice=='2') :
        short_url=input("Enter the URL to expand: ")
        type_bitly = pyshorteners.Shortener(api_key=Constants.BITLY_API_KEY_SERVICE)
        long_url=type_bitly.bitly.expand(short_url)
        print("The Expanded URL is: " + long_url)
    if (answer=='Yes'and choice=='1') :
        short_url=input("Enter the URL to expand: ")
        type_tiny = pyshorteners.Shortener()
        long_url=type_tiny.tinyurl.expand(short_url)
        print("The Expanded URL is: " + long_url)
    else:
        print("Thank you for using our platform")
