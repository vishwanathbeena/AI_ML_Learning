from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords as stp
from preprocessing import tf_idf_lemmetizer as tf_idf_lemma

def get_tf_idf_cosine_similarity(compare_doc,doc_corpus):
    # lemmatizer = WordNetLemmatizer()
    # analyzer = TfidfVectorizer().build_analyzer()
    #
    # def stemmed_words(doc):
    #     return (lemmatizer.lemmatize(w) for w in analyzer(doc) if w not in set(stp.words('english')))

    tf_idf_vect = TfidfVectorizer(analyzer=tf_idf_lemma.stemmed_words)
    #tf_idf_vect = TfidfVectorizer(stop_words='english')
    tf_idf_req_vector = tf_idf_vect.fit_transform([compare_doc]).todense()
    #tf_idf_req_vector = tf_idf_vect.fit_transform(doc_corpus).todense()
    #print('Features are:', len(tf_idf_vect.get_feature_names()))
    #print(tf_idf_vect.get_feature_names())
    tf_idf_resume_vector = tf_idf_vect.transform(doc_corpus).todense()
    #tf_idf_resume_vector = tf_idf_vect.transform([compare_doc]).todense()
    cosine_similarity_list = []
    for i in range(len(tf_idf_resume_vector)):
        cosine_similarity_list.append(cosine_similarity(tf_idf_req_vector,tf_idf_resume_vector[i])[0][0])
    # for i in range(len(tf_idf_req_vector)):
    #   cosine_similarity_list.append(cosine_similarity(tf_idf_resume_vector,tf_idf_req_vector[i])[0][0])
    return cosine_similarity_list

def get_tf_cosine_similarity(compare_doc,doc_corpus):

    # lemmatizer = WordNetLemmatizer()
    # analyzer = TfidfVectorizer().build_analyzer()
    #
    # def stemmed_words(doc):
    #     return (lemmatizer.lemmatize(w) for w in analyzer(doc) if w not in set(stp.words('english')))

    tf_idf_vect = TfidfVectorizer(use_idf=False, analyzer=tf_idf_lemma.stemmed_words)
    #tf_idf_vect = TfidfVectorizer(stop_words='english',use_idf=False)

    tf_idf_req_vector = tf_idf_vect.fit_transform([compare_doc]).todense()
    #print('Features are:', len(tf_idf_vect.get_feature_names()))
    #print(tf_idf_vect.get_feature_names())
    tf_idf_resume_vector = tf_idf_vect.transform(doc_corpus).todense()
    cosine_similarity_list = []
    for i in range(len(tf_idf_resume_vector)):
        cosine_similarity_list.append(cosine_similarity(tf_idf_req_vector,tf_idf_resume_vector[i])[0][0])
    return cosine_similarity_list


