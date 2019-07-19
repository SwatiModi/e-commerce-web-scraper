import fyndScrapper
import os
import sys      

print("This is an interactive scrapper, Carefully follow the instruction prompted on terminal : ") 
availableWeb = [ 
                 "amazon",
                 "myntra",
                 "koovs",
                 "ajio",
                 "fynd"
                ]

print(" Following website are available for scraping --->  ")
for index,website in enumerate(availableWeb,start=0):
    print(str(index) + " : " + website )

webIndex = int(input("Enter the index of the website which you want to scrap or -1 to scrap all available website : "))
if webIndex != -1 :
    if webIndex < 0 and webIndex >= len(availableWeb):
        print("Invalid Index ! ")
        sys.exit()
    website = availableWeb[webIndex]
else :
    website = "all"

# dest_dir = input("Mention path to the directory where you want to store the new data folder : ")

# if os.path.isdir(dest_dir) is not True:
#     print("The Entered Directory path does not exist ")
#     sys.exit()

# if dest_dir[-1] != '/':
#     dest_dir = dest_dir + '/'

# print(dest_dir)

dest_dir = 'images'

item_category = input("Enter the items name : ")

fyndScrapper.scrapper(item_category,dest_dir,website)
# urls = fyndScrapper.scrapper(item_category,dest_dir,website)
# print(urls)