# Remove spaces at the beginning and at the end of the string

# txt = "         banana          "
# print(txt)
# x = txt.strip()
# print(x)


##########################################
# A set of characters to remove as leading/trailing characters.

txt = ",,,,rrttgg.....banana......rrr"
print(txt)
x = txt.strip(",rtg.")
print(x)