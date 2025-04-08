"""
Network Topology Validator
Purpose: Verify device adjacency after power restoration
Dependencies: napalm, netmiko
"""

from napalm import get_network_driver

def validate_layer2_recovery():
    """Checks STP convergence and VLAN consistency"""
    driver = get_network_driver('ios')
    devices = ['core-sw1.example.com', 'edge-sw1.example.com']
    
    for device in devices:
        print(f"\n🔍 Validating {device}...")
        with driver(device, 'admin', 'S3cr3t!') as conn:
            print("STP Root Bridge:", conn.get_spanning_tree()['root']['root_switch'])
            print("Active VLANs:", [vlan for vlan, data in conn.get_vlans().items() if data['status'] == 'active'])

if __name__ == "__main__":
    validate_layer2_recovery()
