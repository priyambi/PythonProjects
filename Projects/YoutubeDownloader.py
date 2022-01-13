from pytube import YouTube		

print("One Spot to download all your youtube videos")
while True:

	link=input("Enter the link of your Youtube Video: ")
	try:
		vid = YouTube(link)
	except:
		print("Connection Error") 
	print("Information about the video you want to download: ")
	print("Title:",vid.title)
	print("Number of views:",vid.views)
	print("Length of video:",vid.length,"seconds")
	print("Description: ",vid.description)
	print("Ratings: ",vid.rating)
	vid_download = vid.streams.get_highest_resolution()
	print("Downloading...")
	vid_download.download("E:/")
	print("Download completed!!")
	str=input(("Would you like to download more videos ? YES or NO: "))
	if str=="YES":
		continue
	else:
		break
print("Thank you for using our Application")