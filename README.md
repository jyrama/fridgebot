# Fridgebot

Symlink sink modules, you want to use, to under the *sinks*
folder and run *AlertBot.py* with Python3. For Mattermost
one needs a bit more config, help for that is included below.
Couple of sinks included can be found under *sinks-available*.

## Mattermost integration
Set your Mattermost incoming webhook's url in config.json.

## Install

1. Clone the project source to your preferred path of your favourite stuff.
2. Start project with Python3.

Consider creating a Systemd service where Systemd is available.

## Writing more sinks

The basic concept for a Fridgebot sink is simple:

1. The sink to be loaded must find itself under the *sinks* folder.
2. It will have an attribute *config* set by its loader in AlertBot.
   The config variable will then include settings specified in config.json
   by the user.
2. It can setup what ever module level variables during loading.
   This scheme has changed **just a bit** in during few interesting commits.
   As of writing this line, the sink module to be loaded can also include an
   initialization function, **init()**, which can address config variables
   set to module's own attribute *config* which is set by the loader in
   AlertBot during loading all the sink modules available.
4. Its filename must end in *.py*.
5. It must implement methods *notify()* and *thanks()* besides the *init()*
   mentioned before. These are called for sending complaints for open doors
   and thanks for closing them afterwards.

## Systemd user service

One using Systemd might use Fridgebot as a user service. An example
.service file configuration can be found from *fridgebot.service.example*.
This can be copied, with modifications some notifications where needed,
to *~/.config/systemd/user/fridgebot.service*. At least check your working
directory, please.

Enable lingering for the user for running the service without a session:

	loginctl enable-linger best-user

The service has to be enable before starting:

	systemd --user enable fridgebot

Start it:

	systemd --user start fridgebot

Check its status:

	systemd --user status fridgebot

Your ice cream is now saved.
