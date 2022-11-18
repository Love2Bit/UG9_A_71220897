#harga
ch = 25000
vh = 22000
ah = 30000
bh = 20000
#disc
dc = 50/100
dv = 65/100
da = 35/100
db = 40/100
print('===================CAFE===================')
print('==========MASUKAN JUMLAH PESANAN==========')
capp =int( input('CAPPUCINO\tDISKON 50%\tRp 25.000\t: '))
vani =int( input('VANILLA LATTE\tDISKON 65%\tRp 22.000\t: '))
amer =int( input('AMERICANO\tDISKON 35%\tRp 30.000\t: '))
brew =int( input('BREWED COFFEE\tDISKON 40%\tRp 20.000\t: '))
#cappucinno
cpp = ch*capp
cpd = cpp*dc
cpn = cpp-cpd
#vanilla
vnn = vh*vani
vnd = vnn*dv
vnt = vnn-vnd
#americano
ame = ah*amer
amd = ame*da
amn = ame-amd
#brewed coffee
bre = bh*brew
brd = bre*db
brn = bre-brd
print('===================TOTAL==================')
print('TOTAL CAPPUCINNO\t: Rp ',cpn)
print('TOTAL VANILLA LATTE\t: Rp ',vnt)
print('TOTAL AMERICANO\t\t: Rp ',amn)
print('TOTAL BREWED COFFEE\t: Rp ',brn)
print('Jumlah total biaya yang harus dibayar adalah Rp.', cpn+vnt+amn+brn)