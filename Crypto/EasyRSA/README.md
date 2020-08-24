# EasyRSA

Студент М плохо изучал криптографию в институте. Он решил зашифровать сообщение алгоритмом RSA, но, к сожалению, что-то не правильно сделал, да ещё и секретный ключ удалил. Расшифруйте сообщение. <br/>

n=2394022425129158348864847443224458173779014261927740111244794464413563879302632785008801293723392607172049524487534795297142641108798189365883139773903001494227313226410875822739016099913407619451961681198433926803811641981069883969839016841126954143567328064956786317960718498779869873320091826409683741 <br/>

e=65537 <br/>

c=33968472370645261182632035351370572834046923936885849150758427394439089853042198039334736413729849687288289844308616781874965204824815808563103023769602191727553598270098139780884119381161521755207184636686956435524544519257809864055117983627035250402561123900020641699105773717004482846110284360195000 <br/>

Формат флага: antiflag{a-zA-Z0-9\_} <br/>

# Решение

Если разложить на множители n, то видно, что множителей не два, как требуется в rsa, а больше.<br/>
Несмотря на это найдем phi как произведение этих множителей, уменьшенных на 1, затем d как обратное к открытой экспоненте по модулю phi и, используя, полученные и имеющиеся данные расшифруем текст по формуле (подробно в вики). <br/>
Полученное сообщение надо перевести в ascii - символы. <br/>
Один из вариантов реализации идеи представлен в приложенном скрипте. <br/>

**_antiflag{34sy_RS4_y0u_4r3_b34ut1fu1}_**