import pandas

def read_excel():
    file_input = "data/AIYAIntentTemplate.xlsx"
    outputfile = open("data/nlu.md",'w')
    data = pandas.read_excel(open(file_input,"rb"),sheetname=0)
    data = data.fillna('')
    for column in data.columns:
        outputfile.writelines("## intent:"+str(column)+"\n")
        for row in data[column]:
            if '' != row:
                outputfile.writelines("- " + str(row)+"\n")
        outputfile.writelines("\n")

if __name__ == '__main__':
    file_input = "data/AIYAIntentTemplate.xlsx"
    read_excel()
