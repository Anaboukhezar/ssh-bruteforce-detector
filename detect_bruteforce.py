

# ===== Version 1 : lire un fichier de logs et afficher les échecs SSH =====
# with open("auth_test.log", "r") as f:
#     for line in f:
#         if "Failed password" in line:
#             print(line.strip())

# ===== Version 2 : extraire l'IP et le compte des échecs SSH =====
# import re
#
# pattern = re.compile(
#     r"Failed password for (?:invalid user )?(\S+) from (\d{1,3}(?:\.\d{1,3}){3})"
# )
#
# with open("auth_test.log", "r") as f:
#     for line in f:
#         match = pattern.search(line)
#         if match:
#             user, ip = match.groups()
#             print(ip, user)

# ===== Version 3 : compter les échecs par IP =====
import re
from collections import defaultdict

pattern = re.compile(
    r"Failed password for (?:invalid user )?(\S+) from (\d{1,3}(?:\.\d{1,3}){3})"
)

failures = defaultdict(int)

with open("auth_test.log", "r") as f:
    for line in f:
        match = pattern.search(line)
        if match:
            user, ip = match.groups()
            failures[ip] += 1

# ===== Version 4 : appliquer un seuil =====
THRESHOLD = 2

suspects = {ip: count for ip, count in failures.items() if count >= THRESHOLD}

print(f"IP suspectes (>= {THRESHOLD} échecs) : {len(suspects)}")
for ip, count in sorted(suspects.items(), key=lambda x: x[1], reverse=True):
    print(ip, count)
