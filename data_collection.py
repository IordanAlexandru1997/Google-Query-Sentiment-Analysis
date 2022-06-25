import random
import requests
import nltk.sentiment
import pandas as pd
from pprint import pprint as pp
from nltk.sentiment import SentimentIntensityAnalyzer


# set up the request parameters
params = {
    "api_key": "FECE96CB49A14DF59E572B3C11EBD2EC",
    "q": "",
    "output": "json",
    "num": "10",
    "hl": "en",
}


def get_page_sentiment(data, limit=10, sia=None):
    if sia is None:
        sia = SentimentIntensityAnalyzer()

    results_scores = []
    for search_result in data["organic_results"][:limit]:
        title_score = sia.polarity_scores(search_result["title"])["compound"]
        snippet_score = sia.polarity_scores(search_result.get("snippet", ""))[
            "compound"
        ]
        results_scores.append((title_score + snippet_score) / 2)
    return sum(results_scores) / len(results_scores)


def get_query_data(
    query="", api_link="https://api.scaleserp.com/search", params=params
):
    sia = SentimentIntensityAnalyzer()
    params["q"] = query
    api_result = requests.get(api_link, params)
    page_one_result = api_result.json()

    print(page_one_result)
    data = {
        "query": query,
        "sentiment query": sia.polarity_scores(query)["compound"],
        "sentiment page 1": get_page_sentiment(page_one_result, sia=sia),
    }
    for page_number, link_to_page in page_one_result["pagination"]["api_pagination"][
        "other_pages"
    ].items():
        response = requests.get(link_to_page)
        page_result = response.json()
        data[f"sentiment page {page_number}"] = get_page_sentiment(page_result, sia=sia)

    return data


def negative_expr_gen():

    df = pd.read_csv("./most_asked_questions.csv")
    df = df.dropna()

    questions = random.sample(df.index.tolist(), 25)
    print(questions)
    return [
        df.loc[question, "Most Asked Questions On Google"] for question in questions
    ]


if __name__ == "__main__":
    sentences = negative_expr_gen()
    # data = [get_query_data(sentence) for sentence in sentences]
    # df = pd.DataFrame(data)
    # Please change the name of the files on each run
    # df.to_csv('collected_data_3.csv')
    # with open('saved_3.txt', 'w') as f:
    #  f.write(str(data))

    df = pd.read_csv("collected_data.csv")
    cols = []
    for i in range(1, 11):
        cols.append(f"sentiment page {i}")

    df["avg_page_sentiment"] = df[cols].mean(axis=1)
    df.to_csv("final.csv")
