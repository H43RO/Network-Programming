import socket
import struct
import binascii


class Udphr:
    def __init__(self, sport, dport, length, checksum):
        self.sport = sport
        self.dport = dport
        self.length = length
        self.checksum = checksum

    def pack_Udphr(self):
        packed = struct.pack("!HHHH", self.sport, self.dport, self.length, self.checksum)
        return packed


def unpack_Udphr(buffer):
    unpacked = struct.unpack('!HHHH', buffer)
    return unpacked


def getSrcPort(unpacked):
    return unpacked[0]


def getDstPort(unpacked):
    return unpacked[1]


def getLength(unpacked):
    return unpacked[2]


def getChecksum(unpacked):
    return unpacked[3]


if __name__ == '__main__':
    udp = Udphr(5555, 80, 1000, 0xFFFF)
    packed_udphr = udp.pack_Udphr()
    print('Packed :', binascii.b2a_hex(packed_udphr))

    unpack_udphr = unpack_Udphr(packed_udphr)  # Tuple 형태로 리턴
    print('Unpacked :', unpack_udphr)
    print()

    print('=' * 20)
    print(f'Source Port : {getSrcPort(unpack_udphr)}')
    print(f'Destination Port : {getDstPort(unpack_udphr)}')
    print(f'Length : {getLength(unpack_udphr)}')
    print(f'Checksum : {getChecksum(unpack_udphr)}')