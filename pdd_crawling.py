from urllib.request import urlopen, Request
from fake_useragent import UserAgent
import json
import pandas as pd
import numpy as np

useragent = UserAgent()

headers = {
    "User-Agent": useragent.chrome,
    "Content-Type": "application/json, text/plain, */*",
    "Host": "mobile.yangkeduo.com",
    "Origin": "http://mobile.yangkeduo.com",
    "Referer": "http://mobile.yangkeduo.com/",
    "Referrer Policy": "strict-origin-when-cross-origin",
}


goods_data_url2 = (
    "http://mobile.yangkeduo.com/proxy/api/api/caterham/query/"
    "fenlei_gyl_group?pdduid=0&page_sn=10002&opt_type=1&count=20&support_types=0_4_5_6_7_9&opt_name="
    "&platform=H5&page_id=index.html%3Fdy_sub_page%3Dcategory&opt_id=14&offset=0"
    "&list_id=fkwgrekvp8_14&anti_content=0aoAfxnUXycYY9dVzic_aXgZ9YGsCZnd2zFSO55WLOvVgf9OPpT_U"
    "8vtFfFpeaaXH_lMuCVQoHzDn5o25o0GrBB2j00MCYQoPPFT3VgF-q-50LumJLcGed9r2ndmwdZu2dSWYDEFRPvCd5b"
    "5M26xUigDTd1z89DbJd414sr29vcWC9sUoFmEIVkcNs7SG_0dftAGicCpWfOMDFfW1q5nr-huuXB1vx7KW8AhNfDgD"
    "q6dWwcz2peh1EFkdRg7sjxrz0giLnd0ungAbxa9TNgh3bp_Sy9u3ZVl3bKc43FouZkGBy5XWf7yvJA0Clw2qFMdRFG"
    "z2q7Rrfr-XJ0sVDZ0TRiVnzIXmcG0cHuspobAFI70dr6cP6ad96sdj9DJ9gtWONYQulj6mWyQujZVh7S1OHxDuRySE"
    "a0cdSsE9Ap-0VA8oYNbOVXBZZ5DUpLqQPX8LmZwZYQIcgUGPjFIfZdXZJ-mMr2mxaJ8Ub7PS3ee1cdyXLscfRlmRt1"
    "T8_1YCXZCzXuUPv5LefBFH7rMQukSO2HYyvnVNwkVb8jxqY_ZagMq8UJ_MufmqVng3bbXF4yuXNdudXMKxaZd8sFCq"
    "ymbIzGLsF3UejNcG0FhDGl3LCpMGancb85wk_G_7ErDYDdnURDmMKzRQRYsUJ5UBrj9LZ6D6k8tTLblQkNHblbrL0af2xyOBb5dtRR2FJKK4o"
)


def category_crawling():
    page_data_url = (
        "http://mobile.yangkeduo.com/proxy/api/api/caterham/query/"
        "opt2_brand_pcard?pdduid=0&opt1_id=1281&"
        "list_id=1281_ed79q2gh35_1281&support_type=10_11"
    )
    page_data_response = (
        urlopen(Request(page_data_url, headers=headers)).read().decode("utf-8")
    )
    page_data = json.loads(page_data_response)["data"]

    # 鞋 category
    category_id = []
    for i in page_data["opt2_list"]:
        category_id.append([i["id"], i["opt_name"]])

    category = pd.DataFrame(category_id, columns=["id", "name"])
    category.to_json("category.json", orient="table")
    print(category.head(5))


# goods
def goods_crawling():
    page = 1
    goods_data_url = (
        "http://mobile.yangkeduo.com/proxy/api/api/alexa/"
        "goods/hub?pdduid=0&page_sn=10002&list_update_time=true&platform=1"
        f"&assist_allowed=1&hs_version=2&wrt_type=1&page={page}&size=20"
        "&list_id=kuyal5m4j6&antiContent=0aoAfxn50Ol9Ug9TX64xHG_oKCKPAKru5JlgVf7EZTZT-TfBaSqGGXoLc"
        "qlr0BCVkBYNCTAoilfZTAoW7MhLevGKWt5Qf3OvhJ_Suxn5u7ovw7ppgNA6gam5UK7jJQhRuefg952kbottCVFCKrp"
        "CTQ42_lX2kx8QEx2efZ-TUHKaK51z1KjCv_pPn9fREz1XX7rmLQHc0u5IdPmEF9e--GZyUhog9B4Pk306w4H05k4vd6"
        "Shuv0Qz3DsAGY9FP2tcyzyGUR9NeUBOq1f6nvYfoO7t3w89YVPbf4gV0Tv3Fk-GNHzJMN5EhNJ4L-cDPiAIDwdiRu5kG"
        "cfZv-LIhIeSSbL7miR-yi6pvn_aAjfCANOpCnIblH5dDVOn6J9wYtehU"
    )
    goods_data_response = (
        urlopen(Request(goods_data_url, headers=headers)).read().decode("utf-8")
    )
    goods_data = json.loads(goods_data_response)["goods_list"]
    items = []
    for page in range(1, 20):
        goods_data_url = f"http://mobile.yangkeduo.com/proxy/api/api/alexa/goods/hub?pdduid=0&page_sn=10002&list_update_time=true&platform=1&assist_allowed=1&hs_version=2&wrt_type=1&page={page}&size=20&list_id=kuyal5m4j6&antiContent=0aoAfxn50Ol9Ug9TX64xHG_oKCKPAKru5JlgVf7EZTZT-TfBaSqGGXoLcqlr0BCVkBYNCTAoilfZTAoW7MhLevGKWt5Qf3OvhJ_Suxn5u7ovw7ppgNA6gam5UK7jJQhRuefg952kbottCVFCKrpCTQ42_lX2kx8QEx2efZ-TUHKaK51z1KjCv_pPn9fREz1XX7rmLQHc0u5IdPmEF9e--GZyUhog9B4Pk306w4H05k4vd6Shuv0Qz3DsAGY9FP2tcyzyGUR9NeUBOq1f6nvYfoO7t3w89YVPbf4gV0Tv3Fk-GNHzJMN5EhNJ4L-cDPiAIDwdiRu5kGcfZv-LIhIeSSbL7miR-yi6pvn_aAjfCANOpCnIblH5dDVOn6J9wYtehU"
        goods_data_response = (
            urlopen(Request(goods_data_url, headers=headers)).read().decode("utf-8")
        )
        goods_data = json.loads(goods_data_response)["goods_list"]
        for item in goods_data:
            items.append(
                [str(item["goods_id"]), item["short_name"], item["normal_price"]]
            )

    df = pd.DataFrame(items, columns=["id", "name", "price"])
    df.to_json("goods.json", orient="table")
    print(df.head(5))


if __name__ == "__main__":
    goods_crawling()
    category_crawling()
