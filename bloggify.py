from datetime import date
import calendar

def myin(s):
	return input(s + "\n")

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

decnum = myin("What's the blog's number?")
binnum = str(bin(int(decnum)))[2:]
hexnum = str(hex(int(decnum)))[2:]

k = open("../../../blog.txt", "r")
f = open("../../sites/blog/" + binnum + ".html", "w")

length = 0
for line in k:
	for word in line.split():
		length += 1
k.seek(0)

if length < 180:
	readtime = str(max(5, length//3)) + "s"
else:
	length = length//50 * 50
	readtime = str(max(1, length//200 + (((length % 200)//90) * .5))) + "m"
length = str(length) + "words"

title = myin("What is the title of this blog?")
og = str(title)
title = eggify(title)

shortname = "bb"
shortname += len(hexnum)*"&nbsp;"

num = "&nbsp;&nbsp;0b" + max(0, 8 - len(binnum))*"0" + binnum
num = eggify(num)
shortnum = "0x" + hexnum
shortnum = eggify(shortnum)

prevpost = str(bin(int(decnum) - 1))[2:]
nextpost = str(bin(int(decnum) + 1))[2:]

dt = date.today()
rooz = str(dt.month) + "." + str(dt.day) + "." + str(dt.year)[2:]

escri("<!DOCTYPE html>")
escri("<html>")
escri("<head>")
escri("\t<title>" + og + "</title>")
escri("\t<meta charset='utf-8'>")
escri("\t<link href='https://fonts.googleapis.com/css?family=PT+Mono' rel='stylesheet'>")
escri("\t<link href='https://fonts.googleapis.com/css?family=Montserrat:300,400,700' rel='stylesheet'>")
escri("\t<link rel='stylesheet' href='./assets/style.css'>")
escri("\t<link rel='shortcut icon' type='image/png' href='./assets/favicon.png'/>")
escri("</head>")
escri()

escri("<body>")
escri("\t<div id='topbar'>")
escri("\t\t<div class='tbitem' id='shortname'><a class='homelink' href='http://brandonb.me/blog'>" + shortname + "</a></div>")
escri("\t\t<div class='tbitem'><a class='homelink' href='http://brandonb.me/blog'>brand</a><div class='turnoff'>0</div><a class='homelink' href='http://brandonb.me/blog'>n</a> <a class='homelink' href='http://brandonb.me/blog'>b</a><div class='turnon'>1</div><a class='homelink' href='http://brandonb.me/blog'>ts</a></div>")
escri("\t\t<div class='tbitem' id='title'>" + title + "</div>")
escri("\t\t<div class='tbitem'>" + num + "</div>")
escri("\t\t<div class='tbitem' id='shortnum'>" + shortnum + "</div>")
escri("\t</div>")
escri()

comment("\t<div id='egg'>\n\t\tinsert easter egg here\n\t</div>")
escri()

escri("\t<a id='prev' href='http://brandonb.me/blog/" + prevpost + "'></a>")
escri("\t<a id='iprev' href='http://brandonb.me/blog/" + prevpost + "'></a>")
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

escri("\n\t</div>")
escri("</body>")
escri()

comment("\t<a id='next' href='http://brandonb.me/blog/" + nextpost + "'></a>")
comment("\t<a id='inext' href='http://brandonb.me/blog/" + nextpost + "'></a>")
escri()

escri("<script src='http://code.jquery.com/jquery-1.11.3.min.js'></script>")
escri("<script src='./assets/script.js'></script>")
escri()

escri("</html>")
escri()

colors = {"r":"rojo", "g":"verde", "b":"azul", "y":"amarillo"}
c = colors[myin("What color should this be?")]

pad = 8 - len(binnum)
ze = binnum.replace("0", "<div class='ze'>0</div>")
if pad > 0:
	ze = "<div class='ze'>" + "0"*pad + "</div>" + ze

print("Add the following to index.html:\n")
print("<div class='blogitem " + c + "'>")

if len(og) < 13:
	print("\t\t\t<a class='num snum' href='http://brandonb.me/blog/" + binnum + "'>" + ze + "</a>")
	print("\t\t\t<a class='name' href='http://brandonb.me/blog/" + binnum + "'>" + og + "</a>")
else:
	print("\t\t\t<a class='name' href='http://brandonb.me/blog/" + binnum + "'>" + og + "</a>")
	print("\t\t\t<a class='num' href='http://brandonb.me/blog/" + binnum + "'>" + ze + "</a>")
print("\t\t</div>")
