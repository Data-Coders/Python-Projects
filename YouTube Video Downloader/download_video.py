import pytube


class y2down():
    def downloadthis(self, link):
        link.streams.first().download()
        return True

    def view(self):
        print('|________________________________________________________|')
        print('|-------------Welcome to YouTube Video Downloader--------|')
        print('|--------------------------------------------------------|')
        y2down.getTheLink('Get the Link')

    def getTheLink(self):
        videoURL = str(input('Enter the URL to Download the Video : '))
        download = pytube.YouTube(videoURL)
        print(download)
        downloaded = y2down.downloadthis('Download this video', download)
        if downloaded:
            option = str(
                input('Want to Download More YouTube Videos (Y/N) : '))
            if option == 'Y':
                main()
                exit()
            elif option == 'N':
                print('Happy to Serve You Please Use Our Service More')
                exit()
            else:
                print(
                    'Please Enter the Correct Option.\n\nCurrently Quiting Better Luck Next time')
                exit()


def main():
    y2down.view('get the link')


if __name__ == "__main__":
    main()
