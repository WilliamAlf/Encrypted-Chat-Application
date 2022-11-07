# Encrypted-Chat-Application

Uppsala University

Public-private key encryted peer to peer chat application for secure communication.

Notes:
The peer to peer infrastructure provides a private unicast connection between communicating peers. Every message is only forwarded between the peers from their machine and network intermediaries to receiving peer. No message reaches any server, that is not part of the general network infrastructure. Thus peers have high control over their messages and no message is saved at any point other than by peers. Packet sniffers connected to the same network as a peer will only see encrypted messages, ensuring authenticity in the sending and receiving endpoints.
