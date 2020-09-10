# Animal crossing

При поиске Animal Crossing на Nintendo Switch вы обнаруживаете странный трафик в своей сети. Исследуйте. <br/>
Формат флага: auctf{}<br/>

# Решение

В этом задании нам дали pcap с подозрительными запросами DNS.<br/>

**Вариант 1**<br/>

Видим, что каждый запрос DNS начинается со строки Base64 + ad.quickbrownfoxes.org, и извлекаем все запросы для домена ad.quickbrownfoxes.org командой:<br/>

`$ tshark -r animalcrossing.pcapng -T fields -e ip.src -e dns.qry.name -Y "dns.flags.response eq 0 and dns.qry.name contains ad.quickbrownfoxes.org"` <br/>
Дальше объединяем все строки Base64 и декодим их.<br/>
`$ cat animalcrossing_dns_query_b64_uniq.txt | sed ':a;N;$!ba;s/\n//g' | base64 -d`<br/>
В полученной строке находим флаг<br/>

**Вариант 2**<br/>

Проводим такие же операции, только с использованием скрипта:<br/>

```
from scapy.all import *
scapy_cap = rdpcap('animalcrossing.pcapng')
out = []
for packet in scapy_cap:
    if packet.haslayer(DNS):
        rec = packet[DNSQR].qname
        if b'ad.quickbrownfoxes.org' in rec:
            s = rec[:rec.find(b'.')]
            if s not in out:
                out.append(s)

print(''.join([i.decode() for i in out]))
```

В полученной строке находим флаг<br/>
