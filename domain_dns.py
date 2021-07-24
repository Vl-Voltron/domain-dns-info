import dns.resolver

print("=====")

print("Domain name: ")
domain = input()
answer = dns.resolver.query(domain, "a")
print(f"Domain name {domain}  is pointed to the following IP addresses: ")
for data in answer:
    print(data.address)

# Finding NS record
result_ns = dns.resolver.query(domain, 'NS')
print()
# Printing record
for val_ns in result_ns:

    print('Name server : ', val_ns.to_text())
print("=====")