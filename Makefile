##
## EPITECH PROJECT, 2019
## SEC_crypto_2019
## File description:
## Makefile
##

all: 	
		cp src/hex_to_base.py challenge01
		cp src/fixed_xor.py challenge02
		cp src/xorcipher.py challenge03
		cp src/detect_xor.py challenge04
		cp src/repeating_xor.py challenge05
		cp src/break_repeating_xor.py challenge06
		cp src/aes_ecb.py challenge07

clean: fclean

fclean:
	rm challenge01
	rm challenge02
	rm challenge03
	rm challenge04
	rm challenge05
	rm challenge06
	rm challenge07

re: fclean all

.PHONY: all clean fclean re