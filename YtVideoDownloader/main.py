from pytube import YouTube

link = input("Enter your url: >>")

y_tube = YouTube(link)


stream =y_tube.streams.filter(progressive=True)

video= list(enumerate(stream))


for i in video:
    print(i)


index =int(input("Give the indext of desire Stream:"))

stream[index].download()
print("Success")