import re

asd = """
    Hii, My name is siddahrth
    I am a Python developer
"""

re_pattern_name = r"name is \w+"
re_stack_pattern = r"am a [\w\s]+"

for i in asd.split("\n"):
    # breakpoint()
    if re.search(re_pattern_name, i):
        print(re.search(re_pattern_name, i).group(0).replace("name is ","").strip())
    if re.search(re_stack_pattern, i):
        print(re.search(re_stack_pattern, i).group(0).replace("am a ","").strip())
    print(i)


d = "[a-zA-Z]+.\d+"
ipv4 = "((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|([1-9]?[0-9])).){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])"
ipv6 = "((([0-9a-fA-F]){1,4}):){7}([0-9a-fA-F]){1,4}"

ipv4ss = "^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$"

print(bool(re.search(ipv4, "127.302.0.1")))
breakpoint()
