

# this script installs the nuclear data for use by neutronics codes

export DATAPATH=$HOME/xdata

mkdir DATAPATH

cp additional_files/xsdir DATAPATH

cd $DATAPATH

wget https://www.oecd-nea.org/dbdata/jeff/jeff33/downloads/JEFF33-n_tsl-ace.tgz

tar -xvzf JEFF33-n_tsl-ace.tgz

mv JEFF33-n_tsl-ace j

wget https://www-nds.iaea.org/fendl/data/neutron/fendl31d-neutron-ace.zip

unzip fendl31d-neutron-ace.zip 

mv ace f

