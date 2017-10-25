
f_list = (("estado_1997.csv", "estado_1997"),
        ("estado_1998.csv", "estado_1998"),
        ("estado_1999.csv", "estado_1999"),
        ("estado_2000.csv", "estado_2000"),
        ("estado_2001.csv", "estado_2001"),
        ("estado_2002.csv", "estado_2002"),
        ("estado_2003.csv", "estado_2003"),
        ("estado_2004.csv", "estado_2004"),
        ("estado_2005.csv", "estado_2005"),
        ("estado_2006.csv", "estado_2006"),
        ("estado_2007.csv", "estado_2007"),
        ("estado_2008.csv", "estado_2008"),
        ("estado_2009.csv", "estado_2009"),
        ("estado_2010.csv", "estado_2010"),
        ("estado_2011.csv", "estado_2011"),
        ("estado_2012.csv", "estado_2012"),
        ("estado_2013.csv", "estado_2013"),
        ("estado_2014.csv", "estado_2014"),
        ("estado_2015.csv", "estado_2015"),
        ("estado_2016.csv", "estado_2016"),
        ("estado_2017.csv", "estado_2017"))

for F in f_list:
    first = 1
    buff = ""
    fi = F[0]
    fo = F[1]
    with open(fi, mode='r', encoding='utf-8') as f:
        for l in f:
            l = l.split(";")
            if first:
                buff += "{ 'hc-key': '%s', value: %s }" % (l[0], l[1][:-1])
                first = 0
            else:
                buff += ",\n{ 'hc-key': '%s', value: %s }" % (l[0], l[1][:-1])

    with open(fo, mode='w', encoding='utf-8') as f:
        f.write(buff)
