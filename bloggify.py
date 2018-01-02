from datetime import date
import calendar
import sys

if len(sys.argv) == 1:
	k = open("../../../blog.txt", "r")
	skip = False
else:
	k = open("../../sites/blog/txt/" + sys.argv[1], "r")
	skip = True

def escri(s="", end="\n"):
	f.write(s + end)

def comment(s="", end="\n"):
	f.write("<!-- " + s + " -->" + end)

def eggify(s):
	ret = s
	ret = ret.replace("0", "<d__v class='turn~~ff'>0</d__v>")
	ret = ret.replace("1", "<d__v class='turn~~n'>1</d__v>")
	ret = ret.replace("o", "<d__v class='turn~~ff'>0</d__v>")
	ret = ret.replace("i", "<div class='turn~~n'>1</div>")
	ret = ret.replace("d__v", "div")
	ret = ret.replace("turn~~", "turno")
	return ret

colors = {"r":"rojo", "g":"verde", "b":"azul", "y":"amarillo"}

decnum, title, col, rooz = k.readline().strip(), k.readline().strip(), k.readline().strip(), k.readline().strip()

binnum = str(bin(int(decnum)))[2:]
if len(binnum) == 1:
	binnum = "0" + binnum
hexnum = str(hex(int(decnum)))[2:]
if len(hexnum) == 1:
	hexnum = "0" + hexnum

og = str(title)
title = eggify(title)

c = colors[col]

less = True
if not rooz:
	less = False
	dt = date.today()
	month = str(dt.month)
	if len(month) == 1:
		month = "0" + month
	day = str(dt.day)
	if len(day) == 1:
		day = "0" + day
	rooz = month + "." + day + "." + str(dt.year)[2:]

length = 0
count = 0
for line in k:
	for word in line.split():
		length += 1

k.seek(0)
k.readline()
k.readline()
k.readline()
k.readline()
if less:
	k.readline()

if length < 180:
	readtime = str(max(5, length//3)) + "s"
else:
	if length % 50 >= 25:
		length += 25
	length = length//50 * 50
	readtime = str(max(1, length//180 + (((length % 200)//90) * .5))) + "m"
length = str(length) + " words"

shortname = "bb"

num = eggify("0") + "<div id='binswitch'>b</div>" + eggify((8 - len(binnum))*"0" + binnum)
shortnum = eggify("0") + "<div id='hexswitch'>x</div>" + eggify(hexnum)

prevpost = str(bin(int(decnum) - 1))[2:]
if len(prevpost) == 1:
	prevpost = "0" + prevpost
nextpost = str(bin(int(decnum) + 1))[2:]
if len(nextpost) == 1:
	nextpost = "0" + nextpost

f = open("../../sites/blog/" + binnum + ".html", "w")

escri("<!DOCTYPE html>")
escri("<html>")
escri("<head>")
escri("\t<title>" + og + "</title>")
escri("\t<meta charset='utf-8'>")
escri("\t<link href='https://fonts.googleapis.com/css?family=PT+Mono' rel='stylesheet'>")
escri("\t<link href='https://fonts.googleapis.com/css?family=Montserrat:300,400,700' rel='stylesheet'>")
escri("\t<link rel='stylesheet' href='./assets/css/style.css'>")
escri("\t<link rel='shortcut icon' type='image/png' href='./assets/img/favicon.png'/>")
# escri("\t<link href='https://afeld.github.io/emoji-css/emoji.css' rel='stylesheet'>")
escri("</head>")
escri()

escri("<body>")
escri("\t<div id='topbar'>")
escri("\t\t<div id='topcontent'>")
escri("\t\t\t<div class='tbitem' id='shortname'><a class='homelink' href='http://brandonb.me/blog'>bb</a></div>")
escri("\t\t\t<div class='tbitem' id='longname'><a class='homelink' href='http://brandonb.me/blog'>brand</a><div class='turnoff'>0</div><a class='homelink' href='http://brandonb.me/blog'>n</a> <a class='homelink' href='http://brandonb.me/blog'>b</a><div class='turnon'>1</div><a class='homelink' href='http://brandonb.me/blog'>ts</a></div>")
escri("\t\t\t<div class='tbitem' id='longnum'>" + num + "</div>")
escri("\t\t\t<div class='tbitem' id='shortnum'>" + shortnum + "</div>")
escri("\t\t</div>")
escri("\t\t<div class='tbitem' id='title'>" + title + "</div>")
escri("\t</div>")
escri()

comment("\t<div id='egg'>\n\t\tinsert easter egg here\n\t</div>")
escri()

if int(decnum) > 0:
	escri("\t<a id='prev' href='http://brandonb.me/blog/" + prevpost + ".html'></a>")
	escri("\t<a id='iprev' href='http://brandonb.me/blog/" + prevpost + ".html'></a>")
	escri()

escri("\t<div id='story'>")
escri("\t\t<div id='info'>")
escri("\t\t\t<div class='infoitem'>" + rooz + "</div>")
escri("\t\t\t<div class='infoitem'>" + length + "</div>")
escri("\t\t\t<div class='infoitem'>" + readtime + "</div>")
escri("\t\t</div>")
escri()

flag = False
first = False

for line in k:
	line = line.strip()
	if first:
		if ":" in line and "." not in line:
			escri("<br><br>\n")
			escri("\t\t<b>" + line + "</b>", "")
			flag = True
		elif line:
			if flag:
				escri("<br>")
			else:
				escri("<br><br>\n")
			escri("\t\t" + line, "")
		else:
			flag = False
	else:
		escri("\t\t" + line, "")
		first = True
if not skip:
	k.seek(0)
	newfile = open("../../sites/blog/txt/" + binnum + ".txt", "w")
	count = 0
	for line in k:
		if not less and count == 3:
			newfile.write(rooz)
			newfile.write("\n")
		newfile.write(line)
		count += 1
	newfile.close()
k.close()

escri("\n\t</div>")
escri("</body>")
escri()

escri("\t<a id='next' href='http://brandonb.me/blog/" + nextpost + ".html'></a>")
escri("\t<a id='inext' href='http://brandonb.me/blog/" + nextpost + ".html'></a>")
escri()

escri("<script src='http://code.jquery.com/jquery-1.11.3.min.js'></script>")
escri("<script src='./assets/js/script.js'></script>")
escri()

escri("</html>")
escri()

f.close()

pad = 8 - len(binnum)
ze = binnum.replace("0", "<div class='ze'>0</div>")
if pad > 0:
	ze = "<div class='ze'>" + "0"*pad + "</div>" + ze

snum = ""
if len(og) < 10:
	snum = " sbi"

print("\n\t\t<div class='blogitem " + c + snum + "'>")

if snum:
	print("\t\t\t<a class='num snum' href='http://brandonb.me/blog/" + binnum + ".html'>" + ze + "</a>")
	print("\t\t\t<a class='name' href='http://brandonb.me/blog/" + binnum + ".html'>" + og + "</a>")
else:
	print("\t\t\t<a class='name' href='http://brandonb.me/blog/" + binnum + ".html'>" + og + "</a>")
	print("\t\t\t<a class='num' href='http://brandonb.me/blog/" + binnum + ".html'>" + ze + "</a>")
print("\t\t</div>")
