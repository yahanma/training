def pathway (fluxes,outputfile_name):
    import csv
    flux = open(outputfile_name, 'w')
    modelname = 'SEED-name.txt'
    s = csv.reader(open(modelname), delimiter="\t")
    realist = []
    realist.extend(s)
    for r,v in fluxes.iteritems():
        if abs(v)>1e-6:
            print (r,v)
            for i in realist:
                if i[0]==r:
                    flux.write(i[0] +'\t' + str(v) + '\t' + i[1] +'\n')
    flux.close()