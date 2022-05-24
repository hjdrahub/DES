
# -*- coding: UTF-8 -*-
# 2014/10/16  wrote by yangyongzhen
# QQ:534117529
# global definition
# base = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F]
 
__author__ = 'YangYongZhen'
 
base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'),ord('A')+6)]
# bin2dec
# 二进制 to 十进制: int(str,n=10)
def bin2dec(string_num):
	return str(int(string_num, 2))
 
# hex2dec
# 十六进制 to 十进制
def hex2dec(string_num):
	return str(int(string_num.upper(), 16))
 
# dec2bin
# 十进制 to 二进制: bin()
def dec2bin(string_num):
	num = int(string_num)
	mid = []
	while True:
		if num == 0: break
		num,rem = divmod(num, 2)
		mid.append(base[rem])

	return ''.join([str(x) for x in mid[::-1]])
 
# dec2hex
# 十进制 to 八进制: oct()
# 十进制 to 十六进制: hex()
def dec2hex(string_num):
	num = int(string_num)
	if num==0:
		return '0'
	mid = []
	while True:
		if num == 0: break
		num,rem = divmod(num, 16)
		mid.append(base[rem])
 
	return ''.join([str(x) for x in mid[::-1]])
 
# hex2tobin
# 十六进制 to 二进制: bin(int(str,16))
def hex2bin(string_num):
	return dec2bin(hex2dec(string_num.upper()))
 
# bin2hex
# 二进制 to 十六进制: hex(int(str,2))
def bin2hex(string_num):
	return dec2hex(bin2dec(string_num))
'''
/**
 * PBOC3DES 加密算法
 * @author Administrator
 *
 */
'''
class PBOC_DES():
	pass
'''
/** ***************************压缩替换S-Box************************************************* */
'''
subKey = [([0] * 48) for ll in range(16)]
 
s1 = [
		[ 14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7 ],
		[ 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8 ],
		[ 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0 ],
		[ 15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13 ] ]
 
s2 = [
		[ 15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10 ],
		[ 3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5 ],
		[ 0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15 ],
		[ 13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9 ] ]
 
s3 = [
		[ 10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8 ],
		[ 13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1 ],
		[ 13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7 ],
		[ 1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12 ] ]
 
s4 = [
		[ 7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15 ],
		[ 13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9 ],
		[ 10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4 ],
		[ 3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14 ] ]
 
s5 = [
		[ 2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9 ],
		[ 14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6 ],
		[ 4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14 ],
		[ 11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3 ] ]
 
s6 = [
		[ 12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11 ],
		[ 10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8 ],
		[ 9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6 ],
		[ 4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13 ] ]
 
s7 = [
		[ 4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1 ],
		[ 13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6 ],
		[ 1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2 ],
		[ 6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12 ] ]
 
s8 = [
		[ 13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7 ],
		[ 1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2 ],
		[ 7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8 ],
		[ 2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11 ] ]
 
ip = [  58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
		62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
		57, 49, 41, 33, 25, 17,  9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
		61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7 ]
 
_ip = [ 40, 8, 48, 16, 56, 24, 64, 32, 39, 7,47, 15, 55, 23, 63, 31,
		38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45,13, 53, 21, 61, 29,
		36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11,51, 19, 59, 27,
		34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25 ]

# 每次密钥循环左移位数
LS = [ 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2,2, 1 ]
# 差分分布表 8*64*16
Sd = []
for i in range(8):
	Sd.append([])
	for j in range(64):
		Sd[i].append([])
		for k in range(16):
			Sd[i][j].append({})
			Sd[i][j][k]['array']=[]
			Sd[i][j][k]['count']=0
# 放统计规律的C数组 8*64
C = []
for i in range(8):
	C.append([])
	for j in range(64):
		C[i].append(0)
res = []
for i in range(8):
	res.append([])
	for j in range(8):
		res[i].append([])
		for k in range(64):
			res[i][j].append(0)
