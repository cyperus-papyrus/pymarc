# coding: utf-8
import pymarc
import argparse


parser = argparse.ArgumentParser(description='Выделяем isbn')
parser.add_argument('--in', required=True, dest='InFileName', help='укажите имя входного файла')
parser.add_argument('--v', required=False, dest='verbose', action="store_true", help='verbose режим')
args = parser.parse_args()

r = pymarc.MARCReader(file(args.InFileName),file_encoding='cp1251')
for x in r:
    isbn = x['920']['a']
    print isbn
    print 'LDR', x.leader
    for y in x:
        if y.tag <'010' and y.tag.isdigit():
            print y.tag, y.data
        else:
            if y.indicators[1] == ' ' and  not y.indicators[0] == ' ':
                print y.tag + y.indicators[0]
            elif y.indicators[0] == ' ' and not y.indicators[1] == ' ':
                print y.tag + ' ' + y.indicators[1]
            elif y.indicators[0] == ' ' and y.indicators[1] == ' ':
                print y.tag
            else:
                new_indicators = ''.join(y.indicators)
                print y.tag + new_indicators
            subfields = []
            for subfield in y:
                new_subfields = ' '.join(subfield)
                subfields.append(new_subfields)
            print ' '.join(subfields)
