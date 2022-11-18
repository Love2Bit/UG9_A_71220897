disc50 = 50/100
disc65 = 65/100
disc35 = 35/100
disc40 = 40/100
cpn = 25000*disc50
vpn = 22000*disc65
amn = 30000*disc35
brn = 20000*disc40
print('===================CAFE===================')
print('==========MASUKAN JUMLAH PESANAN==========')
capp =int( input('CAPPUCINO\tDISKON 50%\tRp 25.000\t: '))
vani =int( input('VANILLA LATTE\tDISKON 65%\tRp 22.000\t: '))
amer =int( input('AMERICANO\tDISKON 35%\tRp 30.000\t: '))
brew =int( input('BREWED COFFEE\tDISKON 40%\tRp 20.000\t: '))
print('===================TOTAL==================')
print('TOTAL CAPPUCINNO\t: Rp ',25000*capp-cpn)
print('TOTAL VANILLA LATTE\t: Rp ',22000*vani-vpn)
print('TOTAL AMERICANO\t: Rp ',30000*amer-amn)
print('TOTAL BREWED COFFEE\t: Rp ',20000*brew-brn)