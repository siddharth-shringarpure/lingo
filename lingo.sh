#!/bin/bash

letter_to_word() {
	case ${1,,} in
		a) echo "Alpha";;
		b) echo "Bravo";;
		c) echo "Charlie";;
		d) echo "Delta";;
		e) echo "Echo";;
		f) echo "Foxtrot";;
		g) echo "Golf";;
		h) echo "Hotel";;
		i) echo "India";;
		j) echo "Juliett";;
		k) echo "Kilo";;
		l) echo "Lima";;
		m) echo "Mike";;
		n) echo "November";;
		o) echo "Oscar";;
		p) echo "Papa";;
		q) echo "Quebec";;
		r) echo "Romeo";;
		s) echo "Sierra";;
		t) echo "Tango";;
		u) echo "Uniform";;
		v) echo "Victor";;
		w) echo "Whiskey";;
		x) echo "X-ray";;
		y) echo "Yankee";;
		z) echo "Zulu";;
		*) echo;;
	esac
}

# Main

read -p "Enter text to convert: " input_string

for ((i = 0; i < ${#input_string}; i++));
do
	curr_char=${input_string:$i:1}

	if [ $curr_char == " " ]; then
		echo
		continue
	else
		if [[ $curr_char =~ [[:alpha:]] ]]; then
			phonetic_word=$(letter_to_word "$curr_char")
			echo "$curr_char: $phonetic_word"
		fi
	fi
done