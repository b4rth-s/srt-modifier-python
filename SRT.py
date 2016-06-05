import os

a = input("Path to .srt file : ")
dt = int(input("Amount of delay (potitive value) = "))
sign = input("Are subtitles arriving too early ? (Y or N) ")
if sign != 'Y' or sign != 'y' or sign != 'yes' or file != 'Yes' :
 dt = -dt

f=open(a,'r',encoding='utf8')
nf=open(''.join([a.split('.')[0],"-2.srt"]),'w',encoding='utf8')

ST=f.readlines()

for l in ST :
 res = l
 if len(l) == 30 and l[2] == ':' and l[5] == ':' and l[13:16:1] == '-->' :
  str_deb, str_fin = l[0:12:1], l[17:29:1]
  h_deb, m_deb, s_ms_deb = int(str_deb.split(':')[0]), int(str_deb.split(':')[1]), str_deb.split(':')[2]
  h_fin, m_fin, s_ms_fin = int(str_fin.split(':')[0]), int(str_fin.split(':')[1]), str_fin.split(':')[2]
  s_deb, ms_deb = int(s_ms_deb.split(',')[0]), int(s_ms_deb.split(',')[1])
  s_fin, ms_fin = int(s_ms_fin.split(',')[0]), int(s_ms_fin.split(',')[1])
  
  ms_deb += dt
  ms_fin += dt

  if ms_deb >= 1000 or ms_deb <= 0 :
   q, r = divmod(ms_deb,1000)
   ms_deb = r
   s_deb += q
  if s_deb >= 60 or s_deb <= 0 :
   q, r = divmod(s_deb,60)
   s_deb = r
   m_deb += q
  if m_deb >= 60 or m_deb <= 0 :
   q, r = divmod(m_deb,1000)
   m_deb = r
   h_deb += q
  if h_deb < 0 :
   print("Error : negative time")
   quit()

  if ms_fin >= 1000 or ms_fin <= 0 :
   q, r = divmod(ms_fin,1000)
   ms_fin = r
   s_fin += q
  if s_fin >= 60 or s_fin <= 0 :
   q, r = divmod(s_fin,60)
   s_fin = r
   m_fin += q
  if m_fin >= 60 or m_fin <= 0 :
   q, r = divmod(m_fin,1000)
   m_fin = r
   h_fin += q
  if h_fin < 0 :
   print("Error : negative time")
   quit()

  h_deb, m_deb, s_deb, ms_deb, h_fin, m_fin, s_fin, ms_fin = str(h_deb), str(m_deb), str(s_deb), str(ms_deb), str(h_fin), str(m_fin), str(s_fin), str(ms_fin)

  if len(h_deb) == 1 :
   h_deb = ''.join(['0',h_deb])
  if len(m_deb) == 1 :
   m_deb = ''.join(['0',m_deb])
  if len(s_deb) == 1 :
   s_deb = ''.join(['0',s_deb])
  if len(ms_deb) <= 2 :
   ms_deb = ''.join(['0',ms_deb])
  if len(h_fin) == 1 :
   h_fin = ''.join(['0',h_fin])
  if len(m_fin) == 1 :
   m_fin = ''.join(['0',m_fin])              
  if len(s_fin) == 1 :
   s_fin = ''.join(['0',s_fin]) 
  if len(ms_fin) <= 2 :
   ms_fin = ''.join(['0',ms_fin])

  s_ms_deb, s_ms_fin = ','.join([s_deb,ms_deb]), ','.join([s_fin,ms_fin])
  str_deb, str_fin = ':'.join([h_deb,m_deb,s_ms_deb]), ':'.join([h_fin,m_fin,s_ms_fin])

  res = ' --> '.join([str_deb,str_fin])
  res = ''.join([res,'\n'])

 nf.write(res)

f.close()
nf.close()
 
quit()
