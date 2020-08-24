from Crypto.Util.number import inverse
import binascii
import gmpy2

n = 2394022425129158348864847443224458173779014261927740111244794464413563879302632785008801293723392607172049524487534795297142641108798189365883139773903001494227313226410875822739016099913407619451961681198433926803811641981069883969839016841126954143567328064956786317960718498779869873320091826409683741
c = 33968472370645261182632035351370572834046923936885849150758427394439089853042198039334736413729849687288289844308616781874965204824815808563103023769602191727553598270098139780884119381161521755207184636686956435524544519257809864055117983627035250402561123900020641699105773717004482846110284360195000
e = 65537

factors = [ 3, 43, 101, 1787, 120091, 215693, 2359482403, 2481618089, 2566978289, 2633652551, 2724934409,
            2846629007, 2850704267, 2929186907, 3104537879, 3175829737, 3197951849, 3241126099, 3287477441, 3329431081,
            3390914641 , 3402553849, 3452876029, 3454264111, 3455112149, 3484855259, 3488029459, 3767324447, 3827010907,
            3831830087 , 3860380091, 3907571699, 4034766187, 4041955903, 4171283407, 4224464213 ]

phi = 1

for number in factors:
    phi *= number - 1

d = inverse(e, phi)
m = pow(c, d, n)
print(binascii.unhexlify(hex(m)[2:].encode('utf-8')))