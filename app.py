import pickle



with open('D:/Auchan_task/auchan_project/files/messages_to_parse.dat', 'rb') as f:
    data = pickle.load(f)

print(len(data))
