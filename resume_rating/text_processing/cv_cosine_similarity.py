from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords as stp
from sklearn.feature_extraction.text import CountVectorizer
from preprocessing import cv_lemmetizer as cv_lemma


def get_binay_cosine_similarity(compare_doc,doc_corpus):
    # lemmatizer = WordNetLemmatizer()
    # analyzer = CountVectorizer().build_analyzer()
    #
    # def stemmed_words(doc):
    #     return (lemmatizer.lemmatize(w) for w in analyzer(doc) if w not in set(stp.words('english')))

    count_vect = CountVectorizer(binary=True,analyzer=cv_lemma.stemmed_words)
    #count_vect = CountVectorizer(stop_words='english', binary=True)
    cv_req_vector = count_vect.fit_transform([compare_doc]).todense()
    #cv_resume_vector = count_vect.fit_transform(doc_corpus).todense()
    #print('stop words are:' ,count_vect.get_stop_words())
    print('Features are:' ,count_vect.get_feature_names())
    cv_resume_vector = count_vect.transform(doc_corpus).todense()
    cosine_similarity_list = []
    for i in range(len(cv_resume_vector)):
        cosine_similarity_list.append(cosine_similarity(cv_req_vector,cv_resume_vector[i])[0][0])
    return cosine_similarity_list

def get_cosine_similarity(compare_doc,doc_corpus):
    # lemmatizer = WordNetLemmatizer()
    # analyzer = CountVectorizer().build_analyzer()
    #
    # def stemmed_words(doc):
    #     return (lemmatizer.lemmatize(w) for w in analyzer(doc) if w not in set(stp.words('english')))

    count_vect = CountVectorizer( analyzer=cv_lemma.stemmed_words)
    #count_vect = CountVectorizer(stop_words='english')
    cv_req_vector = count_vect.fit_transform([compare_doc]).todense()
    #print('Features are:', len(count_vect.get_feature_names()))
    #print(count_vect.get_feature_names())
    cv_resume_vector = count_vect.transform(doc_corpus).todense()
    cosine_similarity_list = []
    for i in range(len(cv_resume_vector)):
        cosine_similarity_list.append(cosine_similarity(cv_req_vector,cv_resume_vector[i])[0][0])
    return cosine_similarity_list


