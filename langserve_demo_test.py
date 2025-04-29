from langserve import RemoteRunnable


chain = RemoteRunnable("http://localhost:8000/chain/c/N4XyA") # copied from http://localhost:8000/chain/playground/ -> Share -> Python SDK
res = chain.invoke({"language": "Spanish", "text": "Generative AI is a bigger opportunity than Internet."})
print(res)

# open another terminal and activate the virtual environment.
# run the file using command : python langserve_demo_test.py