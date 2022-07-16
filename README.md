# Warpswitch
A simple python script to turn on and off Warp on Linux machine.

## What's Warp?
>The Cloudflare WARP client allows individuals and organizations to have a faster, more secure, and more private experience online. The WARP client sits between your device and the Internet, and has several connection modes to better suit different needs.(For more detail, visit [here](https://developers.cloudflare.com/warp-client/)).

*Warp install on Linux machine: visit [here](https://developers.cloudflare.com/warp-client/get-started/linux/)*

## What does this script do?

Depend on your ISP, there'll be some sites can be reached and we need Warp to access.

**But** sometimes Warp make us can't access to some other sites, apps that can connect normally when Warp is off. And turn it on and off several time on Linux with command `warp-cli connect/disconnect` just take more time than you thought. 

**Anddddddd it'time for Warpswitch to do its job.**

Just run it as a normal python file, and up to current Warp status Warpswitch will do the action connect/disconnect.

To make everything even more convenient, the file is executable with ./warpswitch.py( Run chmod +x warpswitch.py if the file is not executabe anymore after download).

Also, move/copy the executable file to bin folder make it can execute without cd to `path-to-file`.
