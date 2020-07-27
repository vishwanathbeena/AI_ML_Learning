from preprocessing import docx_processing  as doc, textract_processing as txt
from text_processing import tf_idf_cosine_similarity as tf_idf,doc2vec_comparison as d2v
from text_processing import cv_cosine_similarity as cv
import os

# def process_doc2_vec_process(req_document,resume_docs):
#     req_doc_text = doc.get_content_as_string(req_document)
#     resume_doc_text = []
#     final_doc_rating_list = []
#     for doct in resume_docs:
#         resume_doc_text.append(doc.get_content_as_string(doct))
#     d2v.get_doc2vec_similarity(req_doc_text,resume_doc_text)

# def process_doc2vec_textract(req_document,resume_docs):
#     req_doc_text = txt.get_content_as_string(req_document)
#     # print('The start' * 5)
#     resume_doc_text = []
#     for doct in resume_docs:
#         resume_doc_text.append(txt.get_content_as_string(doct))
#     # print(req_doc_text)
#     # print(resume_doc_text)
#     d2v.get_doc2vec_similarity(req_doc_text, resume_doc_text)

def process_files(req_document,resume_docs):
    # req_doc_text = doc.get_content_as_string(req_document)
    # resume_doc_text = []

    # for doct in resume_docs:
    #     resume_doc_text.append(doc.get_content_as_string(doct))

    req_doc_text = txt.get_content_as_string(req_document)
    # print('The start' * 5)
    resume_doc_text = []
    for doct in resume_docs:
        resume_doc_text.append(txt.get_content_as_string(doct))

    #similarity_list = d2v.get_doc2vec_similarity(req_doc_text, resume_doc_text)
    #cos_sim_list = tf_idf.get_tf_cosine_similarity(req_doc_text,resume_doc_text)
    # zipped_docs = zip(cos_sim_list,resume_docs)
    # sorted_doc_list = sorted(zipped_docs, key = lambda x: x[0],reverse=True)
    # final_doc_rating_list = []
    # for element in similarity_list:
    #     doc_rating_list = []
    #     doc_rating_list.append(os.path.basename(resume_docs[element[0]]))
    #     doc_rating_list.append("{:.0%}".format(element[1]))
    #     final_doc_rating_list.append(doc_rating_list)
    #print(final_doc_rating_list)
    #return final_doc_rating_list
    # print('TF cosine similarity')
    #print(final_doc_rating_list)



    # TF-IDF - cosine similarity
    # final_doc_rating_list = []
    cos_sim_list = tf_idf.get_tf_idf_cosine_similarity(req_doc_text,resume_doc_text)
    final_doc_rating_list = []
    zipped_docs = zip(cos_sim_list,resume_docs)
    sorted_doc_list = sorted(zipped_docs, key = lambda x: x[0], reverse=True)
    for element in sorted_doc_list:
        doc_rating_list = []
        doc_rating_list.append(os.path.basename(element[1]))
        doc_rating_list.append("{:.0%}".format(element[0]))
        final_doc_rating_list.append(doc_rating_list)
    return final_doc_rating_list
    # print('TF-IDF cosine similarity')
    # print(final_doc_rating_list)
    #
    # # binary cv - cosine similarity
    # final_doc_rating_list = []
    # cos_sim_list = cv.get_binay_cosine_similarity(req_doc_text,resume_doc_text)
    #
    # zipped_docs = zip(cos_sim_list,resume_docs)
    # sorted_doc_list = sorted(zipped_docs, key = lambda x: x[0],reverse=True)
    # for element in sorted_doc_list:
    #     doc_rating_list = []
    #     doc_rating_list.append(os.path.basename(element[1]))
    #     doc_rating_list.append("{:.0%}".format(element[0]))
    #     final_doc_rating_list.append(doc_rating_list)
    # print('Binary BOW cosine similarity')
    # print(final_doc_rating_list)
    #
    # # Regular cv - cosine similarity
    # final_doc_rating_list = []
    # cos_sim_list = cv.get_cosine_similarity(req_doc_text,resume_doc_text)
    #
    # zipped_docs = zip(cos_sim_list,resume_docs)
    # sorted_doc_list = sorted(zipped_docs, key = lambda x: x[0],reverse=True)
    # for element in sorted_doc_list:
    #     doc_rating_list = []
    #     doc_rating_list.append(os.path.basename(element[1]))
    #     doc_rating_list.append("{:.0%}".format(element[0]))
    #     final_doc_rating_list.append(doc_rating_list)
    # print(' BOW cosine similarity')
    # print(final_doc_rating_list)


# if __name__ == "__main__":
#      req_document = 'D:\\learning\\data\\Data\\JD\\WalletShare - P2 ETL DataStage JD.docx'
#      resume_docs = ['D:\\learning\\data\\Data\\Resume\\Srinivas Sivadasu.docx',
#                     'D:\\learning\\data\\Data\\Resume\\Pavan Reddy.docx',
#                     'D:\\learning\\data\\Data\\Resume\\Veeranjaneyulu Tokala.docx',
#                     'D:\\learning\\data\\Data\\Resume\\Sana Reddy.docx'
#                     , 'D:\\learning\\data\\Data\\Resume\\Vishwanath A.docx'
#                     , 'D:\\learning\\data\\Data\\Resume\\Udaya Bhaskar.docx'
#                     , 'D:\\learning\\data\\Data\\Resume\\Ravichandra Reddy.docx'
#                     , 'D:\\learning\\data\\Data\\Resume\\Ravi Kumar.docx'
#                     , 'D:\\learning\\data\\Data\\Resume\\Ambati Nageswararao .docx'
#                     ]
# #     # lemmatizer = WordNetLemmatizer()
# #     # word_list = ['lead', 'leadership', 'leading']
# #     # op = ' '.join(lemmatizer.lemmatize(w) for w in word_list)
# #     # print(op)
#      process_files(req_document,resume_docs)






