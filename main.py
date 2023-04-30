from icrawler.builtin import GoogleImageCrawler

def google_img_downloader():
    #Фильтрация поиска
    #filters = dict( 
        #type='photo', 
        #color='',
        #size="large",
        #license='noncommercial, commercial',
        #date=() 
    #)

    crawler = GoogleImageCrawler(storage={'root_dir' : './img'}) #Путь к папке 

    crawler.crawl(keyword='Название', #Поиск и устоновка изображений
                  max_num=5,
                  #min_size=(1000, 1000),
                  #filters=filters,
                  #file_idx_offset='auto'
                ) 

def main():
    google_img_downloader()

    
if __name__ == '__main__':
    main()