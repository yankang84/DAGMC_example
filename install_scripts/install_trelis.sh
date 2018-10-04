

# prior to running this script install trelis RPM version from https://www.csimsoft.com/account/

# this script install assumes version 16.5 of trelis is installed

# use the included plugin or download the latest dagmc plugin from https://uwmadison.app.box.com/v/dagmc-trelis to your $HOME/Downloads folder

sudo cp additional_files/svalinn-plugin-linux.tgz /opt/Trelis-16.5/bin/plugins

cd /opt/Trelis-16.5/bin/plugins

sudo tar -xvzf DAGMC-Trelis-linux-mw.tgz

cd /opt/Trelis-16.5/bin/plugins/dagmc

sudo sh ./install.sh

export PATH=$PATH:/opt/Trelis-16.5/bin/