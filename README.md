# hw-temps-flask-api

I created this quick flask api to serve my computer's thermal readings to homeassistant. 

This project depends on Home Assistant, Python, Flask, lm-sensors, and liquidctl

api.py uses python's subprocess module to get lm-sensors or liquidctl (depending on the api call) json output from the system,
decodes UTF-8 into a string, and returns that json to the client (in this case, homeassistant).

rest.yaml goes in your homeassistant's configuration.yaml, and needs the line "rest: !include rest.yaml" to be recognized.
rest.yaml needs to modified it you are planning on using it yourself, the json returned from lm-sensors and liquidctl will vary
depending on hardware and kernel modules. I will include a sample json output from my own system, so you might be able to pick up
where to plug what in for your own setup. I also do some simple averages across multiple sensors in my rest.yaml to simplify what I display 
on my homeassistant dashboard for my computer.

bootstrap assumes you have this repo cloned into /root, that you want to serve to all ip-addresses available on port 5000, and
that you have a virtualenv set up in this repo, with flask installed in it. chmod +x ./bootstrap in this repo to make it executable.

add "@reboot /root/hw-temps-flask-api/bootstrap >/root/hw-temps-flask-api/flask.log 2>&1" to your root's cron to have it start on boot
and log to flask.log in this repo. if you stick with port 5000 you do not have to run it as root, you only need root for ports lower than 1024, 
however these files will need to be modified for that to work.

Cited Sources:
https://www.home-assistant.io
https://github.com/lm-sensors/lm-sensors
https://github.com/liquidctl/liquidctl
https://flask.palletsprojects.com/en/2.1.x/