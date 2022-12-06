a=2
b=9
zp=0
op=0
for i in range(0,32):
	ab=a>>i
	bb=b>>i
	if ab==bb==0:
		zp+=1
	if ab==bb==1:
		op+=1
print(min(zp,op))

