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


# Check for flags and input arguments.
while getopts "nh" option; do
  case $option in
    n) nato_flag=true;;
    h) help_flag=true;;
    *) echo "Invalid option: -$OPTARG" >&2; exit 1;;
  esac
done
shift $((OPTIND-1))  # Removes the flag when passing in the input string. Assumes 1 flag exists.

# Display help message and exit if the help flag is set
if [ "$help_flag" = true ]; then
  cat <<EOF
-----
Usage: lingo [-n|-h] [TEXT]
    -n: Use NATO phonetic alphabet (if implemented)
    -h: Display this help message and exit
    TEXT: The text to convert (optional, prompts if not provided)
-----
EOF
  exit 0
fi


# Get input string, either from CLI arguments or user prompt
if [[ $# -gt 0 ]]; then
  input_string="$1"
else
  read -p "Enter text to convert: " input_string
fi

for ((i = 0; i < ${#input_string}; i++));
do
	curr_char=${input_string:$i:1}

	if [ "$curr_char" == " " ]; then
		echo
		continue
	elif [[ $curr_char =~ [[:alpha:]] ]]; then
        phonetic_word=$(letter_to_word "$curr_char")
        echo "$curr_char: $phonetic_word"
    else
        echo $curr_char
    fi
done