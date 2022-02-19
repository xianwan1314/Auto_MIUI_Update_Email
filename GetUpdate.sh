devices="
#umi=Mi10
#thyme=Mi10S
#cmi=Mi10Pro
#cas=Mi10Ultra
#vangogh=Mi10Lite
#venus=Mi11
#star=Mi11Ultra
#renoir=Mi11Lite
#cupid=Mi12
#zeus=Mi12Pro
#psyche=Mi12X
#odin=MiMix4
#cetus=MiMixFold
#nabu=MiPad5
#elish=MiPad5ProWIFI
#enuma=MiPad5Pro5G
#phoenix=RedmiK30
#picasso=RedmiK305G
#lmi=RedmiK30Pro
#cezanne=RedmiK30Ultra
#apollo=RedmiK30S
#alioth=RedmiK40
#haydn=RedmiK40Pro
#ares=RedmiK40Gaming
#ingres=RedmiK50Gaming
"
clear
for device in ${devices}
	do
	model=$(echo ${device} | cut -d = -f2)
	device=$(echo ${device} | cut -d = -f1)
	python3 GetUpdate.py ${device} >> NewLink.txt
done
exit