'''
/**
 * 数组C初始化
 */
'''
def initC(arr):
	for i in range(8):
		for j in range(64):
			arr[i][j] = 0
def initres(arr):
	for i in range(8):
		for j in range(8):
			for k in range(64):
				arr[i][j][k] = 0
'''
/**
 * IP初始置换
 * @param source
 * @return
 */
'''
def changeIP(source):
	dest= [0]*64
	global ip
	for i in range(64):
		dest[i] = source[ip[i] - 1]
	return dest

'''
/*
 *十六进制字符串转二进制列表
*/
'''
def string2Binary(str):
	le = len(str)
	dest =[0]*le*4
	i = 0
	for c in str:
	   i += 4
	   j = 0
	   s = hex2bin(c)
	   l = len(s)
	   for d in s:
		   dest[i-l+j]=int(d)
		   j += 1
	return dest
'''
/*
 *十进制字符串转二进制列表
*/
'''
def decstring2Binary(str):
	return string2Binary(dec2hex(str))
'''
/*
 *0-63的数转化为6位array
*/
'''
def decstring26bit(str):
	temp = decstring2Binary(str)
	ret = [0] * 6
	if len(temp) > 6:
		for i in range(6):
			ret[i] = temp[i+2]
	else :
		ret[0] = 0
		ret[1] = 0
		for i in range(4):
			ret[i+2] = temp[i]
	return ret
print(decstring26bit('20'))
'''
/**
 * IP-1逆置
 * @param source
 * @return
 */
'''
def changeInverseIP(source):
		dest = [0]*64
		global _ip
		for i in range(64):
			dest[i] = source[_ip[i] - 1]
 
		return dest
'''
/**
 *
 * 获取轮子密钥(48bit)
 *
 * @param source
 *
 * @return
 *
 */
'''
def setKey(source):
	global subKey
	# 装换4bit
	temp = string2Binary(source)
	# 6bit均分成两部分
	left =  [0]*28
	right = [0]*28
	# 经过PC-14bit转换6bit
	temp1 = [0]*56
	temp1 = keyPC_1(temp)
	# printArr(temp1);
	#将经过转换的temp1均分成两部分
	for i in range(28):
		left[i] = temp1[i]
		right[i] = temp1[i + 28]
	# 经过16次循环左移，然后PC-2置换
	for i in range(16):
		left = keyLeftMove(left, LS[i])
		right = keyLeftMove(right, LS[i])
		for j in range(28):
				temp1[j] = left[j]
				temp1[j + 28] = right[j]
		subKey[i] = keyPC_2(temp1)
		# print(subKey[i])
 
'''
/**
 *
 * 6bit的密钥转换成48bit
 * @param source
 * @return
 *
 */
'''
def keyPC_2(source):
	dest = [0]*48
	temp = [ 14, 17, 11, 24, 1,   5,
			  3, 28, 15,  6, 21, 10,
			 23, 19, 12,  4, 26,  8,
			 16,  7, 27, 20, 13,  2,
			 41, 52, 31, 37, 47, 55,
			 30, 40, 51, 45, 33, 48,
			 44, 49, 39, 56, 34, 53,
			 46, 42, 50, 36, 29, 32 ]
	for i in range(48):
		dest[i] = source[temp[i] - 1]
	return dest
 
'''
/**
 *
 * 将密钥循环左移i
 * @param source 二进制密钥数
 * @param i 循环左移位数
 * @return
 *
 */
'''
def keyLeftMove( source, i):
	temp = 0
	global LS
	le = len(source)
	ls = LS[i]
	for k in range(ls):
		temp = source[0]
		for j in range(le-1):
			source[j] = source[j + 1]
	source[le - 1] = temp
	return source
