with open('abc', "w") as IFile:
        IFile.write(fileHeader + '\n')
        for upc in upcs:
            if upc == '123':
                onHandQty = str(random.randint(-1110, 0)/10)
            else:
                onHandQty = str(random.randint(1110, 24999)/10)
            data = 'D,' + '{0:<15}'.format(upc) + ',' + '{0:>6}'.format(onHandQty)
            IFile.write(data + '\n')
        IFile.write('T000008')