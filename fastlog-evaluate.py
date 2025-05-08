import re
from datetime import datetime

def analyze_fast_log(file_path, attack_start_str, attack_end_str):
    attack_start = datetime.strptime(attack_start_str, "%m/%d/%Y-%H:%M:%S")
    attack_end = datetime.strptime(attack_end_str, "%m/%d/%Y-%H:%M:%S")

    tp_count = 0
    fp_count = 0
    total_parsed = 0
    results = []

    try:
        with open(file_path, "r") as f:
            for line in f:
                # timestamp
                match = re.search(r"(\d{2}/\d{2}/\d{4}-\d{2}:\d{2}:\d{2}\.\d+)", line)
                if match:
                    timestamp_str_full = match.group(1)
                    timestamp = datetime.strptime(timestamp_str_full, "%m/%d/%Y-%H:%M:%S.%f")

                    total_parsed += 1
                    if attack_start <= timestamp <= attack_end:
                        tp_count += 1
                        results.append((timestamp_str_full, "✅ TP"))
                    else:
                        fp_count += 1
                        results.append((timestamp_str_full, "❌ FP"))
                else:
                    results.append(("⛔ Parse Error", line.strip()))

        # percentage
        if total_parsed > 0:
            tp_rate = (tp_count / total_parsed) * 100
            fp_rate = (fp_count / total_parsed) * 100
        else:
            tp_rate = fp_rate = 0

        for ts, label in results:
            print(f"{ts} → {label}")

        print("\n📊 Final Report:")
        print(f"✅ TP: {tp_count} ({tp_rate:.2f}%)")
        print(f"❌ FP: {fp_count} ({fp_rate:.2f}%)")
        print(f"🔢 total: {total_parsed}")

    except FileNotFoundError:
        print("File Not Found")
    except Exception as e:
        print(f"⚠️ Error in execution {e}")

# execution:
file_path = r"C:\Users\MT\Desktop\ids-zeek-pcap\py\fast-A.log"  # مثلاً: "C:/logs/fast.log"
attack_start = "05/07/2025-14:23:33"
attack_end = "05/07/2025-14:24:08"

analyze_fast_log(file_path, attack_start, attack_end)