'''
/**
 *
 * 4bit的密钥转换成56bit
 * @param source
 * @return
 *
 */
'''
def keyPC_1(source):
	dest = [0]*56
	temp = [ 57, 49, 41, 33, 25, 17,  9,
			  1, 58, 50, 42, 34, 26, 18,
			 10,  2, 59, 51, 43, 35, 27,
			 19, 11,  3, 60, 52, 44, 36,
			 63, 55, 47, 39, 31, 23, 15,
			  7, 62, 54, 46, 38, 30, 22,
			 14,  6, 61, 53, 45, 37, 29,
			 21, 13,  5, 28, 20, 12,  4 ]
	for i in range(56):
		dest[i] = source[temp[i] - 1]
	return dest
'''
/**
 * 两个等长的数组做异或
 * @param source1
 * @param source2
 * @return
 */
'''
def diffOr( source1, source2):
	le = len(source1)
	dest = [0]*le
	for i in range(le):
		dest[i] = source1[i] ^ source2[i]
	return dest
'''
/**
 *
 * DES加密--->对称密钥
 * D = Ln(32bit)+Rn(32bit)
 * 经过16轮置
 * @param D(16byte)明文
 * @param K(16byte)轮子密钥
 * @return (16byte)密文
 */
'''
def encryption( D,  K) :
	temp = [0]*64;
	data = string2Binary(D)
	# 第一步初始置
	data = changeIP(data)
	left =  [([0] * 32) for i in range(17)]
	right = [([0] * 32) for i in range(17)]
	for j in range(32):
		left[0][j] = data[j]
		right[0][j] = data[j + 32]
	setKey(K)# sub key ok
	for i in range(1,17):
		# 获取(48bit)的轮子密
		key = subKey[i - 1]
		# L1 = R0
		left[i] = right[i - 1]
		# R1 = L0 ^ f(R0,K1)
		fTemp = f(right[i - 1], key)# 32bit
		right[i] = diffOr(left[i - 1], fTemp)
	#组合的时候，左右调换
	for i in range(32):
		temp[i] = right[16][i]
		temp[32 + i] = left[16][i]
 
	temp = changeInverseIP(temp)
	str = binary2ASC(intArr2Str(temp))
	return str
'''
/*
 *单个S_box盒变换
*/
'''
def single_S_box(str,n):
	# 6bit src
	temp = decstring2Binary(str)
	src = [0]*6
	if len(temp) > 6 :
		for i in range(6):
			src[i] = temp[i + 2]
	else :
		for i in range(len(temp)):
			src[i+2] = temp[i]
	s =[s1,s2,s3,s4,s5,s6,s7,s8]
	x= src[0] * 2 + src[5]
	y= src[1] * 8 + src[2] * 4 + src[3] * 2 + src[4]
	return s[n][x][y]
'''
/**
 * 8bit压缩2bit
 * @param source(48bit)
 * @return R(32bit) B=E(R)⊕K，将48 位的B 分成8 个分组，B=B1B2B3B4B5B6B7B8
 */
 '''
def press(source) :
	ret = [0]*32
	temp =  [([0] * 6) for i in range(8)]
	s =[s1,s2,s3,s4,s5,s6,s7,s8]
	st=[]
	for i in range(8):
		for j in range(6):
			temp[i][j] = source[i * 6 + j]
	for i in range(8):
		# (16)
		x = temp[i][0] * 2 + temp[i][5]
		# (2345)
		y = temp[i][1] * 8 + temp[i][2] * 4 + temp[i][3] * 2+ temp[i][4]
		val = s[i][x][y]
		ch = dec2hex(str(val))
		# System.out.println("x=" + x + ",y=" + y + "-->" + ch);
		# String ch = Integer.toBinaryString(val);
		st.append(ch)
		# System.out.println(str.toString());
	ret = string2Binary(st)
	# printArr(ret);
	# 置换P
	ret = dataP(ret)
	return ret
'''
/**
 * 置换P(32bit)
 * @param source
 * @return
 */
'''
def dataP( source):
	dest = [0]*32
	temp = [ 16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31,
			 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25 ]
	le = len(source)
	for i in range(le):
		dest[i] = source[temp[i] - 1]
	return dest
