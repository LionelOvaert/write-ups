import urllib.parse

with open("transmissions") as f:
    data = f.readlines()
    parts = {}
    for line in data:
        # URL decode the line and remove the garbage
        line = urllib.parse.unquote(line.strip().replace("kxkxkxkxsh", ""))
        # 2-digit number
        if line[-2:].isnumeric():
            nb = int(line[-2:])
            part = line[: len(line) - 3]
            parts[nb] = part
            if nb == 67:
                # Last part contains 2 elements
                part = line[len(part):len(line) - 2]
                parts[nb + 1] = part
        # 1-digit number
        else:
            nb = int(line[-1:])
            part = line[: len(line) - 2]
            parts[nb] = part

    flag = ""
    for nb in sorted(parts.keys()):
        flag += parts[nb]
    print(flag)

