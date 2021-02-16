
# To look for any line that contains "thon"
grep thon /usr/share/dict/words

# The -i means case insensitive
grep -i python /usr/share/dict/words

# A . dot matches any character
grep l.ts /usr/share/dict/words

# A ^ circumflex indicates the string is at beginning of a line
grep ^fruit /usr/share/dict/words

# A $ indicates the string is at the end of a line
grep cat$ /usr/share/dict/words
