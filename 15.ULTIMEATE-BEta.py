import streamlit as st
import snscrape.modules.twitter as sntwitter
import pandas as pd

st.title('Scraping Twitter with Streamlit and Snscrape')

# Input query and number of tweets to scrape
query = st.text_input('Enter a search query:', 'data science')
num_tweets = st.number_input(
    'Number of tweets to scrape:', min_value=1, max_value=1000, step=1)

# Input since and until dates
since_date = st.date_input("Since Date", value=None,
                           min_value=None, max_value=None, key=None)
until_date = st.date_input("Until Date", value=None,
                           min_value=None, max_value=None, key=None)

# Scrape tweets and store data in a dataframe
tweets_list = []
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query + ' lang:id since:' + since_date.strftime('%Y-%m-%d') + ' until:' + until_date.strftime('%Y-%m-%d')).get_items()):
    if i >= num_tweets:
        break
    tweets_list.append([tweet.id, tweet.date, tweet.content, tweet.user.username,
                       tweet.user.followersCount, tweet.url, tweet.user.id])
tweets_df = pd.DataFrame(tweets_list, columns=[
                         'Tweet Id', 'Datetime', 'Text', 'Username', 'Followers', 'URL', 'User Id'])

# Display data
st.write(tweets_df)

# Download as text file
if st.button('Download as Text File'):
    t = '\t'.join(tweets_df.columns) + '\n'
    for index, row in tweets_df.iterrows():
        t += '\t'.join([str(elem) for elem in row.values]) + '\n'
    with open('tweets.txt', 'w') as f:
        f.write(t)
    st.download_button(
        label="Download Tweets as Text",
        data=t,
        file_name='tweets.txt',
        mime='text/plain'
    )

# Download as csv file
if st.button('Download as CSV File'):
    csv = tweets_df.to_csv(index=False)
    with open('tweets.csv', 'w') as f:
        f.write(csv)
    st.download_button(
        label="Download Tweets as CSV",
        data=csv,
        file_name='tweets.csv',
        mime='text/csv'
    )