'''
/**
 * 逆置换P-1(32bit)
 * @param source
 * @return
 */
'''
def dataPT(source):
	ret = [0] * 32
	PT = [ 9, 17, 23, 31, 13, 28, 2, 18, 24, 16, 30, 6, 26, 20, 10, 1, 
		   8, 14, 25, 3, 4, 29, 11, 19, 32, 12, 22, 7, 5, 27, 15, 21]
	le = len(source)
	for i in range(32):
		ret[i] = source[PT[i]-1]
	return ret
'''
/**
 * 2bit扩展8bit
 * @param source
 * @return
 */
'''
def expend(source):
	ret = [0]*48
	temp = [ 32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12,
			 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22,
			 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1 ]
	for i in range(48):
		ret[i] = source[temp[i] - 1]
	return ret
'''
/**
 * @param R(2bit)
 * @param K(48bit的轮子密
 * @return 32bit
 */
'''
def f( R,  K):
	dest = [0]*32
	temp = [0]*48
	# 先将输入32bit扩展8bit
	expendR = expend(R)# 48bit
	# 与轮子密钥进行异或运
	temp = diffOr(expendR, K);
	# 压缩2bit
	dest = press(temp)
	return dest
'''
/**
 * 将int类型数组拼接成字符串
 * @param arr
 * @return
 */
'''
def intArr2Str( arr) :
	sb = []
	le=len(arr)
	for i in range(le):
		sb.append(str(arr[i]))
	return ''.join(sb)
'''
/**
 * 将二进制字符串转换成十六进制字符
 * @param s
 * @return
 */
'''
def binary2ASC(s):
	st = ''
	ii = 0
	le= len(s)
	#不够4bit左补0
	if le % 4 != 0:
		while ii < (4 - len % 4):
			s = "0" + s
	le=int(len(s)/4)
	for i in range(le):
		st += bin2hex(s[i * 4 : i * 4 + 4])
	return st
# binary2ASC()
'''
/**
 * 两个等长的数组做异或
 * @param source1
 * @param source2
 * @return
 */
'''
def diffOr( source1, source2):
	le = len(source1)
	dest = [0]*le
	for i in range(le):
		dest[i] = source1[i] ^ source2[i]
	return dest
'''
/**
 *
 * DES解密--->对称密钥
 * D = Ln(32bit)+Rn(32bit)
 * 经过16轮置
 * @param D(16byte)明文
 * @param K(16byte)轮子密钥
 * @return (16byte)密文
 */
'''
def decryption( C,  K) :
	temp = [0]*64;
	data = string2Binary(C)
	# 第一步初始置
	data = changeIP(data)
	# print(data)
	left =  [([0] * 32) for i in range(17)]
	right = [([0] * 32) for i in range(17)]
	for j in range(32):
		left[16][j] = data[j + 32]
		right[16][j] = data[j]
	print(left[16],right[16])
	setKey(K)# sub key ok
	for i in range(16,0,-1):
		# 获取(48bit)的轮子密		
		key = subKey[i-1]
		# R15 = L16
		right[i - 1] = left[i]
		# R1 = L0 ^ f(R0,K1)
		# L15 = R16 ^f(L16,K16)
		fTemp = f(left[i], key)# 32bit
		left[i - 1] = diffOr(right[i], fTemp)
		print(left[i-1],right[i-1])
	#组合的时候，左右调换
	for i in range(32):
		temp[i + 32] = right[0][i]
		temp[i] = left[0][i]
 
	temp = changeInverseIP(temp)
	str = binary2ASC(intArr2Str(temp))
	return str
