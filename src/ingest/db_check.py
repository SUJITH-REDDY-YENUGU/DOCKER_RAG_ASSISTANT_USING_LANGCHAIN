import chromadb
client = chromadb.PersistentClient(path="./vectordb/chroma")
print(client.list_collections())

## here check is just that chroma db is being present in memory i
#  dont know why i tried but there mighrt be  a issue i will try in future so 
## i will try in future but the pipeline i working correctly only