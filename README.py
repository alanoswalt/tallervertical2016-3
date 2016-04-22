# tallervertical2016-3
#!/bin/sh

case "$1" in
	'start')
		python /home/manuel/tallervertical2016/scripts/getpic.py	
		tesseract /home/manuel/tallervertical2016/scripts/readme.jpg /home/manuel/tallervertical2016/scripts/out
		echo "Camion con ruta" > /home/manuel/tallervertical2016/scripts/out2.txt
		cat  /home/manuel/tallervertical2016/scripts/out.txt | grep -o '[[:digit:]]' >> /home/manuel/tallervertical2016/scripts/out2.txt
		#echo "     " >> /home/manuel/tallervertical2016/scripts/out2.txt
		eog /home/manuel/tallervertical2016/scripts/pics/3.jpg
		eog /home/manuel/tallervertical2016/scripts/readme.jpg
		festival --language spanish --tts /home/manuel/tallervertical2016/scripts/out2.txt;;
	'modsc')
		nano /etc/init.d/runme;;
	'modpy')
		nano /home/manuel/tallervertical2016/scripts/getpic.py;;
	*)
		echo "usa start"
		exit 1 ;;
esac