'''
/*
 *构建差分攻击统计表
*/
'''
def create_table():
	global Sd
	for n in range(8):
		for i in range(64):
			for j in range(64):
				temp0=bin2dec(intArr2Str(diffOr(decstring26bit(str(i)),decstring26bit(str(j)))))
				Sbox_x = single_S_box(str(i),n)
				Sbox_y = single_S_box(str(j),n)
				temp1=bin2dec(intArr2Str(diffOr(decstring26bit(str(Sbox_x)),decstring26bit(str(Sbox_y)))))
				Sd[n][int(temp0)][int(temp1)]['array'].append(i)
				Sd[n][int(temp0)][int(temp1)]['count'] += 1

'''
/*
 *构建差分攻击计数函数
 *核心部分，形成统计规律 输入为6位二进制字符串 也可以astr也可以直接传入6位2进制数组
 *放入C数组中
*/
'''
def attackCount(instr, outstr, astr,t):
	global C
	global Sd
	global res
	instr = int(bin2dec(instr))
	outstr = int(bin2dec(outstr))
	astr  = bin2dec(astr)
	for j in range(Sd[t][instr][outstr]['count']):
		temp1 = diffOr(decstring26bit(str(Sd[t][instr][outstr]['array'][j])),decstring26bit(astr))
		C[t][int(bin2dec(intArr2Str(temp1)))] += 1
		# res[t][i][int(bin2dec(intArr2Str(temp1)))] += 1

# diff_attack()
'''
/*
 *构建三轮差分攻击函数
 *主要函数
 *已知(L0,R0),(L0p,R0p) 默认输入格式为48位16进制字符串
 *已知(L3,R1),(L3p,R3p)
 *已知 INT 48bit OUT 32bit
*/
'''
def three_diff_attact(L0,L0p,L3,R3,L3p,R3p,):
	global C
	global res
	temp0 = expend(string2Binary(L3))
	temp1 = diffOr(expend(string2Binary(L3)),expend(string2Binary(L3p)))
	temp2 = dataPT(diffOr(diffOr(string2Binary(R3),string2Binary(R3p)),diffOr(string2Binary(L0),string2Binary(L0p))))
	E = []
	IN = []
	OUT = []
	for i in range(8):
		E.append([])
		IN.append([])
		OUT.append([])
		for j in range(6):
			E[i].append(temp0[i*6+j])
			IN[i].append(temp1[i*6+j])
		for j in range(4):
			OUT[i].append(temp2[i*4+j])
		attackCount(intArr2Str(IN[i]),intArr2Str(OUT[i]),intArr2Str(E[i]),i)
'''
/*
 *密钥还原函数
 *得到第三轮子密钥
*/
'''
def resetkey():
	global C
	for i in range(8):
		max = 0
		index = -1
		for j in range(64)
			if C[i][j] > max:
				max = C[i][j]
				index = j
# '''
# /*
#  *构建差分攻击函数
#  *主要函数
#  *已知(L0,R0),(L0p,R0p) 
#  *已知(L1,R1),(L1p,R1p)
#  *已知 INT 48bit OUT 32bit
# */
# '''
# def diff_attact(R0,R0p,IN,OUT):
# 	IN = string2Binary(IN)
# 	OUT = string2Binary(OUT)
# 	ER0 = expend(string2Binary(R0))

if __name__=="__main__":
 
	D='3031323334353637'
	K='1A624C89520DEC46'
	# C=encryption(D,K)
	# print("stop")
	# X=decryption(C,K)
	# print(C)
	# print(X)
	# print(type(C),type(D))
	create_table()
	three_diff_attact('748502CD','38747564','03C70306','D8A09F10','78560A09','60E6D4CB')
	three_diff_attact('48691102','375BD31F','45FA285B','E5ADC730','134F7915','AC253457')
	three_diff_attact('357418DA','12549847','D8A31B2F','28BBC5CF','0F317AC2','B23CB944')
	# print(C)
	for i in range()
	# attackCount('47','9','0')
	# for i in range(8):
	# 	print('-------')
	# 	for j in range(64):
	# 		if C[i][j] != 0:
	# 			print(j)
	# print(C)
	# diff_attack('47','9','0')


