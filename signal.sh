#!/usr/bin/bash
echo $(dbus-send --system --print-reply --dest=org.freedesktop.ModemManager /org/freedesktop/ModemManager/Modems/0 org.freedesktop.ModemManager.Modem.Gsm.Network.GetSignalQuality | grep -E "uint32\ [0-9]*" | sed 's/   uint32 //g')
