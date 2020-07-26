# Parallel_Compression
Parallel algorithm for Text file compression using Huffman coding

In this algorithm, first of all the input text string is equally divided among all the processors. Each
processor convert the characters of the string in the code words. These code words are determined
through Huffman coding. Now the new string is nothing but sequence of 0's and 1's. The binary
string is equally divided among all the processors. Each processor convert every consecutive 8 bits of
its part of the file into corresponding characters. Hence we get the compressed file.
The decompression is done in serial manner by converting every character of the file into its binary
value. Now the newly formed string is scanned from beginning to check the code word and replace
the code word with corresponding character. Code words follow prefix property which means a
codeword can't be a prefix of other codeword so, uniqueness is maintained.




Algorithm:

Input – A text string str

Number of characters in input string = n

Number of processors = N

Processor Model – EREW SM SIMD 

Output – A compressed string result Procedure parallel compression(str,result) 

Step 1: for i in 0 to N-1 do in parallel

Each P[i] computes

1.1	Lowi <-- ceiling(n/N)*i

1.2	Highi <-- min(ceiling(n/N)*(i+1),n )

1.3	For j in range low to high do

Tempi <-- tempi + codeword(str[j]) #temp stores intermediate result

    end for
    
end for

Step 2:processor P[0]

for i in range(0,N-1) do 

temp <-- temp + tempi

end for

Step 3: for i in 0 to N-1 do in parallel

Each P[i] computes

3.1	Lowi <-- ceiling(m/N)*i	              #m=length(temp)

3.2	Highi <-- min(ceiling(m/N)*(i+1),m)

3.3	octatei <-- Low +(ceiling(High -Low)/8)*8

3.4	for j in range (0,f,8) do 

resulti <-- resulti + chr(tmp[j:j+8])

End for

3.5	if m > f then

resulti <-- resulti + chr(tmp[f:m])

End if

end for

Step 4:processor P[0]

for i in range(0,N-1) do 

result <-- result + resulti

end for





Timing analysis:

step 1.1 ,1.2 and 1.3 takes constant time.

Step 1.4 will take n/N time since it string length of size n/N step 2 is bottleneck and takes n

step 3.1 3.2 and 3.3 takes constant time

step 3.4 take m/N time in processing string length of size m/N step 3.5 take constant time

step 4 take m/8 time (bottleneck)

Total complexity T(n) = O(max(n,m/8)) =O(n) since compressed string will always be less then original string.

T(n) = O(n)

P(n)= O(N)


C(n) = P(N)T(N) = O(Nn)

On sequential system it is O(n) Not cost optimal.


