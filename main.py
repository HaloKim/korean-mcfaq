import pandas as pd
import requests
from lxml.html import fromstring
import ray
from tqdm import tqdm


ray.init()


@ray.remote
def scrape_data(n):
    try:
        url = "https://korean.go.kr/front/mcfaq/mcfaqView.do?mn_id=217&mcfaq_seq={}".format(n)
        res = requests.get(url)
        parser = fromstring(res.text)

        title = parser.xpath("/html/body/div/div[2]/div/div[2]/div[3]/div[1]/h2/text()")
        date = parser.xpath("/html/body/div/div[2]/div/div[2]/div[3]/div[1]/div/span[1]/text()")
        q = parser.xpath("/html/body/div/div[2]/div/div[2]/div[3]/div[2]/text()")
        a = parser.xpath("/html/body/div/div[2]/div/div[2]/div[3]/div[2]/div/text()")
        data = {'제목': title, '등록일': date, '질문': ' '.join(q), '답변': ' '.join(a)}
        return pd.DataFrame(data)
    except:
        return pd.DataFrame()


def main(last=9301):
    df = pd.DataFrame(columns=['제목', '등록일', '질문', '답변'])
    futures = [scrape_data.remote(n) for n in range(5552, last+1)]
    df_list = ray.get(futures)
    for sub_df in df_list:
        df = pd.concat([df, sub_df])
    df.to_csv('./국립국어원_온라인가나다_자주묻는질문.csv')
    return df


if __name__ == "__main__":
    main(9301)
