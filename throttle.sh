## Set
tc qdisc add dev wlp3s0 root netem delay 800ms
tc qdisc add dev wlp3s0 handle 1: root htb default 11
tc class add dev wlp3s0 parent 1: classid 1:1 htb rate 1kbps
tc class add dev wlp3s0 parent 1:1 classid 1:11 htb rate 1kbps

## Clear
#tc qdisc del dev wlp3s0 root
