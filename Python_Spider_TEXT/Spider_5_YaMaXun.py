import requests
url = "https://www.amazon.cn/dp/B073LJR2JF/460-5194156-4406010?_encoding=UTF8&_encoding=UTF8&ref_=pc_cxrd_658390051_recTab_658390051_t_6&pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=merchandised-search-4&pf_rd_r=YJGF3DJGY36XA2H539YD&pf_rd_r=YJGF3DJGY36XA2H539YD&pf_rd_t=101&pf_rd_p=7e00fee6-4e12-48f0-b4af-b99068b52067&pf_rd_p=7e00fee6-4e12-48f0-b4af-b99068b52067&pf_rd_i=658390051"
try:
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    print("爬取失败")