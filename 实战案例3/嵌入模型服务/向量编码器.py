# coding=utf-8
from langchain.embeddings import HuggingFaceBgeEmbeddings

class 向量编码器:
    def __init__(self):
        向量编码模型本地存放路径 = "F:\LLAMA_INDEX_CACHE_DIR\models\embeddings"
        向量编码本地所使用的device = "cpu"
        
        model_name = "BAAI/bge-large-zh-v1.5"
        cache_folder=向量编码模型本地存放路径
        model_kwargs = {'device': 向量编码本地所使用的device} #{'device': 'cuda'} # {'device': 'cpu'}
        encode_kwargs = {'normalize_embeddings': True} # set True to compute cosine similarity
        self.embed_model = HuggingFaceBgeEmbeddings(model_name=model_name,cache_folder=cache_folder,model_kwargs=model_kwargs,encode_kwargs=encode_kwargs)

    def 向量编码(self,query: str):
        embed_result =  self.embed_model.embed_query(query)
        return {'向量编码':embed_result}