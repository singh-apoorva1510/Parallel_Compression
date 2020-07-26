
#Importing libraries for functions and thread
import thread, time, sys ,math ,string
#Dictionary containing dataword and corresponding code word.
mapping={'a':'1110','b':'001111','c':'01001','d':'11111','e':'100','f':'00100','g':'110111','h':'0110',
'i':'1011','j':'001110011','k':'1101000','l':'11110','m':'00110','n':'1010','o':'1100','p':'110101',
'q':'001110001','r':'0101','s':'0111','t':'000','u':'01000','v':'1101001','w':'00101','x':'001110010',
'y':'110110','z':'001110000','.':'001110110',' ':'00111010','\n':'001110111'}
#Dictionry containing codeword and corresponding dataword.Used for decompressing file.
reverse={'001110111':'\n','00111010':' ','001110110':'.','1110':'a','01001':'c','001111':'b','100':'e',
'11111':'d','110111':'g','00100':'f','1011':'i','0110':'h','1101000':'k','001110011':'j','00110':'m',
'11110':'l','1100':'o','1010':'n','001110001':'q','110101':'p','0111':'s','0101':'r','01000':'u','000':'t',
'00101':'w','1101001':'v','110110':'y','001110010':'x','001110000':'z'}
#List of dataword.
dataword=['\n',' ','.','a','c','b','e','d','g','f','i','h','k','j','m','l','o','n',
'q','p','s','r','u','t','w','v','y','x','z']
#List of codeword.
codeword=['001110111','00111010','001110110','1110','01001','001111','100','11111',
'110111','00100','1011','0110','1101000','001110011','00110','11110','1100',
'1010','001110001','110101','0111','0101','01000','000','00101','1101001',
'110110','001110010','001110000']

query=None
temp=[""]
result=[]
flag=[False]
master_flag=False
temp_length=int(0)
tt=""
def main():
	global query
	global temp,result
	global flag,length,p_no,master_flag,tt,temp_length
	fp=open("a.txt",'r')
	wp=open("result.txt",'w')
	#Store content of file in to string length of string n
	query=fp.read()
	#Enter number of processor  N
	p_no=int(raw_input("enter no of processors"))
	temp=temp*p_no
	flag=flag*p_no
	length=len(query)
	result=[[] for x in range(p_no)]
	for p_id in xrange(p_no):
		#Start new processor
		thread.start_new(compress,(p_id,) )
	ind=False
    	tmp=True
    	while ind == False :
        	time.sleep(1)
        	for j in range(p_no):
            		tmp=tmp and flag[j]
        	ind=tmp
        	tmp=True
        for pp in temp:
        	tt=tt+pp
        print tt
        temp_length=len(tt)
        for j in range(p_no):
        	flag[j]=False
        time.sleep(1)
        master_flag=True
        print temp_length
        ind=False
    	tmp=True
    	while ind == False :
        	time.sleep(2)
        	for j in range(p_no):
            		tmp=tmp and flag[j]
        	ind=tmp
        	tmp=True
        print result
        for i in result:
        	wp.write(''.join(i))
        print len(result)	
def compress(p_id):
	p_id=int(p_id)
	#lower limit for processor is ceiling(n/N)*p_id
	low=int(math.ceil(float(length)/p_no))*p_id
	#upper limit for processor is min ( ceiling(n/N)*(p_id +1) ,n)
	high=min(int(math.ceil(float(length)/p_no))*(p_id+1),length)	
	time.sleep(1)
	for i in range(low,high):
		#append the codeword corresponding to dataword from dictionary.
		temp[p_id]=temp[p_id]+mapping[query[i]]
	flag[p_id]=True
    while master_flag == False :
       	time.sleep(2)
    #lower limit for processor is ceiling(n/N)*p_id
    low=int(math.ceil(float(temp_length)/(p_no*8)))*p_id*8
    #upper limit for processor is min( ceiling(n/N)*(p_id +1),n)
    high=min(int(math.ceil(float(temp_length)/(p_no*8)))*(p_id+1)*8,temp_length)	
	f=low+int(math.floor((high-low)/8)*8)#find number of bytes to processor.
	for i in range(low,f,8):
		#convert next 8 binary sequence of char to int followed by char and append to result.
		result[p_id].append(chr((string.atoi(tt[i:i+8],2))))
	if(f!=high):
		extra=8-(temp_length%8)
		result[p_id].append(chr((string.atoi(tt[f:temp_length],2))))
	flag[p_id]=True
        print "%d complete successfully" % (p_id) 


main()

