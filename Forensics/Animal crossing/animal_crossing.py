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