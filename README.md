# Google-Query-Sentiment-Analysis
Is Google search results ranking mitigated or influenced  in any way by the user’s query?

In order to respond to this question, we had to come up with a careful designed plan that tries to minimize the bias found in query formulation.

Why do we consider this question important?

We live in a world where everything is one click away. We tend to spend years of our life in the online environment, learn, get up to date with news, events from all around the world. How do we know the displayed data has not been altered along with our vision about a topic? How do we know that Google doesn’t have any other ranking system except PageRank?

Short description of how the algorithm works
I started by gathering the top 1000 queries searched on Google. I tried several libraries to get the most accurate sentiment analysis and we stop to nltk’s Sentiment Intensity Analyzer. This library returns the polarity scores (either a sentence is neutral, positive or negative) and we could observe in the image below that most of the questions are neutral as they should be.

I used a certified Google SERP API that would give the pages, a short description about them that corresponds to a query. I only filtered for English pages and took the first 10 pages with circa 10 results per page.

Then I ran the title and the description of each website through the same Sentiment Intensity Analyzer in order to see if Google tends to influence positively or negatively the results, since there cannot be any neutral content websites.


Conclusions
1. All the neutral queries (a score of 0) tend to lead to positive Google Search Results (the bigger the score, the more positive the website or article title / description).
2. The negative queries have positive results on the first pages and then followed by negative results (with few exceptions). Does Google try to hide the results we need to see, but show us the ones that we want to see? The data is way too less in order to respond to this question.
3. The positive query has the highest average sentiment per page ! This along with the most negative query which has the lowest average page sentiment shows us that Google results are influenced by the sentiment of the query !
