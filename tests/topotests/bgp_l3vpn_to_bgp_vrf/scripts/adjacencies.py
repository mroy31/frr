from lutil import luCommand

luCommand("ce1", 'vtysh -c "show bgp summary"', " 00:0", "wait", "Adjacencies up", 180)
luCommand("ce2", 'vtysh -c "show bgp summary"', " 00:0", "wait", "Adjacencies up", 180)
luCommand("ce3", 'vtysh -c "show bgp summary"', " 00:0", "wait", "Adjacencies up", 180)
luCommand(
    "ce4", 'vtysh -c "show bgp vrf all summary"', " 00:0", "wait", "Adjacencies up", 180
)
luCommand(
    "r1", "ping 2.2.2.2 -c 1", " 0. packet loss", "wait", "PE->P2 (loopback) ping", 60
)
luCommand(
    "r3", "ping 2.2.2.2 -c 1", " 0. packet loss", "wait", "PE->P2 (loopback) ping", 60
)
luCommand(
    "r4", "ping 2.2.2.2 -c 1", " 0. packet loss", "wait", "PE->P2 (loopback) ping", 60
)
luCommand(
    "r2",
    'vtysh -c "show bgp summary"',
    " 00:0.* 00:0.* 00:0",
    "wait",
    "Core adjacencies up",
    180,
)
luCommand(
    "r1", 'vtysh -c "show bgp summary"', " 00:0", "wait", "Core adjacencies up", 180
)
luCommand(
    "r3", 'vtysh -c "show bgp summary"', " 00:0", "wait", "Core adjacencies up", 180
)
luCommand(
    "r4", 'vtysh -c "show bgp summary"', " 00:0", "wait", "Core adjacencies up", 180
)
luCommand(
    "r1",
    'vtysh -c "show bgp vrf all summary"',
    " 00:0.* 00:0",
    "pass",
    "All adjacencies up",
)
luCommand(
    "r3",
    'vtysh -c "show bgp vrf all summary"',
    " 00:0.* 00:0",
    "pass",
    "All adjacencies up",
)
luCommand(
    "r4",
    'vtysh -c "show bgp vrf all summary"',
    " 00:0.* 00:0.* 00:0",
    "pass",
    "All adjacencies up",
)
luCommand(
    "r1", "ping 3.3.3.3 -c 1", " 0. packet loss", "wait", "PE->PE3 (loopback) ping"
)
luCommand(
    "r1", "ping 4.4.4.4 -c 1", " 0. packet loss", "wait", "PE->PE4 (loopback) ping"
)
luCommand(
    "r4", "ping 3.3.3.3 -c 1", " 0. packet loss", "wait", "PE->PE3 (loopback) ping"
)
