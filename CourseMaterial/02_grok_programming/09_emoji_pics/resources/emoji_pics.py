#!/usr/bin/env python3

bw_emojis = "⬜⬛"
color_emojis = "⬜⬛🟥🟦🟪🟩🟨🩵"

#
# Black and white pictures
#
bw_emoji_pic_1 = "10102010121010201012"
bw_emoji_pic_2 = "111111100001111112111100000000011112111000000000001112110000000000000112110000000000000112100000000000000012100001100001100012100000100000100012100000000000000012100000000000000012110000000000000112110000100010000112111000011100001112111100000000011112111111000001111112"


#
# Gray scale pictures
#
gray_scale_emoji_pic_1 = "11100100220001101122"
gray_scale_emoji_pic_2 = "11111111111111000000001000000011221111111111000000000000001111110022111111110000000000000000111111002211111100000100000000000000111100221111000000000000000000000000100022111100000000111111111111000000112211000000001111110011001100000000221100100000111111001100110000000022001111000000111111111111110000002200111111001111001111111111000000221101111111110000000011110000001122111100001111111100000000000000112211111100000011111111100000000011221111000000000000000000000000111122110000010000000000000000001111112200000100000000000000010000001111220000000011111100000000000000111122000000111111111100010000000000112211000011111111110011110101000011221111000011111100011111010001010022110001010000000101010100010101002200000100010101010101010001010100220001010001010101000000000101010022000101000100000011111100010100002200010100001111111111111100000011221100001111111111111111111111111122"


#
# Color pictures
#
color_emoji_pic_1 = "111111111111111111111111111111111111111111111111111111111111111111111111000000000111111111111111111111111000000000111111111111111111000110110110000111111111111111111000110110110000111111111111000110110110000110000111111111111000110000110110110000111111111000110110110000000000000000000000000000000110110110000111111111111000000000000111111111111110110110110000000000000111111111111111111111000111111111111111111110110110110000111111111111111111111111111000111111111111111111110110110110000111111111111111111111111111000111111111111111111110110110110000111111111111111111111111111000111111000111111111000111110110000111111111111111111111111111000111111000000111111000000110110000111111111111111111111111111000111111111111111111111110110110000111111111111111111111111000111111111000000000000000000111110110000111111111111111111111000111111111000000000000000000111111111000111111111111111111111000111111111111000000000000111111111111000111111111111111111111000111111111111111111111111111000111111000111111111111111111111111000111111000000000000000000111111000111111111111111111111111111111000111111111111111111111111000111111111111111111111111111111111111000100100110110100100000111111111111111111111111111111111111000111111110110110110111111000111111111111111111111111111111111000111111110110110110111111000111111111000111111111111111111111000111111111111111111111111000111111000111000111111111111111000111111111111111111111111111111000111000111000111111111111000111111111111111000111000111111111111000000111000111111111111000111111000111111000111000111111000111000111111000111111111000111000111000111111000111000111111000111000111000000111010010000111111000000111111000000000111111000000111000000010010010010010000000010010000000010010010000000010010000000010010010010010010010010010010010010010010010010010010010010010010010010"
color_emoji_pic_2 = "111"


## REMOVE below when sharing w/ students


# Problem 1
for c in bw_emoji_pic_1:
    if c == "1":
        print("⬜️", end="")
    elif c == "0":
        print("⬛️", end="")
    else:
        print()

        
# Problem 2
while gray_scale_emoji_pic_1:
    pixel = gray_scale_emoji_pic_1[0:2]
    gray_scale_emoji_pic_1 = gray_scale_emoji_pic_1[2:]
    if pixel == "11":
        print("⬜️", end="")
    elif pixel == "10":
        print("🔲", end="")
    elif pixel == "01":
        print("🔳️", end="")
    elif pixel == "00":
        print("⬛️", end="")
    else:
        print("")


ite = 0
for _ in range(15):
    for _ in range(18):
        c = bw_emoji_pic_2[ite]
        if c == "1":
            print("⬜️", end="")
        elif c == "0":
            print("⬛️", end="")
        ite += 1
    print()

print()
print()
    
# Problem 3



# Problem 4
for _ in range(40):
    for _ in range(21):
        pixel = color_emoji_pic_1[0:3]
        color_emoji_pic_1 = color_emoji_pic_1[3:]
        if pixel == "111":
            print("⬜", end="")
        elif pixel == "000":
            print("⬛", end="")
        elif pixel == "100":
            print("🟥", end="")
        elif pixel == "001":
            print("🟦", end="")
        elif pixel == "010":
            print("🟩", end="")
        elif pixel == "110":
            print("🟨", end="")
        elif pixel == "101":
            print("🟪", end="")
        elif pixel == "011":
            print("🩵", end="")
    print()