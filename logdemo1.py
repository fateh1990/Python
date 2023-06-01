import logging
logging.basicConfig(filename = "test2.log" , level = logging.DEBUG , format = '%(asctime)s %(name)s %(levelname)s  %(message)s')
l1_int = []
l2_str = []
for i in l :
    logging.info("we are iterating throuhg our list and our local var is {}")
    if type(i ) == list :
        logging.info("i am inside if statement and i am trying to check list type")
        for j in i :
            logging.info("i am in anothe for loop for list inside list element ")
            if type(j) == int :
                logging.info("i am inside if statement")
                l1_int.append(j)
    elif type(i) == int :
        l1_int.append(i)
