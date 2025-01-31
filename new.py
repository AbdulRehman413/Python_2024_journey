with open('myfile.txt', 'w') as f:
    # print(type(f))
    f.write('hello world')
    f.truncate(7)
    with open('myfile.txt', 'r') as f:
        print(f.read())
    
 