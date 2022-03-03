import pandas as pd
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import csv


data = pd.read_excel (r'/Users/malaikasheikh/test.xlsx') 
df = pd.DataFrame(data, columns= ['XML'])
df_list = df.values.tolist()
csvFile = open('testing.csv', 'w')
try:
    writer = csv.writer(csvFile)
    writer.writerow(('Cnic', 'file_no','tranx_no','seq_no','mem_name','subbrn_name','acct_no','acct_ty','term','acct_status','limit','open_date','maturity_date','co-borrower','status_date','last_payment','high_credit','overdueamount','balance','payment_status','currency'))
    for i in range(0,len(df_list)):
        xml = str(df_list[i])
        if(xml == '[nan]'):
            continue
        else:
            soup = BeautifulSoup(xml, 'lxml')
            cnic = soup.find('cnic')
            ccp_master = soup.find_all('ccp_master')
            print("Cnic: "+cnic.text)
            for j in range(0,len(ccp_master)):
                record = [] 
                myroot = ET.fromstring(str(ccp_master[j]))
                record.append(cnic.text)
                for x in myroot:
                    #print(str(x.tag) + ":" )
                    data = x.text
                    if(data == None):
                        record.append('None')
                    elif "<![CDATA" in data:
                        record.append(data[9:-3])
                    else:
                        record.append(data)
                writer.writerow(record)
            print(" ")
except Exception as e:
    print(e)
finally:
    csvFile.close()