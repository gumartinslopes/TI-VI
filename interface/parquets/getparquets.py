from datetime import datetime, timedelta
from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions
import pandas as pd
import os

# def getParquets():

#     # enter credentials
#     account_name = 'clothessimilar6084886475'
#     account_key = '2uI3KJBFT1J+e3prLGB9cPflPYOCcKaIkSC15CB2k3L2qlmnoPijl500M+ZPdUeOziiUORhBvJS7+AStJMaM2g=='
#     container_name = 'parquetonlypaths'

#     # create a client to interact with blob storage
#     connect_str = 'DefaultEndpointsProtocol=https;AccountName=' + account_name + \
#         ';AccountKey=' + account_key + ';EndpointSuffix=core.windows.net'
#     blob_service_client = BlobServiceClient.from_connection_string(
#         connect_str)

#     # use the client to connect to the container
#     container_client = blob_service_client.get_container_client(
#         container_name)

#     # get a list of all blob files in the container
#     df_treino_teste = []
#     blob_list = []
#     for blob_i in container_client.list_blobs():
#         blob_list.append(blob_i.name)

#         df_list = []
#         # generate a shared access signiture for files and load them into Python
#         for blob_i in blob_list:
#             # generate a shared access signature for each blob file
#             sas_i = generate_blob_sas(account_name=account_name,
#                                       container_name=container_name,
#                                       blob_name=blob_i,
#                                       account_key=account_key,
#                                       permission=BlobSasPermissions(read=True),
#                                       expiry=datetime.utcnow() + timedelta(hours=1))

#             sas_url = 'https://' + account_name+'.blob.core.windows.net/' + \
#                 container_name + '/' + blob_i + '?' + sas_i

#             df = pd.read_parquet(sas_url)
#             df_list.append(df)

#         df_combined = pd.concat(df_list, ignore_index=True)
#         df_treino_teste.append(df_combined)

#     #print(df_treino_teste)
#     df_treino_teste = pd.read_parquet(sas_url)
#     return df_treino_teste
def getParquets():  
   df = pd.read_parquet('./df.parquet')
   return [df]