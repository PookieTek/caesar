##
## EPITECH PROJECT, 2021
## Caesar
## File description:
## Makefile
##

all:
	cp src/hex_to_base64.py challenge01

clean: fclean

fclean:
	rm challenge01

re: fclean all

.PHONY: all clean fclean re