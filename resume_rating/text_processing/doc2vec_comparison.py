import gensim
from gensim.models.doc2vec import TaggedDocument
from gensim.parsing.preprocessing import remove_stopwords
from preprocessing import nltk_tokenizer as nl_token

def get_doc2vec_similarity(req_doc,list_of_resume):
    train_corpus = list(read_corpus(list_of_resume))
    test_corpus = list(read_corpus([req_doc],tokens_only=True))
    model = gensim.models.doc2vec.Doc2Vec(vector_size=50, min_count=1, epochs=40)
    model.build_vocab(train_corpus)
    #print(model.wv.vocab)
    model.train(train_corpus, total_examples=model.corpus_count, epochs=model.epochs)
    inferred_vector = model.infer_vector(test_corpus[0])
    sims = model.docvecs.most_similar([inferred_vector], topn=len(model.docvecs))
    #print(sims)
    return sims



def read_corpus(doc_corpus,tokens_only=False):

    for i in range(len(doc_corpus)):
        tokens = gensim.utils.simple_preprocess(doc_corpus[i])
        selected_tokens=[]
        for token in nl_token.tag_tokens(gensim.utils.simple_preprocess(doc_corpus[i])):
            if token[1][0] in ('N', 'V','F'):
                selected_tokens.append(token[0])
            else:
                selected_tokens.append(token[0])
        if tokens_only:
            yield selected_tokens
        else:
            # For training data, add tags
            yield gensim.models.doc2vec.TaggedDocument(selected_tokens, [i])

def read_corpus_and_lemmatize(doc_corpus,tokens_only=False):
    doc_tokens = []
    for i in range(len(doc_corpus)):
        tokens = []
        temp_sentence = remove_stopwords(doc_corpus[i])
        #tokens = gensim.utils.lemmatize(temp_sentence,allowed_tags=re.compile('(NN|VB|)'))
        for token in nl_token.tag_tokens(nl_token.tokenize_document(temp_sentence)):
            if token[1][0] in ('N','V'):
                print(token[0])
                print(token[1])
                tokens.append(token[0])
        if tokens_only:
            doc_tokens.append(tokens)
        else:
            doc_tokens.append(TaggedDocument(words=tokens, tags=[i]))
    return doc_tokens
