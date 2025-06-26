#Today I am learning about multithreading and multiprocessing. Bascially multithreading is used by every computer, because if CPU is staying idle for a second also is very big loss, when we accummulate the total time. So that's why rather than puting a CPU in idle mode, it better that it do some work in mean time, this is where multithreading comes into the picture, where a big task divides into threads and complete and back to main program whenever the task get's over. 

#In multiprocessing, each process have their own memory space (virtual space), so everything takes place in that space only. Thus program variable cannot be shared between the two process, if we want then need to use InterProcess Communication (IPC). So key difference between thread and process is that every thread is sharing the same memory space whereas every process have their own. One more thing need to takes care while creating the process, if we create more number of process than required then it will hinder the performance and takes more time then minimum. Always take care this with cpu_count() from multiprocessing. 

#Multithreading is basically used for io bound task, whereas Multiprocessing is used for cpu bound task that's heavy one like heavy computation. 

import time, multiprocessing, threading, requests

def square(number):
    for n in number:
        time.sleep(5)
        print(f"square = {n*n}")

def cube(number):
    for n in number:
        time.sleep(5)
        print(f"cube = {n*n*n}")
        
# if __name__=="__main__":
#     t = time.time()
#     num_range = range(1,5)
#     square(number=num_range)
#     cube(number=num_range)
    # thread1 = threading.Thread(target=square,args=(num_range,))
    # thread2 = threading.Thread(target=cube,args=(num_range,))

    # thread1.start()
    # thread2.start()

    # thread1.join()
    # thread2.join()

    # process1 = multiprocessing.Process(target=square,args=(num_range,))
    # process2 = multiprocessing.Process(target=cube,args=(num_range,))

    # process1.start()
    # process2.start()

    # process1.join()
    # process2.join()
    # print('Hey I am done with the process approach and below is the result in seconds')
    # print('Hey I am done with the threading approach and below is the result in seconds')
    # print('Hey I am done with the simple approach and below is the result in seconds')
    # print(f"{(time.time()-t)} seconds")
    
class FileHandler:
    def __init__(self,file_name:str, mode:str):
        self.filename = file_name
        self.mode = mode
        
    def __enter__(self):
        return open(file=self.filename,mode=self.mode)
        
    def __exit__(self,exc_type, exc_value,exc_tb):
        print(f"{self.filename} is Closed")
            
def file_downloader(url,filename):
    print(f"{filename} starts downloading")
    res = requests.get(url=url)
    with FileHandler(file_name=filename,mode='wb') as f:
        f.write(res.content)
    print(f"{filename} Download completed")

urls_list = [
    ("https://www.hloom.com/download-pdf/sample-contract-agreement.pdf", "Sample.pdf"),
    ("https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf", "Dummy.pdf"),
    ("https://www.orimi.com/pdf-test.pdf", "Test.pdf")
]
threads =[]
for url,name in urls_list:
    thread = threading.Thread(target=file_downloader,args=(url,name))
    thread.start()
    threads.append(thread)

for t in threads:
    t.join()
print('finally everything is completed')

        
    