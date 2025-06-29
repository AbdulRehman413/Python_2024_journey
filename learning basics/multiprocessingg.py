import multiprocessing
import requests
import os 



def downlaodfile(url, name):
    print(f"started downloadin {name}")
    
    response = requests.get(url)
    with open (f"files/{name}.jpg","wb") as f:
        f.write(response.content)
    print(f"finished downloading {name}")

if __name__ == "__main__":
    os.makedirs("files", exist_ok=True)

    url = "https://picsum.photos/2000/3000"

    pros = []
    for i in range(5):
        p = multiprocessing.Process(target=downlaodfile, args=[url, i])
        p.start()
        pros.append(p)

    for p in pros:
        p.join()

    
