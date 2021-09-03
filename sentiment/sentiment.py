from textblob import TextBlob
from db import Mongo
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def getDataFromOriginal():
    'fetches the records from the database to display it in the frontend plugin'
    # empty array to store data
    output = []
    for s in Mongo.originalCol.find():
        del s['_id'] #delete the default ID created by mongoDB
        if s['caption'] != '':
            output.append(s)
    return output

def sentimentalAnalysis():
    data = getDataFromOriginal()
    Mongo.kfcCol.drop()
    Mongo.subwayCol.drop()
    Mongo.mcdCol.drop()
    Mongo.dominosCol.drop()
    Mongo.timCol.drop()
    for r in data:
        review = {}
        review['id_review'] = r['id_review']
        review['caption'] = r['caption']
        review['relative_date'] = r['relative_date']
        review['retrieval_date'] = r['retrieval_date']
        review['rating'] = r['rating']
        review['username'] = r['username']
        review['n_review_user'] = r['n_review_user']
        review['n_photo_user'] = r['n_photo_user']
        review['url_user'] = r['url_user']
        review['subject'] = r['subject']
        

        useBlob = r['caption']
        blob = TextBlob(useBlob) 
        review['polarity'] = blob.sentiment.polarity
        
        if review['polarity'] > 0:
            review['polarity_sentiment'] = 'Positive'
        elif review['polarity'] < 0:
            review['polarity_sentiment'] = 'Negative'
        else:
            review['polarity_sentiment'] = 'Neutral'

        
        analyzer = SentimentIntensityAnalyzer()
        sentence = r['caption']
        subScore = analyzer.polarity_scores(sentence)
        review['subjectivity'] = subScore['compound']

        if subScore['compound'] > 0:
            review['subjectivity_sentiment'] = 'Subjective'
        elif subScore['compound'] == 0:
            review['subjectivity_sentiment'] = 'Neutral'
        elif subScore['compound'] < 0:
            review['subjectivity_sentiment'] = 'Objective'

        if review['subject'] == 'KFC':
            Mongo.kfcCol.insert_one(review)
        elif review['subject'] == 'Subway':
            Mongo.subwayCol.insert_one(review)
        elif review['subject'] == 'McDonalds':
            Mongo.mcdCol.insert_one(review)
        elif review['subject'] == 'Dominos':
            Mongo.dominosCol.insert_one(review)
        else:
            Mongo.timCol.insert_one(review)


sentimentalAnalysis()