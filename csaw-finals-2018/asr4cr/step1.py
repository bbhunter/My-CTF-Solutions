# From https://github.com/scryptos/scryptoslib
from scryptos.crypto.attack import *
from scryptos import *

import gmpy2

# From https://github.com/p4-team/crypto-commons
from crypto_commons.rsa.rsa_commons import *
from crypto_commons.generic import fermat_factors, bytes_to_long


p = 428643990416976477716764850878502231603705523272326398026786240084557376443073803416819816120333525653424613406611204037952546455629443911848049419374304880115648925248301709937343412988970459434056661778634837743595123576734580491051784931880469858273312892768122532095192274813235103685291374797410282818273

q = 337650031986638255256124896423474229331083186382695534617272536764831570266854189744586592186454979143954214295937685718718879065111184184757765801450026109110978471356060857270313869918128562484485794392597973610219214304334212116619451081817951317601028337770709368740009259230153993786625072792516471979157

c = 45532901824779701378231663264317691918332830832727980686741777650350897654972731931906126487183695081149779754337211259576173166293099080026360210494238959275834930884772828914504790990220112618808803618718921284861471408452351387148489569208903847288964821402052254148148283550521299399412532966770835208456058835316550638049581681130969595007241458911654151363153992694300910445899304425484918330492562481928441188111780684754432851810943390386788371370446571697596730749234374112810876064553895009312729747803267970163376377525012371123934730259190839294187981333459364290514186662847699605450828212079377654174428

e = 56464345445116249098049045336807445234357883929066056160509800851174255932943697111857107660018784212036377880810894047380656549383278972198516300670834705016468999714250951486912600249341791051961539477938043350992976556533909606031953927579029664976360355357096884954199433767448339255264831657804069495212007831723081630922243488700092552780963937083647566868158843349870118898134140101603936510785879524001693384328179832659722334742169456879889671271238721506778301709871337885442564361586631293011137834137912109208181348656281720720627766394041913283080319450233438914935475856576320213363102937394294033243533

n = 144731657075172369458365253117444692939543043921858848859103787081029935571261433965575780267889126491908228025197396050544630151378291212236766311668806004054369644769305000545793583915353079764667366200180574291376348069728516020997330701012031222049248560650540529425983462590552767265793268609531384242005329075143421408062869554263876675060033088763864236117044254825364969220914682084657647653707895098928730418682497939953647008736234172764734833411879279956351555928480516439340800516536708422230087334841118192814828087714947355712947595518081579349585938062548316427420775872732829914145491413512568074735861

'''
As e is too big, I used wiener to factor p,q
'''

#rsa = RSA(e, n)
#print rsautil.wiener(rsa)

phi = (p-1)*(q-1)
d = modinv(e,phi)
pt = rsa_printable(c,d,n)
print pt
# RSA{FIRST_ROUND_WAS_NOT_TOO_BAD}