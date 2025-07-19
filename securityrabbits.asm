DATA SECTION
    srmsg db "Hi from SecurityRabbits.com !", 13, 10

CODE SECTION

start:
    invoke GetStdHandle, -11
    invoke WriteConsoleA, eax, ADDR srmsg, SIZEOF srmsg, 0, 0
    invoke ExitProcess, 0
