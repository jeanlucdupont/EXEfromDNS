**EXEfromDNS** is a proof-of-concept (PoC) that demonstrates how to deliver a Windows executable over DNS using TXT records.

This project consists of:
- A minimal Windows x86 executable (~2.5 KB) written in assembly (GoAsm)
- A Python script that reconstructs the binary by querying DNS TXT records

The executable payload is base64-encoded, sliced into chunks, and stored as DNS **TXT records** under subdomains like:
chunk0.securityrabbits.com
chunk1.securityrabbits.com
...

This project is intended for educational, research, and red-team use only.
Do not use in any unauthorized environment. Misuse of this technique may violate laws or terms of service.
