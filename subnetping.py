import ping3
import ipaddress


def ping_subnet(subnet):
    network = ipaddress.ip_network(subnet)

    for ip in network.hosts():
        ip_str = str(ip)
        response_time = ping3.ping(ip_str, timeout=1)

        if response_time is not None:
            print(f'{ip_str} is reachable. Response time: {response_time} ms.')
        else:
            print(f'{ip_str} is unreachable.')


# Get user input for the subnet and subnet mask
subnet_input = input('Enter the subnet (e.g., 192.168.0.0/24): ')

# Call the function to ping the subnet
ping_subnet(subnet_input)
