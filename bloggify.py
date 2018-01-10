from datetime import date
import calendar
import sys

skip = False
if len(sys.argv) == 1:
	k = open("../../../blog.txt", "r")
else:
	skip = True
	try:
		k = open("../../sites/blog/txt/" + sys.argv[1], "r")

	except:
		try:
			k = open(sys.argv[1], "r")
	
		except:
			print("ERROR")

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

decnum, title, col, rooz, egg = k.readline().strip(), k.readline().strip(), k.readline().strip(), k.readline().strip(), k.readline().strip()

binnum = str(bin(int(decnum)))[2:]
if len(binnum) == 1:
	binnum = "0" + binnum
hexnum = str(hex(int(decnum)))[2:]
if len(hexnum) == 1:
	hexnum = "0" + hexnum

og = str(title)
title = eggify(title)

rang = True
if col == "x":
	c = colors.popitem()[1]
	rang = False
else:
	c = colors[col]

less = True
if rooz == "x":
	less = False
	dt = date.today()
	month = str(dt.month)
	if len(month) == 1:
		month = "0" + month
	day = str(dt.day)
	if len(day) == 1:
		day = "0" + day
	rooz = month + "." + day + "." + str(dt.year)[2:]

if egg == "x":
	egg = False

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
k.readline()
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
escri("\t<meta name='viewport' content='width=device-width,initial-scale=1.0'>")
escri("\t<link href='https://fonts.googleapis.com/css?family=PT+Mono' rel='stylesheet'>")
escri("\t<link href='https://fonts.googleapis.com/css?family=Montserrat:300,400,700' rel='stylesheet'>")
escri("\t<link rel='stylesheet' href='./assets/css/style.css'>")
escri("\t<link rel='shortcut icon' type='image/png' href='./assets/img/favicon.png'/>")
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

if not egg:
	comment("\t<div id='egg'>\n\t\tinsert easter egg here\n\t</div>")
else:
	escri("\t<div id='egg'>\n\t\t" + egg + "\n\t</div>")
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

flag = False
first = False
nolim = False
pre = False
after = False

for line in k:
	if "<pre>" in line:
		pre = True
	if "</pre>" in line:
		pre = False
		after = True
	if not pre and not after:
		line = line.strip()
	if first:
		if ":" in line and "." not in line and "nobold" not in line:
			escri("<br><br>\n")
			escri("\t\t<b>" + line + "</b>", "")
			flag = True
			if "nolim" in line:
				nolim = True
		elif line:
			if "<pre>" in line:
				escri()
				escri(line, "")
			elif not pre and not after:
				if flag:
					if not nolim:
						escri("<br>")
					escri()
				else:
					escri("<br><br>\n")
				if "nobold" in line:
					escri("\t\t" + line[8:])
				else:
					escri("\t\t" + line, "")
			else:
				after = False
				if "</pre>" in line:
					escri(line[:len(line)-1], "")
				else:
					escri(line, "")
			nolim = False
		else:
			flag = False
			nolim = False
	else:
		escri("\t\t" + line, "")
		first = True
k.seek(0)

count = 0
towrite = []
for line in k:
	if not rang and count == 2:
		towrite.append(c)
		towrite.append("\n")
	elif not less and count == 3:
		towrite.append(rooz)
		towrite.append("\n")
	else:
		towrite.append(line)
	count += 1
k.close()

newfile = open("../../sites/blog/txt/" + binnum + ".txt", "w")
for line in towrite:
	newfile.write(line)
newfile.close()

escri("\n\t</div>")
escri()

escri("\t<a id='next' href='http://brandonb.me/blog/" + nextpost + ".html'></a>")
escri("\t<a id='inext' href='http://brandonb.me/blog/" + nextpost + ".html'></a>")
escri("</body>")
escri()

escri("<script src='http://code.jquery.com/jquery-1.11.3.min.js'></script>")
escri("<script src='./assets/js/script.js'></script>")
escri()

escri("</html>")
f.close()

if not skip:
	fourohfour = open("../../sites/blog/404.html", "w")
	fourohfour.write("<!DOCTYPE html>\n")
	fourohfour.write("<html>\n")
	fourohfour.write("<head>\n")
	fourohfour.write("\t<title>brand0n b1ts</title>\n")
	fourohfour.write("\t<meta charset='utf-8'>\n")
	fourohfour.write("\t<meta name='viewport' content='width=device-width, initial-scale=1.0, maximum-scale=1.0'/>\n")
	fourohfour.write("\t<link href='https://fonts.googleapis.com/css?family=PT+Mono' rel='stylesheet'>\n")
	fourohfour.write("\t<link rel='stylesheet' href='./assets/css/404.css'>\n")
	fourohfour.write("\t<link rel='shortcut icon' type='image/png' href='./assets/img/favicon.png'/>\n")
	fourohfour.write("</head>\n")
	fourohfour.write("\n")
	fourohfour.write("<body background='./assets/img/404.png'>\n")
	fourohfour.write("\t<div id='title'>\n")
	fourohfour.write("\t\t4<div class='turnoff'>0</div>4<div class='turnon'>!</div>\n")
	fourohfour.write("\t</div>\n")
	fourohfour.write("\n")
	fourohfour.write("\t<a id='prev' href='http://brandonb.me/blog/" + binnum + ".html'></a>\n")
	fourohfour.write("\t<a id='iprev' href='http://brandonb.me/blog/" + binnum + ".html'></a>\n")
	fourohfour.write("\n")
	fourohfour.write("\t<a id='next' href='http://brandonb.me/blog'></a>\n")
	fourohfour.write("\t<a id='inext' href='http://brandonb.me/blog'></a>\n")
	fourohfour.write("</body>\n")
	fourohfour.write("\n")
	fourohfour.write("<script src='http://code.jquery.com/jquery-1.11.3.min.js'></script>\n")
	fourohfour.write("<script src='./assets/js/404.js'></script>\n")
	fourohfour.write("\n")
	fourohfour.write("</html>\n")
	fourohfour.close()

	pad = 8 - len(binnum)
	ze = binnum.replace("0", "<div class='ze'>0</div>")
	if pad > 0:
		ze = "<div class='ze'>" + "0"*pad + "</div>" + ze

	count = 0
	stop = 24 + 4*int(decnum)
	towrite = []
	index = open("../../sites/blog/index.html", "r")
	for line in index:
		if count != stop:
			towrite.append(line)
		else:
			towrite.append("\t\t<div class='blogitem " + c + "'>\n")
			towrite.append("\t\t\t<a class='num' href='http://brandonb.me/blog/" + binnum + ".html'>" + ze + "</a>\n")
			towrite.append("\t\t\t<a class='name' href='http://brandonb.me/blog/" + binnum + ".html'>" + og + "</a>\n")
			towrite.append("\t\t</div>\n")
			towrite.append(line)
		count += 1
	index.close()

	index = open("../../sites/blog/index.html", "w")
	for line in towrite:
		index.write(line)
	index.close()
