##
## EPITECH PROJECT, 2021
## Caesar
## File description:
## Makefile
##

all:
	cp src/hex_to_base64.py challenge01
	cp src/xor_cipher.py challenge03

clean: fclean

fclean:
	rm challenge01
	rm challenge03

re: fclean all

.PHONY: all clean fclean re