##
## EPITECH PROJECT, 2021
## Caesar
## File description:
## Makefile
##

all:
	cp src/hex_to_base64.py challenge01
	cp src/xor_fixed.py challenge02
	cp src/xor_cipher.py challenge03
	cp src/xor_detect.py challenge04
	cp src/xor_repeating.py challenge05
	cp src/xor_break_repeating.py challenge06
	cp src/aes_in_ecb.py challenge07
	cp src/detect_aes_in_ecb.py challenge08
	cp src/cbc.py challenge09
	cp src/ecb_decryption.py challenge10

clean: fclean

fclean:
	rm challenge01
	rm challenge02
	rm challenge03
	rm challenge04
	rm challenge05
	rm challenge06
	rm challenge07
	rm challenge08
	rm challenge09
	rm challenge10

re: fclean all

.PHONY: all clean fclean re
